def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    if not aList:
        return []

    if type(aList[0]) is list:
        return flatten(aList[0]) + flatten(aList[1:])

    return [aList[0]] + flatten(aList[1:])
