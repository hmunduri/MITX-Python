## Problem Set 6

### Problem 5

Here is code for linear search that uses the fact that a set of
elements is sorted in increasing order:

```python
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
```

Consider the following code, which is an alternative version of
`search`.

```python
def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size - i - 1] == e:
            return True
        if L[i] < e:
            return False
    return False
```

`search` and `newsearch` return the same answers for lists `L` of
length 0, 1, or 2.
