__author__ = 'm'

"""
Now write a program that calculates the minimum fixed monthly payment needed in
order pay off a credit card balance within 12 months. By a fixed monthly
payment, we mean a single number which does not change each month, but instead
is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will
pay off all debt in under 1 year, for example:

Lowest Payment: 180
"""


def compute_balance(balance: float,
                    fixed_payment: float,
                    annual_interest_rate: float) -> float:
    """
    :param balance: balance
    :param fixed_payment: fixed payment
    :param annual_interest_rate:  annual interest rate
    :return: the balance at the end of a month
    """
    monthly_interest_rate = annual_interest_rate / 12
    monthly_unpaid_balance = balance - fixed_payment

    return monthly_unpaid_balance * (1 + monthly_interest_rate)


def compute_balance_after(balance: float,
                          fixed_payment: float,
                          annual_interest_rate: float,
                          months: int=12) -> float:
    """
    :param balance: balance
    :param fixed_payment: fixed payment
    :param annual_interest_rate: annual interest rate
    :param months: number of months
    :return: the balance after months
    """
    for _ in range(months):
        balance = compute_balance(balance,
                                  fixed_payment,
                                  annual_interest_rate)

    return balance


def compute_fixed_monthly_payment(balance: float,
                                  annual_interest_rate: float) -> float:
    """
    :param balance: balance
    :param annual_interest_rate: annual interest rate
    :return: fixed payment to pay balance within 12 months rounded to two
    decimal places
    """
    fixed_payment = 0

    while True:
        fixed_payment += 10
        balance_after_a_year = compute_balance_after(balance,
                                                     fixed_payment,
                                                     annual_interest_rate)

        if balance_after_a_year <= 0:
            return round(fixed_payment, 2)


def main():
    balance = eval(input('Enter the initial balance: '))
    annual_interest_rate = eval(
        input('Enter the annual interest rate as a decimal: '))
    lowest_payment = compute_fixed_monthly_payment(balance,
                                                   annual_interest_rate)
    print('Lowest Payment: ' + str(lowest_payment))


if __name__ == '__main__':
    main()
