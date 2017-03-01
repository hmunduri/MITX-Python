## Problem Set 6

### Problem 6

#### Problem 6-1
Answer the questions below based on the following sorting function. If
it helps, you may paste the code in your programming environment.
Study the output to make sure you understand the way it sorts.

```python
def swapSort(L):
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print(L)
    print("Final L: ", L)
```
Does this function sort the list in increasing or decreasing order?

**increasing**

#### Problem 6-2
What is the worst case time complexity of swapSort? Consider different
kinds of lists when the length of the list is large.

**O(n^2)**

#### Problem 6-3
If we make a small change to the line `for j in range(i+1, len(L)):`
such that the code becomes:

```python
def modSwapSort(L):
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print(L)
    print("Final L: ", L)
```

What happens to the behavior of `swapSort` with this new code?

`modSwapSort` now orders the list in descending order for all lists.

#### Problem 6-4
What happens to the time complexity of this `modSwapSort`?

Best and worst cases stay the same.
