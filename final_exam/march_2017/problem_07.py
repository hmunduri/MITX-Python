def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def compute(base):
        total = 0
        powers = list(range(len(L) - 1, -1, -1))
        for power, e in zip(powers, L):
            total += (e * base ** power)

        return total

    return compute


def general_poly_comprehension(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def compute(base):
        powers = list(range(len(L)))[::-1]
        return sum(e * base ** power for power, e in zip(powers, L))

    return compute
