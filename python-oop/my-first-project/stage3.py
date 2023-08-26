# Write your code here
bubblegum = 202
toffee = 118
ice_cream = 2250
milk_chocolate = 1680
doughnut = 1075
pancake = 80
print(f"""
Earned amount:
Bubblegum: ${bubblegum}
Toffee: ${toffee}
Ice cream: ${ice_cream}
Milk chocolate: ${milk_chocolate}
Doughnut: ${doughnut}
Pancake: ${pancake}

Income: ${bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake}

Staff expenses:""")
staff = int(input())
print('Other expenses:')
other = int(input())
print(f'Net income: ${bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake - staff - other}')

