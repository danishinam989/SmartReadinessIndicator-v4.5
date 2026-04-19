def sri_score_lighting(answers):
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
    
    # Question 1 - Occupancy control for indoor lighting
    if answers['q26'] == '26a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q26'] == '26b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Convenience"] += 1
    elif answers['q26'] == '26c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Convenience"] += 2
    elif answers['q26'] == '26d':
        total_scores["Energy Efficiency"] += 3
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 2

    # Question 2 - Control artificial lighting power based on daylight levels
    if answers['q27'] == '27a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q27'] == '27b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Comfort"] += 1
    elif answers['q27'] == '27c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 1
    elif answers['q27'] == '27d':
        total_scores["Energy Efficiency"] += 3
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 2
    elif answers['q27'] == '27e':
        total_scores["Energy Efficiency"] += 3
        total_scores["Comfort"] += 3
        total_scores["Convenience"] += 3
        total_scores["Health, Well Being and Accessibility"] += 3

    # Question 3 - Lighting zone control
    if answers['q28'] == '28a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q28'] == '28b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Convenience"] += 1
    elif answers['q28'] == '28c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Convenience"] += 2
        total_scores["Comfort"] += 1

    # Question 4 - Blind/shutter control
    if answers['q29'] == '29a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q29'] == '29b':
        total_scores["Convenience"] += 1
    elif answers['q29'] == '29c':
        total_scores["Energy Efficiency"] += 1
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 2
    elif answers['q29'] == '29d':
        total_scores["Energy Efficiency"] += 2
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 3
        total_scores["Energy Flexibility and Storage"] += 1

    # Question 5 - Display/scene control
    if answers['q30'] == '30a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q30'] == '30b':
        total_scores["Convenience"] += 1
        total_scores["Comfort"] += 1
    elif answers['q30'] == '30c':
        total_scores["Energy Efficiency"] += 1
        total_scores["Convenience"] += 2
        total_scores["Comfort"] += 2
        total_scores["Health, Well Being and Accessibility"] += 1
    
    return total_scores

def calculate_sri_score_lighting(scores):
    category_weights = {
        "Energy Efficiency": (11, 1.46),
        "Energy Flexibility and Storage": (1, 0),
        "Comfort": (10, 16),
        "Convenience": (10, 10),
        "Health, Well Being and Accessibility": (4, 16),
        "Maintenance and Fault Prediction": (0, 0),
        "Information to Occupants": (0, 0),
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

    sri_score_lighting = {
        'adjusted_sri_scores_lighting': adjusted_scores,
        'total_sri_score_lighting': round(total_score, 2)
    }
    return sri_score_lighting