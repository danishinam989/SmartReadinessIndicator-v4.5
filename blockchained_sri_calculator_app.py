from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Any
import json

# Import your existing modules
from modules.CoolingDomain import sri_score_cooling, calculate_sri_score_cooling
from modules.HeatingDomain import sri_score_heating, calculate_sri_score_heating
from modules.DWHDomain import sri_score_DWH, calculate_sri_score_DWH
from modules.LightingDomain import sri_score_lighting, calculate_sri_score_lighting
from modules.VentilationDomain import (
    sri_score_ventilation,
    calculate_sri_score_ventilation,
)
from modules.DynamicBuildingEnvelopeDomain import (
    sri_score_envelope,
    calculate_sri_score_envelope,
)
from modules.EVChargingDomain import (
    sri_score_ev_charging,
    calculate_sri_score_ev_charging,
)
from modules.ElectricityDomain import (
    sri_score_electricity,
    calculate_sri_score_electricity,
)
from modules.MonitoringAndControlDomain import (
    sri_score_monitoring,
    calculate_sri_score_monitoring,
)
from modules.total_sri_score import calculate_final_sri_score

sri_calculator_app = FastAPI(
    title="SRI Calculator API", description="API for calculating SRI scores"
)


class SRIRequest(BaseModel):
    """Request model for SRI calculation"""

    body: Dict[str, str] = Field(..., description="Form data with answers q1-q57")


def split_form_data(body: Dict[str, str]) -> Dict[str, Dict[str, str]]:
    domains = {
        "heating": (1, 10),
        "cooling": (11, 20),
        "dwh": (21, 25),
        "lighting": (26, 30),
        "ventilation": (31, 36),
        "envelope": (37, 39),
        "ev_charging": (40, 42),
        "electricity": (43, 49),
        "monitoring": (50, 57),
    }
    return {
        domain: {k: v for k, v in body.items() if start <= int(k[1:]) <= end}
        for domain, (start, end) in domains.items()
    }


def validate_form_data(body: Dict[str, str]):
    # Validate required fields
    required_fields = [f"q{i}" for i in range(1, 58)]
    missing_fields = [field for field in required_fields if field not in body]
    if missing_fields:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Missing required fields",
                "missing_fields": missing_fields,
                "message": "Please provide answers for all questions (q1-q57)",
            },
        )

    # Validate input values
    invalid_fields = []
    for field, value in body.items():
        question_num = int(field[1:])
        if not isinstance(value, str) or not value.startswith(f"{question_num}"):
            invalid_fields.append(field)

    if invalid_fields:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Invalid answer format",
                "invalid_fields": invalid_fields,
                "message": 'Answers should be in format: q1="1a", q11="11b", etc.',
            },
        )


@sri_calculator_app.get("/health")
async def health_check():
    return {"status": "200 - [Healthy]", "service": "SRI Calculator API"}


@sri_calculator_app.post("/calculate")
async def calculate_sri(request: SRIRequest):
    try:
        validate_form_data(request.body)
        domain_data = split_form_data(request.body)

        # Calculate scores for each domain
        scores = {
            "Heating": calculate_sri_score_heating(
                sri_score_heating(domain_data["heating"])
            ),
            "Cooling": calculate_sri_score_cooling(
                sri_score_cooling(domain_data["cooling"])
            ),
            "DWH": calculate_sri_score_DWH(sri_score_DWH(domain_data["dwh"])),
            "Lighting": calculate_sri_score_lighting(
                sri_score_lighting(domain_data["lighting"])
            ),
            "Ventilation": calculate_sri_score_ventilation(
                sri_score_ventilation(domain_data["ventilation"])
            ),
            "Envelope": calculate_sri_score_envelope(
                sri_score_envelope(domain_data["envelope"])
            ),
            "EV_Charging": calculate_sri_score_ev_charging(
                sri_score_ev_charging(domain_data["ev_charging"])
            ),
            "Electricity": calculate_sri_score_electricity(
                sri_score_electricity(domain_data["electricity"])
            ),
            "Monitoring": calculate_sri_score_monitoring(
                sri_score_monitoring(domain_data["monitoring"])
            ),
        }

        final_scores = calculate_final_sri_score(scores)

        response_body = {
            "status": 200,
            "message": "Success",
            "scores": {
                "Total_SRI_Score": final_scores["final_score"],
                "Domain_Weighted_Scores": final_scores["impact_totals"],
                **scores,
            },
        }
        # print(response_body)

        return {
            "statusCode": 200,
            "body": json.dumps(response_body),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
        }

        # return {
        #     "status": 200,
        #     "message": "Success",
        #     "scores": {
        #         "Total_SRI_Score": final_scores["final_score"],
        #         "Domain_Weighted_Scores": final_scores["impact_totals"],
        #         **scores,
        #     },
        # }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(sri_calculator_app, host="0.0.0.0", port=8000)
