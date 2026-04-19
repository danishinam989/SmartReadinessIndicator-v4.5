def sri_score_electricity(answers):
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
    
    # Question 43 - Reporting information regarding local electricity generation
    if answers['q43'] == '43a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q43'] == '43b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 1
    elif answers['q43'] == '43c':
        total_scores["Energy Efficiency"] += 1
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 2
    elif answers['q43'] == '43d':
        total_scores["Energy Efficiency"] += 1
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 3
    elif answers['q43'] == '43e':
        total_scores["Energy Efficiency"] += 1
        total_scores["Convenience"] += 1
        total_scores["Maintenance and Fault Prediction"] += 2
        total_scores["Information to Occupants"] += 3
    
    # Question 44 - Storage of (locally generated) electricity
    if answers['q44'] == '44a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q44'] == '44b':
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Convenience"] += 2
    elif answers['q44'] == '44c':
        total_scores["Energy Flexibility and Storage"] += 2
        total_scores["Convenience"] += 2
    elif answers['q44'] == '44d':
        total_scores["Energy Flexibility and Storage"] += 2
        total_scores["Convenience"] += 2
    elif answers['q44'] == '44e':
        total_scores["Energy Flexibility and Storage"] += 3
        total_scores["Convenience"] += 2

    # Question 45 - Optimizing self consumption of locally generated electricity
    if answers['q45'] == '45a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q45'] == '45b':
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Convenience"] += 1
    elif answers['q45'] == '45c':
        total_scores["Energy Flexibility and Storage"] += 2
        total_scores["Convenience"] += 2
    elif answers['q45'] == '45d':
        total_scores["Energy Flexibility and Storage"] += 3
        total_scores["Convenience"] += 2

    # Question 46 - Control of combined heat and power plant (CHP)
    if answers['q46'] == '46a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q46'] == '46b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Convenience"] += 1
    elif answers['q46'] == '46c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 2
        total_scores["Convenience"] += 1

    # Question 47 - Support of microgrid operation modes
    if answers['q47'] == '47a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q47'] == '47b':
        total_scores["Energy Flexibility and Storage"] += 2
        total_scores["Convenience"] += 2
    elif answers['q47'] == '47c':
        total_scores["Energy Flexibility and Storage"] += 2
        total_scores["Convenience"] += 2
    elif answers['q47'] == '47d':
        total_scores["Energy Flexibility and Storage"] += 3
        total_scores["Convenience"] += 3

    # Question 48 - Reporting information regarding energy storage
    if answers['q48'] == '48a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q48'] == '48b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 1
    elif answers['q48'] == '48c':
        total_scores["Energy Efficiency"] += 1
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 2
    elif answers['q48'] == '48d':
        total_scores["Energy Efficiency"] += 1
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 3
    elif answers['q48'] == '48e':
        total_scores["Energy Efficiency"] += 1
        total_scores["Convenience"] += 1
        total_scores["Maintenance and Fault Prediction"] += 2
        total_scores["Information to Occupants"] += 3

    # Question 49 - Reporting information regarding electricity consumption
    if answers['q49'] == '49a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q49'] == '49b':
        total_scores["Information to Occupants"] += 1
    elif answers['q49'] == '49c':
        total_scores["Energy Efficiency"] += 1
        total_scores["Information to Occupants"] += 2
    elif answers['q49'] == '49d':
        total_scores["Energy Efficiency"] += 2
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 3
    elif answers['q49'] == '49e':
        total_scores["Energy Efficiency"] += 3
        total_scores["Convenience"] += 1
        total_scores["Maintenance and Fault Prediction"] += 2
        total_scores["Information to Occupants"] += 3
    
    return total_scores

def calculate_sri_score_electricity(scores):
    category_weights = {
        "Energy Efficiency": (21, 11.09),
        "Energy Flexibility and Storage": (11, 14.93),
        "Comfort": (12, 0),
        "Convenience": (10, 10),
        "Health, Well Being and Accessibility": (5, 0),
        "Maintenance and Fault Prediction": (5, 11.31),
        "Information to Occupants": (4, 11.43),
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

    sri_score_electricity = {
        'adjusted_sri_scores_electricity': adjusted_scores,
        'total_sri_score_electricity': round(total_score, 2)
    }
    return sri_score_electricity

