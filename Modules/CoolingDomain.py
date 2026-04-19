def sri_score_cooling(answers):
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
    
    # Question 11 - Cooling Emission Control 
    if answers['q11'] == '11a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q11'] == '11b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 1
        total_scores["Health, Well Being and Accessibility"] += 1
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    elif answers['q11'] == '11c':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 2
        total_scores["Health, Well Being and Accessibility"] += 2
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    elif answers['q11'] == '11d':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 3
        total_scores["Health, Well Being and Accessibility"] += 2
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 0
    elif answers['q11'] == '11e':
        total_scores["Energy Efficiency"] += 3
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 3
        total_scores["Health, Well Being and Accessibility"] += 2
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 0
    
    # Question 12 - Emission Control for TABS (Cooling mode)
    if answers['q12'] == '12a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q12'] == '12b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 1
        total_scores["Health, Well Being and Accessibility"] += 1
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    elif answers['q12'] == '12c':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 1
        total_scores["Health, Well Being and Accessibility"] += 2
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    elif answers['q12'] == '12d':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 3
        total_scores["Health, Well Being and Accessibility"] += 2
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 1

    # Question 13 - Control of distribution network chilled water temperature (supply or return)
    if answers['q13'] == '13a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q13'] == '13b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 1
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    elif answers['q13'] == '13c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 1
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    
    # Question 14 - Control of distribution pumps in networks
    if answers['q14'] == '14a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q14'] == '14b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    elif answers['q14'] == '14c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0

    elif answers['q14'] == '14d':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0

    elif answers['q14'] == '14e':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0

    # Question 15 - Interlock: avoiding simultaneous heating and cooling in the same room
    if answers['q15'] == '15a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q15'] == '15b':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    elif answers['q15'] == '15c':
        total_scores["Energy Efficiency"] += 3
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0

    # Question 16 - Control of Thermal Energy Storage (TES) Operation
    if answers['q16'] == '16a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q16'] == '16b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    elif answers['q16'] == '16c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    elif answers['q16'] == '16d':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 2
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0

    # Question 17 - Generator Control for Cooling
    if answers['q17'] == '17a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q17'] == '17b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    elif answers['q17'] == '17c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0

    elif answers['q17'] == '17d':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 3
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0

  # Question 18 - Sequencing in case of different cooling generators 
    if answers['q18'] == '18a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q18'] == '18b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    elif answers['q18'] == '18c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0

    elif answers['q18'] == '18d':
        total_scores["Energy Efficiency"] += 3
        total_scores["Energy Flexibility and Storage"] += 2
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0

    elif answers['q18'] == '18e':
        total_scores["Energy Efficiency"] += 3
        total_scores["Energy Flexibility and Storage"] += 3
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
        
# Question 19 - Report Information Regarding cooling System Performance
    if answers['q19'] == '19a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q19'] == '19b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 1
    elif answers['q19'] == '19c':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 2

    elif answers['q19'] == '19d':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 1
        total_scores["Information to Occupants"] += 3

    elif answers['q19'] == '19e':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 0
        total_scores["Convenience"] += 0
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 3
        total_scores["Information to Occupants"] += 3

# Question 20 - Flexible and Grid Interaction 
    if answers['q20'] == '20a':
        total_scores = {key: value for key, value in total_scores.items()}
    elif answers['q20'] == '20b':
        total_scores["Energy Efficiency"] += 1
        total_scores["Energy Flexibility and Storage"] += 0
        total_scores["Comfort"] += 1
        total_scores["Convenience"] += 1
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
    elif answers['q20'] == '20c':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 1
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 2
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0

    elif answers['q20'] == '20d':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 3
        total_scores["Comfort"] += 2
        total_scores["Convenience"] += 3
        total_scores["Health, Well Being and Accessibility"] += 0
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0

    elif answers['q20'] == '20e':
        total_scores["Energy Efficiency"] += 2
        total_scores["Energy Flexibility and Storage"] += 3
        total_scores["Comfort"] += 3
        total_scores["Convenience"] += 3
        total_scores["Health, Well Being and Accessibility"] += 1
        total_scores["Maintenance and Fault Prediction"] += 0
        total_scores["Information to Occupants"] += 0
        
    return total_scores

def calculate_sri_score_cooling(scores):
    category_weights = {
        "Energy Efficiency": (22, 3.04),
        "Energy Flexibility and Storage": (11, 4.09),
        "Comfort": (10, 16),
        "Convenience": (10, 10),
        "Health, Well Being and Accessibility": (5, 16),
        "Maintenance and Fault Prediction": (5, 3.10),
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

    sri_score_cooling = {
        'adjusted_sri_scores_cooling': adjusted_scores,
        'total_sri_score_cooling': round(total_score, 2)
    }
    return sri_score_cooling