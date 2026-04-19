def sri_score_ev_charging(answers):
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
    
    # Question 40 - EV Charging Capacity
    if answers['q40'] == '40a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q40'] == '40b':
        total_scores["Convenience"] += 1
    elif answers['q40'] == '40c':
        total_scores["Convenience"] += 2
    elif answers['q40'] == '40d':
        total_scores["Convenience"] += 3
    elif answers['q40'] == '40e':
        total_scores["Convenience"] += 3
    
    # Question 41 - EV Charging Grid Balancing
    if answers['q41'] == '41a':
        total_scores["Energy Flexibility and Storage"] += -2
    elif answers['q41'] == '41b':
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Convenience"] += 2
    elif answers['q41'] == '41c':
        total_scores["Energy Flexibility and Storage"] += 3
        total_scores["Convenience"] += 2

    # Question 42 - EV charging information and connectivity
    if answers['q42'] == '42a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q42'] == '42b':
        total_scores["Convenience"] += 1
    elif answers['q42'] == '42c':
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Convenience"] += 1
        total_scores["Information to Occupants"] += 3
    
    return total_scores

def calculate_sri_score_ev_charging(scores):
    category_weights = {
        "Energy Efficiency": (0, 0),
        "Energy Flexibility and Storage": (3, 5),
        "Comfort": (0, 0),
        "Convenience": (5, 10),
        "Health, Well Being and Accessibility": (0, 0),
        "Maintenance and Fault Prediction": (0, 0),
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

    sri_score_ev_charging = {
        'adjusted_sri_scores_ev_charging': adjusted_scores,
        'total_sri_score_ev_charging': round(total_score, 2)
    }
    return sri_score_ev_charging