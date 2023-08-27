import argparse

from math import ceil, floor, log

parser = argparse.ArgumentParser(description="This program prints recipes \
consisting of the ingredients you provide.")
parser.add_argument("--type", choices=["diff", 'annuity'])
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()
principal = int(args.principal) if args.principal else None
payment = int(args.payment) if args.payment else None
periods = int(args.periods) if args.periods else None
interest = float(args.interest) if args.interest else None

if args.type == 'diff':
    if not principal or not periods or not interest or payment:
        print('Incorrect parameters')
    else:
        i = interest / 1200
        s = 0
        for m in range(periods):
            d = ceil(principal / periods + i * (principal - (principal * m / periods)))
            print(f'Month {m + 1}: payment is {d}')
            s += d
        print(f'Over = {s - principal}')

if args.type == 'annuity':
    if payment and periods and interest:
        i = interest / 1200
        loan_principal = floor(payment / (i * (1 + i) ** periods / ((1 + i) ** periods - 1)))
        print(loan_principal)
    elif principal and periods and interest:
        i = interest / 1200
        monthly_payment = ceil(principal * i * (1 + i) ** periods / ((1 + i) ** periods - 1))
        print(f'Your monthly payment = {monthly_payment}')
    elif principal and payment and interest:
        i = interest / 1200
        n = ceil(log(payment / (payment - i * principal), 1 + i))
        years = n // 12
        months = n % 12
        years_word = '' if years == 0 else 'year' if years == 1 else 'years'
        months_word = '' if months == 0 else 'month' if months == 1 else 'months'
        years_frase = f'{years} {years_word}' if years > 0 else ''
        months_frase = f'{months} {months_word}' if months > 0 else ''
        frase_period = f'{years_frase} and {months_frase}' if years_frase and months_frase else years_frase if years_frase else months_frase
        print(f'It will take {frase_period} to repay this loan!')
        print(f'Overcome = {payment * n - principal}')
    else:
        print('Incorrect parameters')
    
            
        
