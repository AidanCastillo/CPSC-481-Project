##FILE IS UNIMPORTANT NO LONGER USED

import random

cards = []
colors = ["Red", "Green", "Blue", "Yellow"]
action = ["Reverse", "Skip", "Draw 2", "Draw 4"]

def createDeck():
    #numbered cards
    for i in range(4):
        number = 0
        for j in range(10):
            card = colors[i] + "_" + str(number)
            if number == 0:
                cards.append(card)
            else:
                cards.append(card)
                cards.append(card)
            number += 1
    #Action Cards
    for i in range(4):
        index = 0
        for j in range(3):
            card = colors[i] + "_" + action[index]
            cards.append(card)
            card.append(card)
            index += 1

    #Wild Cards
    for i in range(4):
        cards.append("Wild")
        cards.append("Wild Draw 4")


createDeck()
random.shuffle(cards)
random.shuffle(cards)
print(cards)
