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


def compute_balance(balance, minimum_monthly_payment, annual_interest_rate):
    monthly_interest_rate = annual_interest_rate / 12.0
    monthly_unpaid_balance = balance - minimum_monthly_payment

    return monthly_unpaid_balance * (1 + monthly_interest_rate)


def get_balance_after_a_year(balance, annual_interest_rate, monthly_payment_rate):
    for _ in range(12):
        minimum_monthly_payment = monthly_payment_rate * balance
        balance = compute_balance(balance, minimum_monthly_payment, annual_interest_rate)

    return balance


def main():
    balance = eval(input('Enter the initial balance: '))
    annual_interest_rate =eval(input(
        'Enter the annual interest rate as a decimal: '))
    monthly_payment_rate = eval(input(
        'Enter the minimum monthly payment rate as a decimal: '))

    balance_after_a_year = get_balance_after_a_year(balance, annual_interest_rate, monthly_payment_rate)
    print('Remaining balance: ' + str(round(balance_after_a_year, 2)))


if __name__ == '__main__':
    main()
