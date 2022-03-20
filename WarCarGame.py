import random
from string import capwords

#def createDeck():
suites = ["Hearts", "Clubs", "Diamonds", "Spades" ]
deck = []
p1_cards = []
p2_cards = []
for suite in suites:
    for i in range(1,14):
        deck.append([i , suite])
random.shuffle(deck)
#print(deck)

for i in range(0,len(deck),2):
    p1_cards.append(deck[i])
    p2_cards.append(deck[i+1])

print("\n Player 1 Deck:", p1_cards)
print("\n Player 2 Deck" ,p2_cards)

print('\n Return Value:', p1_cards.pop(0))
print("\n Player 1 Deck:", p1_cards)