import random

class Deck:
    """A deck of cards that can hold values between 1 and 13.

    The responsibility of the Deck is to keep track of value of the card facing up. 
   
    Attributes:
        value (int): number of the random card pulled from the deck
    """

    def __init__(self):
        """Constructs a new instance of Die with a value and points attribute.

        Args:
            self (Deck): An instance of Deck.
        """
        self.value = 0
    

    def draw(self):
        """Generates a new random value and calculates the points.
        
        Args:
            self (Deck): An instance of Deck.
        """
        self.value = random.randint(1, 13)

        
        

        