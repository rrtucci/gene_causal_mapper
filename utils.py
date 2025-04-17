import copy as cp

def merge_two_dicts(dict1, dict2):
    for name in dict1.keys():
        if name in dict2.keys():
            assert False, f"key {name} appears more than once"
    x = cp.deepcopy(dict1)
    x.update(dict2)
    return x

def print_list(list1):
    for i, x in enumerate(list1):
        print(str(i+1) + ", ", x)

def print_dict(dict1):
    for i, key in enumerate(dict1):
        print(i+1, ",", key, ":")
        print_list(dict1[key])

