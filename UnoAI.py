from CardDeck import *
import random

class UnoAI:
    def __init__(self):
        # Initialize the AI's hand as an empty list.
        self.ai_hand = []

    def takeTurn(self, top_card):
        # Determine playable cards based on the top card of the discard pile.
        playable_cards = [card for card in self.ai_hand if card.isPlayable(top_card)]

        # If there are playable cards, choose one randomly.
        if playable_cards:
            chosen_card = random.choice(playable_cards)
            self.ai_hand.remove(chosen_card)
            # Assign a random color for Wild cards.
            if chosen_card.card_color == "Black":
                chosen_card.card_color = random.choice(["Red", "Green", "Blue", "Yellow"])
            return chosen_card
        # If no cards are playable, draw a card.
        return "draw"
