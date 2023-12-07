class UnoCard:
    def __init__(self, card_color, card_value):
        # Initialize an Uno card with a color and a value/action.
        self.card_color = card_color
        self.card_value = card_value

    def __str__(self):
        # Return a string representation of the Uno card.
        return f"{self.card_color} {self.card_value}"

    def isPlayable(self, other_card):
        # Determine if the card is playable over another card.
        # A card is playable if it matches the color or value of the other card,
        # or if it's a Wild card.
        return (self.card_color == other_card.card_color or 
                self.card_value == other_card.card_value or 
                self.card_color == "Black")
