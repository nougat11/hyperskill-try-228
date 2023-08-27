from math import ceil

print('Enter the loan principal:')
loan_principal = int(input())
print("""
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:""")
calculate_type = input()
if calculate_type == 'p':
    print('Enter the number of months:')
    number_of_months = int(input())
    monthly_payment = ceil(loan_principal / number_of_months)
    last_payment = loan_principal - (number_of_months - 1) * monthly_payment
    last_payment_output = f' and the last payment = {last_payment}' if last_payment else ''
    print()
    print(f'Your monthly payment = {monthly_payment}{last_payment_output}.')
else:
    monthly_payment = int(input())
    number_of_months = ceil(loan_principal / monthly_payment)
    print()
    month_output = "month" if number_of_months == 1 else "months"
    print(f'It will take {number_of_months} {month_output} to repay the loan')


# write your code here
