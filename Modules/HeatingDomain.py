#HeatingDomain.py

def sri_score_heating(answers):
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
    
    # Question 1 - Heat Emission Control
    if answers['q1'] == '1a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q1'] == '1b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 1
        total_scores["Health, Well Being and Accessibility"] += 1
    elif answers['q1'] == '1c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 2
        total_scores["Health, Well Being and Accessibility"] += 2
    elif answers['q1'] == '1d':
        total_scores["Energy Efficiency"] += 2
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 3
        total_scores["Health, Well Being and Accessibility"] += 2
        total_scores["Maintenance and Fault Prediction"] += 1
    elif answers['q1'] == '1e':
        total_scores["Energy Efficiency"] += 3
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 3
        total_scores["Health, Well Being and Accessibility"] += 2
        total_scores["Maintenance and Fault Prediction"] += 1
    
    # Question 2 - Emission Control for TABS (Heating mode)
    if answers['q2'] == '2a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q2'] == '2b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 1
        total_scores["Health, Well Being and Accessibility"] += 1
    elif answers['q2'] == '2c':
        total_scores["Energy Efficiency"] += 1
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 2
        total_scores["Health, Well Being and Accessibility"] += 2
    elif answers['q2'] == '2d':
        total_scores["Energy Efficiency"] += 2
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 3
        total_scores["Health, Well Being and Accessibility"] += 2
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 1

    # Question 3 - Control of distribution fluid temperature (supply and return air flow or water  flow) - Similar function can be applied to the control of direct electric heating networks
    if answers['q3'] == '3a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q3'] == '3b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 1
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    elif answers['q3'] == '3c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 1
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    
    # Question 4 - Control of distribution pumps in network
    if answers['q4'] == '4a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q4'] == '4b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    elif answers['q4'] == '4c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0

    elif answers['q4'] == '4d':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0

    elif answers['q4'] == '4e':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0

    # Question 5 - Thermal Energy Strage (TES) for building heating (excluding TABS)
    if answers['q5'] == '5a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q5'] == '5b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    elif answers['q5'] == '5c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0

    elif answers['q5'] == '5d':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 2
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0


    # Question 6 - Heat generator control (all except heat pump)
    if answers['q6'] == '6a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q6'] == '6b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    elif answers['q6'] == '6c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0


    # Question 7 - Heat generator control (for heat pumps)
    if answers['q7'] == '7a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q7'] == '7b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    elif answers['q7'] == '7c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0

    elif answers['q7'] == '7d':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 3
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0

  # Question 8 - Sequencing in case of different heat generators 
    if answers['q8'] == '8a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q8'] == '8b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    elif answers['q8'] == '8c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0

    elif answers['q8'] == '8d':
        total_scores["Energy Efficiency"] += 3
        total_scores["Energy Flexibility and Storage"] += 2
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0

    elif answers['q8'] == '8e':
        total_scores["Energy Efficiency"] += 3
        total_scores["Energy Flexibility and Storage"] += 3
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
        
# Question 9 - Report Information Regarding Human System Performance
    if answers['q9'] == '9a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q9'] == '9b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 1
    elif answers['q9'] == '9c':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 2

    elif answers['q9'] == '9d':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 3

    elif answers['q9'] == '9e':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 3
        total_scores["Information to Occupants"] += 3

# Question 10 - Flexible and Grid Interaction 
    if answers['q10'] == '10a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q10'] == '10b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 1
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    elif answers['q10'] == '10c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 2
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0

    elif answers['q10'] == '10d':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 3
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 3
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0

    elif answers['q10'] == '10e':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 3
        total_scores["Comfort"] += 3
        total_scores["Convenience"] += 3
        total_scores["Health, Well Being and Accessibility"] += 1
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    
    return total_scores

def calculate_sri_score_heating(scores):
    category_weights = {
        "Energy Efficiency": (21, 33.97),
        "Energy Flexibility and Storage": (11, 45.72),
        "Comfort": (12, 16),
        "Convenience": (10, 10),
        "Health, Well Being and Accessibility": (5, 16),
        "Maintenance and Fault Prediction": (5, 34.64),
        "Information to Occupants": (4, 11.43),
    }

    total_score = 0
    adjusted_scores = {}

    for category, score in scores.items():
        if category in category_weights:
            max_score, weight = category_weights[category]
            percentage = round((score / max_score) * 100, 2)
            adjusted_percentage = round(percentage * (weight / 100), 2)
            adjusted_scores[category] = adjusted_percentage
            total_score += adjusted_percentage
        else:
            print(f"Error: Unknown category '{category}'")

        sri_score_heating = {
            'adjusted_sri_scores_heating': adjusted_scores,
            'total_sri_score_heating': round(total_score, 2)
        }
    return sri_score_heating