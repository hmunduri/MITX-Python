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
    increasing_indices = [0]
    decreasing_indices = [0]
    max_increasing_indexes = increasing_indices[:]
    max_decreasing_indexes = decreasing_indices[:]
    max_increasing = [L[0]]
    max_decreasing = [L[0]]
    increasing = max_increasing[:]
    decreasing = max_decreasing[:]

    for i, e in enumerate(L[1:]):
        if L[i] <= L[i + 1]:
            increasing.append(L[i + 1])
            increasing_indices.append(i + 1)
            if len(increasing) > len(max_increasing):
                max_increasing = increasing[:]
                max_increasing_indexes = increasing_indices[:]
        else:
            increasing = [L[i + 1]]
            increasing_indices = [i + 1]

        if L[i] >= L[i + 1]:
            decreasing.append(L[i + 1])
            decreasing_indices.append(i + 1)
            if len(decreasing) > len(max_decreasing):
                max_decreasing = decreasing[:]
                max_decreasing_indexes = decreasing_indices[:]
        else:
            decreasing = [L[i + 1]]
            decreasing_indices = [i + 1]

    if len(max_increasing) > len(max_decreasing):
        return sum(max_increasing)
    elif len(max_increasing) < len(max_decreasing):
        return sum(max_decreasing)
    else:
        if max_increasing_indexes[0] < max_decreasing_indexes[0]:
            return sum(max_increasing)
        else:
            return sum(max_decreasing)

print(longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2]))
print(longest_run([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(longest_run([3, 2, -1, 2, 7]))
print(longest_run([100, 200, 300, -100, -200, -1500, -5000]))
print(longest_run([1, 2, 3, 2, -1]))
