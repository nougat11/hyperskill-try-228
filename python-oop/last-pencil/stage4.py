print("How many pencils would you like to use:")
pencils = None
while True:
    pencils = input()
    if not pencils.isnumeric():
        print('The number of pencils should be numeric')
    elif pencils == '0':
        print('The number of pencils should be positive')
    else:  
        pencils = int(pencils)
        break
        
players = ['John', 'Jack']
print('Who will be the first (John, Jack):')
name = None
while True:
    name = input()
    if name not in players:
        print(f'Choose between {" and ".join(players)}')
    else:
        break
index = players.index(name)
while pencils > 0:
    print('|' * pencils)
    print(f"{players[index]}'s turn")
    while True:
        count = input()
        if count not in ('1', '2', '3'):
            print("Possible values: '1', '2' or '3'")
        else:
            count = int(count)
            if count > pencils:
                print('Too many pencils were taken')
            else:
                break
    pencils -= count
    index += 1
    index %= len(players)
print(f'{players[index]} won')
    
