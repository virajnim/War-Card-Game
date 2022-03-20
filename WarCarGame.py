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


def play_war(p1, p2):
    intro()
    print("game has started here")
    #THIS IS WHERE YOU ENDED LAST NIGHT. THE IDEA I HAD WAS TO HAVE A WHILE LOOP UNTIL ONE OF THE DECKS IS EMPTY. THE WHILE LOOP WILL CONTAIN 3 IF/ELIF STATEMENTS THAT WILL HANDLE THE COMPARISON OF THE CARDS.
    



if __name__ == "__main__":
    p1, p2 = createDeck()
    play_war(p1, p2)