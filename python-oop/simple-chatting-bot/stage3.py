print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders
three_reminders = int(input())
five_reminders = int(input())
seven_reminders = int(input())

your_age = (three_reminders * 70 + five_reminders * 21 + seven_reminders * 15) % 105

print(f"Your age is {your_age}; that's a good time to start programming!")
