## Final Exam

### Problem 2

#### Problem 2-1
You have the following class hierarchy:
```python
class A(object):
    def foo(self):
        print 'hi'
class B(A):
    def foo(self):
        print 'bye'
```

**When `a = A()` we say that `a` is an instance of `A`**

#### Problem 2-2
Consider the function `f` below. What is its Big O complexity?
```python
def f(n):
    def g(m):
        m = 0
        for i in range(m):
            print m
    for i in range(n):
        g(n)
```

**O(n)**

#### Problem 2-3
A dictionary is an immutable object because its keys are immutable.

**False because a dictionary is mutable**

#### Problem 2-4
Consider the following two functions and select the correct choice
below:
```python
def foo_one(n):
    """ Assume n is an int >= 0 """
    answer = 1.0
    while n > 1:
        answer *= n
        n -= 1
    return answer

def foo_two(n):
    """ Assume n is an int >= 0 """
    if n <= 1:
        return 1.0
    else:
        return n*foo_two(n-1)
```

**The worst case Big Oh time complexity of foo_one and foo_two are
the same.**

#### Problem 2-5
The complexity of `1 ^ n + n ^ 4 + 4 * n + 4` is

**polynomial**
