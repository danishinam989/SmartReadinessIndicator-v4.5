import json
import boto3
import os
from datetime import datetime
import io
from botocore.exceptions import ClientError
import logging
from urllib.parse import quote
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from modules.recommendations import SRIOptimizer
from typing import Dict, Any

# Initialize FastAPI sri_upgrade_app
sri_upgrade_app = FastAPI(
    title="SRI Upgrade API", description="API for analyzing SRI upgrades"
)

# Add CORS middleware
sri_upgrade_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize AWS services
s3 = boto3.client("s3")

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# S3 bucket configurations
REPORTS_BUCKET = "blockchained-sri-upgrade-reports"
WEIGHTS_PREFIX = "weights"
SCORES_BUCKET = "blockchained-sri-scores"
BUILDINGS_PREFIX = "buildings"

# Get AWS region
AWS_REGION = os.environ.get("AWS_REGION", "eu-west-1")


def load_json_from_s3(bucket, key):
    """Helper function to load JSON from S3"""
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        return json.loads(response["Body"].read().decode("utf-8"))
    except ClientError as e:
        logger.error(f"Error loading from S3 - Bucket: {bucket}, Key: {key}: {str(e)}")
        raise


def load_weights():
    """Load all weight files from S3"""
    try:
        weight_files = [
            "energy_efficiency_weights.json",
            "energy_flexibility_weights.json",
            "comfort_weights.json",
            "convenience_weights.json",
            "health_weights.json",
            "maintenance_weights.json",
            "information_weights.json",
        ]

        weights = []
        for file_name in weight_files:
            weights.append(
                load_json_from_s3(REPORTS_BUCKET, f"{WEIGHTS_PREFIX}/{file_name}")
            )

        pricing = load_json_from_s3(
            REPORTS_BUCKET, f"{WEIGHTS_PREFIX}/pricing_weights.json"
        )

        return weights, pricing

    except Exception as e:
        logger.error(f"Error loading weights: {str(e)}")
        raise


def load_building_answers(building_id):
    """Load current building answers from S3"""
    try:
        key = f"{BUILDINGS_PREFIX}/{building_id}/{building_id}_sri-submit.json"
        data = load_json_from_s3(SCORES_BUCKET, key)
        return data
    except Exception as e:
        logger.error(f"Error loading building answers for {building_id}: {str(e)}")
        raise


def validate_input(body):
    """Validate the input parameters"""
    try:
        if "building_id" not in body:
            raise ValueError("building_id is required")
        if "upgrade" not in body:
            raise ValueError("upgrade is required")

        budget = int(body["upgrade"])
        if budget <= 0:
            raise ValueError("upgrade must be a positive number")

        return body["building_id"], budget

    except KeyError as e:
        raise ValueError(f"Invalid input format: {str(e)}")


def analyze_building_upgrades(building_id, weights, pricing, current_answers, budget, output_pdf):
    """Main function to analyze upgrades and generate report"""
    optimizer = SRIOptimizer()

    try:
        current_scores = optimizer.calculate_current_scores(current_answers, weights)
        upgrades = optimizer.get_possible_upgrades(
            current_answers, weights, pricing, budget
        )
        chosen = optimizer.optimize(upgrades, budget)
        future_scores = optimizer.calculate_upgrade_scores(current_scores, chosen)
        total_cost = sum(u["cost"] for u in chosen)

        results = {
            "upgrades": chosen,
            "total_cost": total_cost,
            "remaining_budget": budget - total_cost,
            "current_scores": current_scores,
            "future_scores": future_scores,
            "domain_impacts": {
                d: future_scores[d] - current_scores[d] for d in optimizer.domain_names
            },
        }
        
        '''
        #generate_pdf_report(self, results, building_id, current_answers, output_path):
        '''
        optimizer.generate_pdf_report(building_id, results, output_pdf) 
        return results

    except Exception as e:
        logger.error(f"Error during analysis: {str(e)}")
        raise


@sri_upgrade_app.post("/sri_upgrade_report")
async def analyze_upgrades(request: Request):
    """
    Analyze SRI upgrades for a building

    Accepts two formats:
    1. Direct JSON: {"building_id": "BLDG_0006", "upgrade": "50000"}
    2. Lambda-style: {"body": "{\"building_id\": \"BLDG_0006\", \"upgrade\": \"50000\"}"}

    Returns upgrade recommendations and a PDF report URL
    """
    try:
        # Parse the request body
        request_data = await request.json()

        # Handle Lambda-style request with nested body
        if "body" in request_data:
            # If body is a string, parse it as JSON
            if isinstance(request_data["body"], str):
                try:
                    body = json.loads(request_data["body"])
                except json.JSONDecodeError:
                    raise ValueError("Invalid JSON in request body")
            else:
                # If body is already a dictionary
                body = request_data["body"]
        else:
            # Direct JSON format
            body = request_data

        building_id, budget = validate_input(body)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Generate PDF key using the requested format
        pdf_key = f"{BUILDINGS_PREFIX}/{building_id}/{timestamp}_report.pdf"

        # Create a temporary file-like object for the PDF
        pdf_buffer = io.BytesIO()

        weights, pricing = load_weights()
        current_answers = load_building_answers(building_id)

        results = analyze_building_upgrades(
            building_id, weights, pricing, current_answers, budget, pdf_buffer
        )

        # Upload PDF to S3 with public-read ACL
        pdf_buffer.seek(0)
        s3.put_object(
            Bucket=REPORTS_BUCKET,
            Key=pdf_key,
            Body=pdf_buffer.getvalue(),
            ContentType="application/pdf",
        )

        # Generate direct S3 URL
        s3_url = (
            f"https://{REPORTS_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{quote(pdf_key)}"
        )

        # return {
        #     "message": "Report generated successfully",
        #     "status": "success",
        #     "body": {
        #         "building_id": building_id,
        #         "results": results,
        #         "key": pdf_key,
        #         "s3_uri": f"s3://{REPORTS_BUCKET}/{pdf_key}",
        #         "s3_url": s3_url,
        #         "timestamp": timestamp,
        #     },
        # }
    
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'message': 'Report generated successfully',
                'status': 'success',
                'data':{
                    'building_id': building_id,
                    'results': results,
                    'key': pdf_key,
                    's3_uri': f"s3://{REPORTS_BUCKET}/{pdf_key}",
                    's3_url': s3_url,
                    'timestamp': timestamp
                }
                
            })
        }

    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@sri_upgrade_app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "SRI Upgrade API"}
