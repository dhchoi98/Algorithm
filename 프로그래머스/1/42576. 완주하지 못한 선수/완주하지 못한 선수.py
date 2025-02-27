from collections import Counter

def solution(participant, completion):
    # ww
    participant.sort()
    completion.sort()
    
    part = Counter(participant)
    comp = Counter(completion)
    sets = set(participant)
    
    for key, value in part.items():
        if comp[key] != value:
            return key
        
        