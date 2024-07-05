# Advaced dictionaries

square_dict = {}
for num in range(1, 11):
    square_dict[num] = num*num

print(square_dict)

square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)

for i in square_dict.items():
    print(i)

person = {'name': 'jo', 'age': 42, 'height': 170}
for item in person:
    print(f"key value pair: {item} -> {person[item]}")
    
friends = ["Will", "Bernie", "Garth", "Suze"]
card_suit = ["Spades", "Clubs", "Diamonds", "Hearts"]
import random
random_dict = {friend:random.choice(card_suit) for friend in friends}
print(random_dict)

from random import shuffle
shuffle(card_suit)
card_friends = {friend:card for (friend, card) in zip(friends, card_suit)}
print(card_friends)

tourny_dict = {'Dan': 10, 'Wolfgang': 20, 'June': 53, 'Tany': 37, 'Sharon': 14}
new_player = {"Will":0}
tourny_dict.update(new_player)
print(tourny_dict)

# To eliminate player from tourney dict, we could use a for loop or the filer function

next_round = {}
for player, score in tourny_dict.items():
    if score > 20:
        next_round[player] = score
print(next_round)

next_round = {}
next_round = dict(filter(lambda player: player[1] > 20, tourny_dict.items()))
print(next_round)