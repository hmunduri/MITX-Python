def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    increasing_index = decreasing_index = 0
    max_increasing_index = max_decreasing_index = 0
    max_increasing = [L[0]]
    max_decreasing = [L[0]]
    increasing = max_increasing[:]
    decreasing = max_decreasing[:]

    for i in range(len(L) - 1):
        if L[i] <= L[i + 1]:
            increasing.append(L[i + 1])
            if len(increasing) > len(max_increasing):
                max_increasing = increasing[:]
                max_increasing_index = increasing_index
        else:
            increasing = [L[i + 1]]
            increasing_index = i + 1

        if L[i] >= L[i + 1]:
            decreasing.append(L[i + 1])
            if len(decreasing) > len(max_decreasing):
                max_decreasing = decreasing[:]
                max_decreasing_index = decreasing_index
        else:
            decreasing = [L[i + 1]]
            decreasing_index = i + 1

    if len(max_increasing) > len(max_decreasing):
        return sum(max_increasing)
    elif len(max_increasing) < len(max_decreasing):
        return sum(max_decreasing)
    else:
        return sum(max_increasing
                   if max_increasing_index < max_decreasing_index else
                   max_decreasing)
