import random

def weighted_choice(item_dict):
    '''Pick a random item from a list
    keys are the items and the values are numbers for the keys
    
    Ex.
    {'a': 2, 'b': 3}
    '''
    return random.choice([k for k in item_dict for dummy in range(item_dict[k])])