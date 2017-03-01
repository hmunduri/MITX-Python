## Problem Set 6

### Problem 4

#### Problem 4-1
Consider the following Python procedure. Specify its order of growth.

```python
def modten(n):
    return n % 10
```

**O(1)**

#### Problem 4-2
Consider the following Python procedure. Specify its order of growth.

```python
def multlist(m, n):
    '''
    m is the multiplication factor
    n is a list.
    '''
    result = []
    for i in range(len(n)):
        result.append(m * n[i])
    return result
```

**O(len(n))**


#### Problem 4-3
Consider the following Python procedure. Specify its order of growth.

```python
def foo(n):
    if n <= 1:
        return 1
    return foo(n / 2) + 1
```

**O(log(n))**

#### Problem 4-4
Consider the following Python procedure. Specify its order of growth.

```python
def recur(n):
    if n <= 0:
        return 1
    else:
        return n*recur(n - 1)
```

**O(n)**

#### Problem 4-5
Consider the following Python procedure. Specify its order of growth.

```python
def baz(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
```

**O(n^2)**
