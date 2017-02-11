def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    dot_product = 0
    for a, b in zip(listA, listB):
        dot_product += a * b

    return dot_product
