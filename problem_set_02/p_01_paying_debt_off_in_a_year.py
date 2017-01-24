__author__ = 'm'

"""
Write a program to calculate the credit card balance after one year if a person
only pays the minimum monthly payment required by the credit card company each
month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining
balance. At the end of 12 months, print out the remaining balance. Be sure to
print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
instead of

Remaining balance: 813.4141998135
So your program only prints out one thing: the remaining balance at the end of
the year in the format:

Remaining balance: 4784.0
"""


def compute_balance(
        balance: float,
        payment: float,
        annual_interest_rate: float) -> float:
    """
    :param balance: balance
    :param annual_interest_rate:  annual interest rate
    :param payment: monthly payment
    :return: the balance at the end of a month
    """
    monthly_interest_rate = annual_interest_rate / 12
    monthly_unpaid_balance = balance - payment

    return monthly_unpaid_balance * (1 + monthly_interest_rate)

def compute_balance_with_minimum_payment(
        balance: float,
        annual_interest_rate: float,
        monthly_payment_rate: float) -> float:
    """
    :param balance: balance
    :param annual_interest_rate: annual interest rate
    :param monthly_payment_rate: monthly payment rate
    :return: balance at the end of a month when paying the minimum
    """
    min_monthly_payment = monthly_payment_rate * balance

    return compute_balance(balance,
                           min_monthly_payment,
                           annual_interest_rate)


def main():
    balance = eval(input('Enter the initial balance: '))
    annual_interest_rate =eval(input(
        'Enter the annual interest rate as a decimal: '))
    monthly_payment_rate = eval(input(
        'Enter the minimum monthly payment rate as a decimal: '))

    for _ in range(12):
        balance = compute_balance_with_minimum_payment(
            balance,
            annual_interest_rate,
            monthly_payment_rate)

    print('Remaining balance: ' + str(round(balance, 2)))


if __name__ == '__main__':
    main()
