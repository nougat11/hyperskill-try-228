from math import ceil, log

def enter_loan_principal():
    print("Enter the loan principal:")
    loan_principal = int(input())
    return loan_principal


def enter_annuity_payment():
    print("Enter the annuity payment:")
    annuity_payment = float(input())
    return annuity_payment


def enter_monthly_payment():
    print("Enter the monthly payment:")
    monthly_payment = int(input())
    return monthly_payment

def enter_periods():
    print("Enter the number of periods:")
    periods = int(input())
    return periods

def enter_loan_interest():
    print("Enter the loan interest:")
    loan_interest = float(input())
    return loan_interest


print("""
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")

payment_type = input()

loan_principal = None
annuity_payment = None
if payment_type in ['a', 'n']:
    loan_principal = enter_loan_principal()
else:
    annuity_payment = enter_annuity_payment()

monthly_payment = None
periods = None

if payment_type == 'n':
    monthly_payment = enter_monthly_payment()
else:
    periods = enter_periods()

loan_interest = enter_loan_interest()

if payment_type == 'n':
    i = loan_interest / 1200
    n = ceil(log(monthly_payment / (monthly_payment - i * loan_principal), 1 + i))
    years = n // 12
    months = n % 12
    years_word = '' if years == 0 else 'year' if years == 1 else 'years'
    months_word = '' if months == 0 else 'month' if months == 1 else 'months'
    years_frase = f'{years} {years_word}' if years > 0 else ''
    months_frase = f'{months} {months_word}' if months > 0 else ''
    frase_period = f'{years_frase} and {months_frase}' if years_frase and months_frase else years_frase if years_frase else months_frase
    print(f'It will take {frase_period} to repay this loan!')
elif payment_type == 'a':
    i = loan_interest / 1200
    monthly_payment = ceil(loan_principal * i * (1 + i) ** periods / ((1 + i) ** periods - 1))
    print(f'Your monthly payment = {monthly_payment}')
else:
    i = loan_interest / 1200
    loan_principal = annuity_payment / (i * (1 + i) ** periods / ((1 + i) ** periods - 1))
    print(f'Your loan principal = {loan_principal}!')
    
    



# write your code here
