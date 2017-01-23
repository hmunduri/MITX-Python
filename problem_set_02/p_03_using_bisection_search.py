__author__ = 'm'

"""
This program uses bisection search to find out the smallest monthly payment
such that we can pay off the entire balance within a year.
"""

from p_02_paying_debt_off_in_a_year import compute_balance_after


def compute_bounds(balance: float,
                   annual_interest_rate: float) -> (float, float):
    """"
    :param balance: balance
    :param annual_interest_rate: annual interest rate
    :return: lower and upper bounds
    """
    monthly_interest_rate = annual_interest_rate / 12
    lower_bound = balance / 12
    upper_bound = balance * (1 + monthly_interest_rate) ** 12 / 12

    return lower_bound, upper_bound


def compute_lowest_payment(balance: float,
                           annual_interest_rate: float) -> float:
    """
    :param balance: balance
    :param annual_interest_rate: annual interest rate
    :return: the lowest payment to pay balance within 12 months using
    bisection search and rounded to 2 decimal places
    """
    lower_bound, upper_bound = compute_bounds(balance, annual_interest_rate)

    while True:
        lowest_payment = (lower_bound + upper_bound) / 2
        balance_after_a_year = compute_balance_after(balance,
                                                     lowest_payment,
                                                     annual_interest_rate)

        if abs(balance_after_a_year) <= 0.01:
            return round(lowest_payment, 2)

        if balance_after_a_year > 0:
            lower_bound = lowest_payment
        else:
            upper_bound = lowest_payment


def main():
    balance = eval(input('Enter the initial balance: '))
    annual_interest_rate = eval(input('Enter the annual interest rate: '))

    lowest_payment = compute_lowest_payment(balance, annual_interest_rate)
    print('Lowest Payment: ' + str(lowest_payment))


if __name__ == '__main__':
    main()
