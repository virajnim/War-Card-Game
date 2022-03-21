# War-Card-Game

Here are the rules to the card game: https://en.wikipedia.org/wiki/War_(card_game)

The objective of the game is to win all of the cards.

The deck is divided evenly among the players, giving each a down stack. In unison, each player reveals the top card of their deck—this is a "battle"—and the player with the higher card takes both of the cards played and moves them to their stack. Aces are high, and suits are ignored.

If the two cards played are of equal value, then there is a "war". Both players place the next three cards face down and then another card face-up. The owner of the higher face-up card wins the war and adds all the cards on the table to the bottom of their deck. If the face-up cards are again equal then the battle repeats with another set of face-down/up cards. This repeats until one player's face-up card is higher than their opponent's.

Most descriptions of War are unclear about what happens if a player runs out of cards during a war. In some variants, that player immediately loses. In others, the player may play the last card in their deck as their face-up card for the remainder of the war or replay the game from the beginning.



Assumptions -
- I have assumed that once a player loses all of his/her cards, the game is over and the other player wins.

- I have assumed the game can end in a tie between both players.

- I am assuming that the winnings of each round are added to the winners deck in a randomized order. After a lot of troubleshooting I found that this needs to be done in order to avoid an infinite loop

- Even though the cards' suits do not matter in this specific game, I added them into the game-play to make the game seem more realistic.

- Even though normally the cards would be dealt one-by-one to each player, I split the randomized 52 card deck in half to shorten time complexity



corner cases -
- If you do not randomize the order of the winnings before you put them at the bottom of the deck you will eventually run into an infinite loop.

- Having the last card of a players deck be a tie could cause an index out of bounds error if not handled properly.



What I might do differently if given more time - 
- If I had more time I would've coded this in OOP using classes and creating objects. Each element of the game would have its own class- like deck, tie pots, player, etc...
  this would make the code more robust for multiple use cases like playing with more than 2 players.

- I would find a better way to compare the cards instead of using a number system that uses a dictionary to translate it to the right cards. I would create a data structure that could immediately
  compare the cards with their original names. For example, an Ace is greater than a King without having to translate them to 13 and 12 respectively.      
