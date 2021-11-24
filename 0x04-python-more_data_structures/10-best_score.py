#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    highest_scorer = list(a_dictionary.keys())[0]
    highest_score = a_dictionary[highest_scorer]
    for key, value in a_dictionary.items():
        if value > highest_score:
            highest_score = value
            highest_scorer = key
    return (highest_scorer)
