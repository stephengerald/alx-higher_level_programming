#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None or len(a_dictionary) == 0:
        return None

    current_high_score = 0
    high_score_holder = None
    
    for key in a_dictionary:
        if a_dictionary[key] > current_high_score:
            current_high_score = a_dictionary[key]
            high_score_holder =  key

    return high_score_holder
