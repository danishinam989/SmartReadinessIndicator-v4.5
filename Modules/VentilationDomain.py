def sri_score_ventilation(answers):
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
    
    # Question 1 - Supply air flow control at the room level
    if answers['q31'] == '1a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q31'] == '1b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 1
    elif answers['q31'] == '1c':
        total_scores["Energy Efficiency"] += 1
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 2
    elif answers['q31'] == '1d':
        total_scores["Energy Efficiency"] += 2
        total_scores["Comfort"] += 3
        total_scores["Convenience"] += 3
        total_scores["Health, Well Being and Accessibility"] += 3
    elif answers['q31'] == '1e':
        total_scores["Energy Efficiency"] += 3
        total_scores["Comfort"] += 3
        total_scores["Convenience"] += 3
        total_scores["Health, Well Being and Accessibility"] += 3

    # Question 2 - Airflow or pressure control at the air handler level
    if answers['q32'] == '32a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q32'] == '32b':
        total_scores["Energy Efficiency"] += 1
    elif answers['q32'] == '32c':
        total_scores["Energy Efficiency"] += 2
    elif answers['q32'] == '32d':
        total_scores["Energy Efficiency"] += 3
    elif answers['q32'] == '32e':
        total_scores["Energy Efficiency"] += 3

    # Question 3 - Heat recovery control: prevention of overheating
    if answers['q33'] == '33a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q33'] == '33b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 1
    elif answers['q33'] == '33c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 2

    # Question 4 - Supply air temperature control at the air handling unit level
    if answers['q34'] == '34a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q34'] == '34b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 1
    elif answers['q34'] == '34c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 1
    elif answers['q34'] == '34d':
        total_scores["Energy Efficiency"] += 3
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 1

    # Question 5 - Free cooling with mechanical ventilation system
    if answers['q35'] == '35a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q35'] == '35b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Comfort"] += 3
        total_scores["Convenience"] += 2
        total_scores["Health, Well Being and Accessibility"] += 1
    elif answers['q35'] == '35c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Comfort"] += 3
        total_scores["Convenience"] += 2
        total_scores["Health, Well Being and Accessibility"] += 1
    elif answers['q35'] == '35d':
        total_scores["Energy Efficiency"] += 3
        total_scores["Comfort"] += 3
        total_scores["Convenience"] += 2
        total_scores["Health, Well Being and Accessibility"] += 1

    # Question 6 - Report information regarding Indoor Air Quality
    if answers['q36'] == '36a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q36'] == '36b':
        total_scores["Health, Well Being and Accessibility"] += 2
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 1
    elif answers['q36'] == '36c':
        total_scores["Health, Well Being and Accessibility"] += 3
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 2
    elif answers['q36'] == '36d':
        total_scores["Health, Well Being and Accessibility"] += 3
        total_scores["Maintenance and Fault Prediction"] += 2
        total_scores["Information to Occupants"] += 3
    
    return total_scores

def calculate_sri_score_ventilation(scores):
    category_weights = {
        "Energy Efficiency": (15, 17.82),
        "Energy Flexibility and Storage": (1, 0),
        "Comfort": (14, 16),
        "Convenience": (11, 10),
        "Health, Well Being and Accessibility": (10, 16),
        "Maintenance and Fault Prediction": (4, 18.17),
        "Information to Occupants": (6, 11.43),
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

    sri_score_ventilation = {
        'adjusted_sri_scores_ventilation': adjusted_scores,
        'total_sri_score_ventilation': round(total_score, 2)
    }
    return sri_score_ventilation