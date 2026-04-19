def sri_score_envelope(answers):
    # Initialize the total scores for each category
    total_scores = {
        "Energy Efficiency": 0,
        "Energy Flexibility and Storage": 0,
        "Comfort": 0,
        "Convenience": 0,
        "Health, Well Being and Accessibility": 0,
        "Maintenance and Fault Prediction": 0,
        "Information to Occupants": 0
    }
    
    # Question 37 - Window solar shading control
    if answers['q37'] == '37a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q37'] == '37b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 1
    elif answers['q37'] == '37c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 2
        total_scores["Health, Well Being and Accessibility"] += 1
    elif answers['q37'] == '37d':
        total_scores["Energy Efficiency"] += 3
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 3
        total_scores["Health, Well Being and Accessibility"] += 2
    elif answers['q37'] == '37e':
        total_scores["Energy Efficiency"] += 3
        total_scores["Comfort"] += 3
        total_scores["Convenience"] += 3
        total_scores["Health, Well Being and Accessibility"] += 3
    
    # Question 38 - Window open/closed control, combined with HVAC system
    if answers['q38'] == '38a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q38'] == '38b':
        total_scores["Energy Efficiency"] += 2
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 1
    elif answers['q38'] == '38c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 1
        total_scores["Health, Well Being and Accessibility"] += 1
    elif answers['q38'] == '38d':
        total_scores["Energy Efficiency"] += 2
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 2
        total_scores["Health, Well Being and Accessibility"] += 1

    # Question 39 - Reporting information regarding performance of dynamic building envelope systems
    if answers['q39'] == '39a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q39'] == '39b':
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 1
    elif answers['q39'] == '39c':
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 2
    elif answers['q39'] == '39d':
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 3
    elif answers['q39'] == '39e':
        total_scores["Convenience"] += 1
        total_scores["Maintenance and Fault Prediction"] += 2
        total_scores["Information to Occupants"] += 3
    
    return total_scores

def calculate_sri_score_envelope(scores):
    category_weights = {
        "Energy Efficiency": (5, 5),
        "Energy Flexibility and Storage": (0, 0),
        "Comfort": (5, 16),
        "Convenience": (6, 10),
        "Health, Well Being and Accessibility": (4, 16),
        "Maintenance and Fault Prediction": (2, 5),
        "Information to Occupants": (3, 11.43),
    }

    total_score = 0
    adjusted_scores = {}

    for category, score in scores.items():
        if category in category_weights:
            max_score, weight = category_weights[category]
            percentage = round((score / max_score) * 100, 2) if max_score > 0 else 0
            adjusted_percentage = round(percentage * (weight / 100), 2)
            adjusted_scores[category] = adjusted_percentage
            total_score += adjusted_percentage
        else:
            print(f"Error: Unknown category '{category}'")

    sri_score_envelope = {
        'adjusted_sri_scores_envelope': adjusted_scores,
        'total_sri_score_envelope': round(total_score, 2)
    }
    return sri_score_envelope