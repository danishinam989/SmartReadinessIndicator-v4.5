def calculate_final_sri_score(domain_scores):
    """
    Calculate final SRI score from pre-weighted domain scores and sum of impact categories
    
    Args:
        domain_scores (dict): Dictionary containing pre-weighted domain scores
        
    Returns:
        dict: Contains final weighted SRI score and total impact scores
            {
                'final_score': float,  # Weighted final SRI score
                'impact_totals': dict,  # Sum of each impact category across domains
                'total_impact_score': float  # Simple sum of all impact totals
            }
    """
    # Impact criteria weights
    impact_weights = {
        "Energy Efficiency": 0.1667,
        "Energy Flexibility and Storage": 0.3333,
        "Comfort": 0.0833,
        "Convenience": 0.0833,
        "Health, Well Being and Accessibility": 0.0833,
        "Maintenance and Fault Prediction": 0.1667,
        "Information to Occupants": 0.0833
    }
    
    # Sum pre-weighted scores across domains for each impact
    impact_totals = {impact: 0 for impact in impact_weights}
    
    for domain, scores in domain_scores.items():
        if domain != "Total_SRI_Score":
            adjusted_scores_key = f"adjusted_sri_scores_{domain.lower()}"
            if adjusted_scores_key in scores:
                for impact, score in scores[adjusted_scores_key].items():
                    impact_totals[impact] += score 

    # Calculate final weighted score
    final_score = sum(
        score * impact_weights[impact] 
        for impact, score in impact_totals.items()
    )
    
    return {
        'final_score': round(final_score, 2),
        'impact_totals': {k: round(v, 2) for k, v in impact_totals.items()},

    }