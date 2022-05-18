import random


class Card:
    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Card is to keep track of the displayed card and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of card options.
    """
    card = random.randint(1,13)

    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0
        self.points = 0

    def draw(self):
        """Generates a new random value and calculates the points for the card.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1, 13)
        self.points = 50 if self.value == 5 else 100 if self.value == 1 else 0