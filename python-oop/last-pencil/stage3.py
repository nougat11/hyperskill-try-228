print("How many pencils would you like to use:")
pencils = int(input())
players = ['John', 'Jack']
print('Who will be the first (John, Jack):')
name = input()
index = players.index(name)
while pencils > 0:
    print('|' * pencils)
    print(f"{players[index]}'s turn")
    count = int(input())
    pencils -= count
    index += 1
    index %= len(players)
    
