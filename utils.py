import copy as cp

"""
The methods in this file are global methods of general applicability, 
not particularly associated with any class.
"""


def print_list(list1):
    """
    This method prints a detailed inventory of the contents of list `list1`

    Parameters
    ----------
    list1: list

    Returns
    -------
    None

    """
    for i, x in enumerate(list1):
        print(str(i + 1) + ", ", x)


def print_dict(dict1):
    """
    This method prints a detailed inventory of the contents of dictionary
    `dict1`.

    Parameters
    ----------
    dict1: dict

    Returns
    -------
    None

    """
    for i, key in enumerate(dict1):
        print(i + 1, ",", key, ":")
        print_list(dict1[key])
