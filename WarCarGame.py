import random
from string import capwords

# The creatDeck method creates a standard deck of 52 cards, shuffles that deck, and deals it to 2 players. It is dealt to each player one by one. It is not dealt by cutting the deck in half.
# This method will return a distinct deck of 26 cards to each player.
def createDeck():
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

    #print("\n Player 1 Deck:", p1_cards)
    #print("\n Player 2 Deck" ,p2_cards)

    #print('\n Return Value:', p1_cards.pop(0))
    #print("\n Player 1 Deck:", p1_cards)
    return p1_cards, p2_cards

def num_to_card(p1_card, p2_card):
    numdict = {
        1: "2",
        2: "3",
        3: "4",
        4: "5",
        5: "6",
        6: "7",
        7: "8",
        8: "9",
        9: "10",
        10: "Jack",
        11: "Queen",
        12: "King",
        13: "Ace",
    }
    p1_str = numdict[p1_card[0]] + " of " + p1_card[1]
    p2_str = numdict[p2_card[0]] + " of " + p2_card[1]
    print("{:40}{:40}".format(p1_str, p2_str), end='')

def intro():
    print("Hello, welcome to the game of war! Press 0 to read the game rules or press 1 to start the game")
    val = input()
    if val == '0':
        print("RULES: The objective of the game is to win all of the cards. The deck is divided evenly \namong the players, giving each a down stack. In unison, each player reveals the top card \nof their deck and the player with the higher card takes both of the cards \nplayed and moves them to their stack. Aces are high, and suits are ignored. If the two \ncards played are of equal value, then there is a WAR. Both players place the next three \ncards face down and then another card face-up. The owner of the higher face-up card \nwins the war and adds all the cards on the table to the bottom of their deck. If the \nface-up cards are again equal then the battle repeats with another set of face-down/up cards. \nThis repeats until one player's face-up card is higher than their opponent's. \nIf a player runs out cards, they lose the game")
        intro()
    elif val == '1':
        print("LETS GO TO WAR!!!")
        return 0
    else:
        print("Invalid option")
        intro()

def winner(p1,p2):
    if len(p2) == 0:
            if len(p1) == 0:
                print('\nThe war ended in a tie.')
            else:
                print('\nPlayer 1 wins the war.')
    else:
            print('\nPlayer 2 wins the war.')
 
    return True


def play_war(p1, p2):
    
    intro()
    print("game has started here")
    print("{:40}{:40}".format("Player 1", "Player 2"), 'Result.\n', sep='')
    count = 1
    p1_4cards = []
    p2_4cards = []

    while len(p1) >=0 and len(p2) >=0:

        if len(p1) <= 0 or len(p2) <= 0:
            return winner(p1,p2)
 
        p1_card = p1.pop(0)
        p2_card = p2.pop(0)
        #print(p1_card, p2_card)
        #print(len(p1), " ", len(p2))
        num_to_card(p1_card, p2_card)
        if p2_card[0] == p1_card[0]:
            p1_4cards.extend([p1_card] + p1[0:4])
            del p1[0:4]

            p2_4cards.extend([p2_card] + p2[0:4])
            del p2[0:4]
            print("Tie.\n")
        elif p1_card[0] > p2_card[0]:
            #p1.extend([p1_card, p2_card, p1_4cards, p2_4cards])
            p1 = p1 + [p1_card] + [p2_card] + p2_4cards + p1_4cards
            p1_4cards = []
            p2_4cards = []
            print("Player 1 takes the cards.\n")
            
        
        elif p2_card[0] > p1_card[0]:
            #p2.extend([p2_card, p1_card, p1_4cards, p2_4cards])
            p2 = p2 + [p1_card] + [p2_card] + p2_4cards + p1_4cards
            p1_4cards = []
            p2_4cards = []
            print("Player 2 takes the cards.\n")
            if len(p1) <= 0 or len(p2) <= 0:
                return winner(p1,p2)
        count += 1
    return True




if __name__ == "__main__":
    p1, p2 = createDeck()
    play_war(p1, p2)