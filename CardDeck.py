from UnoCard import *
import random

class CardDeck:
    def __init__(self):
        # Initialize an empty list to represent the deck of Uno cards.
        self.deck_cards = []

    def assembleDeck(self):
        # Populate the deck with Uno cards.
        # 2 of each number except 0, two of each action card, and 4 of each wild card.
        for color in ["Red", "Blue", "Green", "Yellow"]:
            self.deck_cards.append(UnoCard(color, 0))

            for value in range(1, 10):
                # Add two of each number card
                self.deck_cards.append(UnoCard(color, value))
                self.deck_cards.append(UnoCard(color, value))

            for action in ["Reverse", "Skip", "Draw 2"]:
                # Add two of each action card.
                self.deck_cards.append(UnoCard(color, action))
                self.deck_cards.append(UnoCard(color, action))
        # Add Wild and Draw 4 cards.
        for _ in range(4):
            self.deck_cards.append(UnoCard("Black", "Wild"))
            self.deck_cards.append(UnoCard("Black", "Draw 4"))
        self.mixDeck()

    def mixDeck(self):
        random.shuffle(self.deck_cards)
    
    def drawCard(self):
        # Remove and return the top card from the deck.
        return self.deck_cards.pop(0)

    def addToDiscardPile(self, card):
        # Handle Wild card color selection.
        while card.card_color == "Black":
            chosen_color = input("Choose a color (Red, Green, Blue, Yellow): ").capitalize()
            if chosen_color not in ["Red", "Green", "Blue", "Yellow"]:
                print("Invalid color.")
            else:
                card.card_color = chosen_color
         # Add the played card to the discard pile.
        self.deck_cards.append(card)
