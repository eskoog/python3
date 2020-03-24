lottery_numbers = {13, 21, 22, 5, 8}
players = (
    {'name': 'Ted', 'numbers': {1, 2, 3, 4, 5}}, 
    {'name': 'Bill', 'numbers': {11, 12, 13, 14, 15}}, 
)
match = lottery_numbers.intersection(players[0]['numbers'])
num_right = len(match)
print(players[0]['name'] + ' got ' + str(num_right) + ' right!')

match = lottery_numbers.intersection(players[1]['numbers'])
num_right = len(match)
print(players[1]['name'] + ' got ' + str(num_right) + ' right!')