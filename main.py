from CardDeck import * # Corrected import statement
from UnoAI import *
import random

# Initialize the deck and shuffle it
game_deck = CardDeck()
game_deck.assembleDeck()

class PlayerHand:
    def __init__(self):
        self.cards_in_hand = []
        # Each player starts with 7 cards
        for _ in range(7):
            self.addCard(game_deck.drawCard())

    def addCard(self, card):
        # Add a card to the player's hand
        self.cards_in_hand.append(card)

    def removeCard(self, card):
        # Remove a card from the player's hand
        self.cards_in_hand.remove(card)

    def displayHand(self):
        # Display the cards in the player's hand
        for idx, card in enumerate(self.cards_in_hand):
            if card.card_color != "Black":
                print(f"{idx+1}.) {card.card_color} {card.card_value}")
            else:
                print(f"{idx+1}.) {card.card_value}")

def isValidPlay(player_card, top_card):
    # Check if the player's card can be played on the top card
    return player_card.isPlayable(top_card)

def reshuffleDeck(discard_pile):
    # Reshuffle the discard pile into the deck when running low on cards
    for card in discard_pile.deck_cards[:-1]:
        if card.card_value in ["Wild", "Draw 4"]:
            card.card_color = "Black"
    game_deck.deck_cards += discard_pile.deck_cards[:-1]
    game_deck.mixDeck()

def processSpecialCard(turn, played_card):
    # Process special cards like Draw 2, Draw 4, Skip, and Reverse
    cards_to_draw = 0
    if played_card.card_value == "Draw 2":
        cards_to_draw = 2
    elif played_card.card_value == "Draw 4":
        cards_to_draw = 4

    # Apply the effects of the special cards
    if turn == "ai":
        for _ in range(cards_to_draw):
            player_hand.addCard(game_deck.drawCard())
    else:
        for _ in range(cards_to_draw):
            ai_player.ai_hand.append(game_deck.drawCard())

    if played_card.card_value in ['Skip', 'Reverse']:
        return False
    return True

# Initialize the player and AI's turn, hands, and the discard pile
turn = "player"
discard_pile = CardDeck()
player_hand = PlayerHand()
ai_player = UnoAI()

# Draw initial hands for both player and AI
for _ in range(7):
    ai_player.ai_hand.append(game_deck.drawCard())
discard_pile.deck_cards.append(game_deck.drawCard())
while not isinstance(discard_pile.deck_cards[-1].card_value, int):
    discard_pile.deck_cards.append(game_deck.drawCard())

# Main game loop
while len(player_hand.cards_in_hand) > 0 and len(ai_player.ai_hand) > 0:
    # Reshuffle the deck if it has too few cards
    if len(game_deck.deck_cards) <= 4:
        reshuffleDeck(discard_pile)
        discard_pile.deck_cards = [discard_pile.deck_cards[-1]]
    
    played_card = None
    if turn == "player":
        print("\n-----------------------------------------------------------------------\n")
        print(f"There are {len(game_deck.deck_cards)} in the deck.")
        print(f"AI is holding {'Uno!' if len(ai_player.ai_hand) == 1 else f'{len(ai_player.ai_hand)} cards.'}")
        print(f"Display Card: {discard_pile.deck_cards[-1].card_color} {discard_pile.deck_cards[-1].card_value}")
        player_hand.displayHand()

        # Player chooses a card to play or draws a card
        while not played_card:
            player_choice = input("Select a card or type 'draw': ")
            if player_choice.lower() == "draw":
                player_hand.addCard(game_deck.drawCard())
                played_card = UnoCard("Blank", "Blank")
            elif player_choice.isnumeric():
                chosen_card = player_hand.cards_in_hand[int(player_choice) - 1]
                if isValidPlay(chosen_card, discard_pile.deck_cards[-1]):
                    played_card = chosen_card
                    player_hand.removeCard(chosen_card)
                    discard_pile.addToDiscardPile(played_card)
                else:
                    print("Invalid card selection.")
            else:
                print("Invalid input.")
    else:
        print("\n-----------------------------------------------------------------------\n")
        ai_choice = ai_player.takeTurn(discard_pile.deck_cards[-1])
        if ai_choice == "draw":
            print("AI draws a card.")
            ai_player.ai_hand.append(game_deck.drawCard())
        else:
            print(f"AI plays: {ai_choice.card_color} {ai_choice.card_value}")
            played_card = ai_choice
            discard_pile.addToDiscardPile(played_card)

    if played_card and processSpecialCard(turn, played_card):
        turn = 'ai' if turn == 'player' else 'player'

print("\n-----------------------------------------------------------------------\n")
if len(player_hand.cards_in_hand) > 0:
    print("You lost!")
else:
    print("You won!")
