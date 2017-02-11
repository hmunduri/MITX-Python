def f(a, b):
    return a + b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersection = set(d1) & set(d2)
    sym_difference = set(d1) ^ set(d2)


    return ({key: f(d1[key], d2[key]) for key in intersection},
            {key: d1.get(key) if d1.get(key) is not None else d2.get(key)
             for key in sym_difference})

