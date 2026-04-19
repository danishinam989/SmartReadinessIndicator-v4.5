def sri_score_monitoring(answers):
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
    
    # Question 50 - Run time management of HVAC systems
    if answers['q50'] == '50a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q50'] == '50b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 1
    elif answers['q50'] == '50c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 2
        total_scores["Health, Well Being and Accessibility"] += 1
    elif answers['q50'] == '50d':
        total_scores["Energy Efficiency"] += 3
        total_scores["Energy Flexibility and Storage"] += 2
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 3
        total_scores["Health, Well Being and Accessibility"] += 1
    
    # Question 51 - Detecting faults of technical building systems
    if answers['q51'] == '51a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q51'] == '51b':
        total_scores["Convenience"] += 1
        total_scores["Health, Well Being and Accessibility"] += 1
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 1
    elif answers['q51'] == '51c':
        total_scores["Convenience"] += 2
        total_scores["Health, Well Being and Accessibility"] += 2
        total_scores["Maintenance and Fault Prediction"] += 2
        total_scores["Information to Occupants"] += 2
    elif answers['q51'] == '51d':
        total_scores["Convenience"] += 3
        total_scores["Health, Well Being and Accessibility"] += 3
        total_scores["Maintenance and Fault Prediction"] += 3
        total_scores["Information to Occupants"] += 3

    # Question 52 - Occupancy detection: connected services
    if answers['q52'] == '52a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q52'] == '52b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 1
        total_scores["Maintenance and Fault Prediction"] += 1
    elif answers['q52'] == '52c':
        total_scores["Energy Efficiency"] += 1
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 1
        total_scores["Maintenance and Fault Prediction"] += 2

    # Question 53 - Central reporting of TBS performance
    if answers['q53'] == '53a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q53'] == '53b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Convenience"] += 1
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 1
    elif answers['q53'] == '53c':
        total_scores["Energy Efficiency"] += 1
        total_scores["Convenience"] += 2
        total_scores["Maintenance and Fault Prediction"] += 2
        total_scores["Information to Occupants"] += 2
    elif answers['q53'] == '53d':
        total_scores["Energy Efficiency"] += 1
        total_scores["Convenience"] += 3
        total_scores["Maintenance and Fault Prediction"] += 3
        total_scores["Information to Occupants"] += 3

    # Question 54 - Smart Grid Integration
    if answers['q54'] == '54a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q54'] == '54b':
        total_scores["Energy Flexibility and Storage"] += 2
    elif answers['q54'] == '54c':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 3
        total_scores["Convenience"] += 1

    # Question 55 - DSM performance reporting
    if answers['q55'] == '55a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q55'] == '55b':
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 2
    elif answers['q55'] == '55c':
        total_scores["Energy Flexibility and Storage"] += 2
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 3

    # Question 56 - Override of DSM control
    if answers['q56'] == '56a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q56'] == '56b':
        total_scores["Energy Flexibility and Storage"] += 3
        total_scores["Comfort"] += -2
        total_scores["Maintenance and Fault Prediction"] += -1
        total_scores["Information to Occupants"] += -2
    elif answers['q56'] == '56c':
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Convenience"] += 1
    elif answers['q56'] == '56d':
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Convenience"] += 2
        total_scores["Maintenance and Fault Prediction"] += 1
    elif answers['q56'] == '56e':
        total_scores["Energy Flexibility and Storage"] += 2
        total_scores["Convenience"] += 3
        total_scores["Maintenance and Fault Prediction"] += 1

    # Question 57 - Single platform TBS coordination
    if answers['q57'] == '57a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q57'] == '57b':
        total_scores["Convenience"] += 1
        total_scores["Maintenance and Fault Prediction"] += 1
    elif answers['q57'] == '57c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Convenience"] += 2
        total_scores["Maintenance and Fault Prediction"] += 1
    elif answers['q57'] == '57d':
        total_scores["Energy Efficiency"] += 2
        total_scores["Convenience"] += 3
        total_scores["Maintenance and Fault Prediction"] += 1
    
    return total_scores

def calculate_sri_score_monitoring(scores):
    category_weights = {
        "Energy Efficiency": (21, 20),
        "Energy Flexibility and Storage": (11, 20),
        "Comfort": (12, 20),
        "Convenience": (10, 20),
        "Health, Well Being and Accessibility": (5, 20),
        "Maintenance and Fault Prediction": (5, 20),
        "Information to Occupants": (4, 20),
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

    sri_score_monitoring = {
        'adjusted_sri_scores_monitoring': adjusted_scores,
        'total_sri_score_monitoring': round(total_score, 2)
    }
    return sri_score_monitoring
