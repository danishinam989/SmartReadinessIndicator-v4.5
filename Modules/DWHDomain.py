def sri_score_DWH(answers):
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
    
    # Question 1 - Control of dwh storage charging (with direct electric heating or integrated electric heat pump)
    if answers['q21'] == '21a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q21'] == '21b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Convenience"] += 1
    elif answers['q21'] == '21c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 2
        total_scores["Convenience"] += 2
    elif answers['q21'] == '21d':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 3
        total_scores["Convenience"] += 2

    # Question 2 - Control of dwh storage charging (using hot water generation)
    if answers['q22'] == '22a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q22'] == '22b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Convenience"] += 1
        total_scores["Health, Well Being and Accessibility"] += 1
    elif answers['q22'] == '22c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 2
        total_scores["Convenience"] += 2
    elif answers['q22'] == '22d':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 3
        total_scores["Convenience"] += 2

    # Question 3 - Control of dwh storage charging (with solar collector and supplementary heat generation)
    if answers['q23'] == '23a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q23'] == '23b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Convenience"] += 1
    elif answers['q23'] == '23c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Convenience"] += 2
    elif answers['q23'] == '23d':
        total_scores["Energy Efficiency"] += 3
        total_scores["Energy Flexibility and Storage"] += 2
        total_scores["Convenience"] += 2

    # Question 4 - Sequencing in case of different dwh generators
    if answers['q24'] == '24a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q24'] == '24b':
        total_scores["Energy Efficiency"] += 1
    elif answers['q24'] == '24c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 1
    elif answers['q24'] == '24d':
        total_scores["Energy Efficiency"] += 3
        total_scores["Energy Flexibility and Storage"] += 2
    elif answers['q24'] == '24e':
        total_scores["Energy Efficiency"] += 3
        total_scores["Energy Flexibility and Storage"] += 3

    # Question 5 - Report information regarding domestic hot water performance
    if answers['q25'] == '25a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q25'] == '25b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 1
    elif answers['q25'] == '25c':
        total_scores["Energy Efficiency"] += 1
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 2
    elif answers['q25'] == '25d':
        total_scores["Energy Efficiency"] += 1
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 3
    elif answers['q25'] == '25e':
        total_scores["Energy Efficiency"] += 1
        total_scores["Convenience"] += 1
        total_scores["Maintenance and Fault Prediction"] += 2
        total_scores["Information to Occupants"] += 3
    
    return total_scores

def calculate_sri_score_DWH(scores):
    category_weights = {
        "Energy Efficiency": (11, 7.62),
        "Energy Flexibility and Storage": (11, 10.26),
        "Comfort": (0, 0),
        "Convenience": (7, 10),
        "Health, Well Being and Accessibility": (1, 0),
        "Maintenance and Fault Prediction": (2, 7.77),
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

    sri_score_dwh = {
        'adjusted_sri_scores_dwh': adjusted_scores,
        'total_sri_score_dwh': round(total_score, 2)
    }
    return sri_score_dwh