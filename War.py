"""
Recreate the card game "War"
In this game there are 2 players.
Each player gest 26 cards.
Objective of the game is to take away the other players cards. 
if you have no more cards left, you lost.
Each player will draw 1 card, the highest card wins the hand, and the other player takes your card.
If you draw equal cards, each player draws an extra 3 cards. this is called "war"
Another card is drawn, whoever wins that hand, gets to take all 4 of the cards.

-Structure
    -Create Class for
        1)Cards
            -Suit
            -Rank
            -Interger value
        2)Deck
            -create all 52 card objects
            -hold as a list of card objects
            -shuffle a deck thru method call (random library shuffle function)
            -pop method from cards list
        3)Player
    -Incorporate Game logic revolving around these
"""
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    def __init__(self,suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit
    
class Deck:
    def __init__(self):
        self.allCards = []
        for suit in suits:
            for rank in ranks:
                createdCard = Card(suit,rank)
                self.allCards.append(createdCard)
    def shuffle(self):
        random.shuffle(self.allCards)
    def deal_one(self):
        return self.allCards.pop()
class player:
    def __init__(self, name):
        self.name = name
        self.allCards = []
    def remove_one(self):
        return self.allCards.pop(0)
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.allCards.extend(new_cards)
        else:
            self.allCards.append(new_cards)
    def __str__(self):
        return f'Player {self.name} has {len(self.allCards)} cards.'

"""
RUNNING GAME
"""
player_one = player("One")
player_two = player("Two")
new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0
while game_on:
    round_num += 1
    print(f"Round {round_num}")
    if len(player_one.allCards) == 0:
        print("Player One Wins")
        game_on = False
        break
    if len(player_two.allCards) == 0:
        print("Player Two Wins")
        game_on = False
        break
# START NEW ROUND
    player_one_cards_in_play = []
    player_one_cards_in_play.append(player_one.remove_one())
    player_two_cards_in_play = []
    player_two_cards_in_play.append(player_two.remove_one())
# WHILE AT WAR
    at_war = True
    while at_war:
        if player_one_cards_in_play[-1].value > player_two_cards_in_play[-1].value:
            player_one.add_cards(player_one_cards_in_play)
            player_one.add_cards(player_two_cards_in_play)
            at_war = False
        elif player_one_cards_in_play[-1].value < player_two_cards_in_play[-1].value:
            player_two.add_cards(player_one_cards_in_play)
            player_two.add_cards(player_two_cards_in_play)
            at_war = False
        else:
            print("IT IS WAR")
            if len(player_one.allCards) < 5:
                print("Player one doesn't have enough cards remaining.")
                print("Player 2 Wins!")
                game_on = False
                break
            if len(player_two.allCards) < 5:
                print("Player Two doesn't have enough cards remaining.")
                print("Player 1 Wins!")
                game_on = False
                break
            else:
                for num in range(3):
                    player_one_cards_in_play.append(player_one.remove_one())            
                    player_two_cards_in_play.append(player_two.remove_one())