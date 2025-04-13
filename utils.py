import copy as cp

def merge_two_dicts(dict1, dict2):
    for name in dict1.keys():
        if name in dict2.keys():
            assert False, f"key {name} appears more than once"
    return cp.deepcopy(dict1).update(dict2)