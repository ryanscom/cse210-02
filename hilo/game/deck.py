<<<<<<< HEAD
import random
=======
<<<<<<< HEAD
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
        self.suit = 0
    
    def draw(self):
        """Generates a new random value and calculates the points.
        
        Args:
            self (Deck): An instance of Deck.
        """
        suits = ['\u2666', '\u2665', '\u2663', '\u2660']

        self.suit = random.choice(suits)
        self.value = random.randint(1, 13)



""" Notes on how to access a variable within a class method

deck = Deck() # make an instance of Deck class
deck.draw() # run the method in that instance
card = deck.value # get the value of the variable wanted in the method 

print(card) 

"""
=======

>>>>>>> b556dd559c37ba5d4fe2c52764aaefa83c06ba74

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
        self.suit = 0
    
    def draw(self):
        """Generates a new random value and calculates the points.
        
        Args:
            self (Deck): An instance of Deck.
        """
        suits = ['\u2666', '\u2665', '\u2663', '\u2660']

        self.suit = random.choice(suits)
        self.value = random.randint(1, 13)



""" Notes on how to access a variable within a class method

deck = Deck() # make an instance of Deck class
deck.draw() # run the method in that instance
card = deck.value # get the value of the variable wanted in the method 

print(card) 

<<<<<<< HEAD
"""
=======
    def draw():
        """draws a card from the deck.  value of 1-13 """
>>>>>>> debfaf85fae40d3fe2fc11c5145a3e9e8f1acbb1
>>>>>>> b556dd559c37ba5d4fe2c52764aaefa83c06ba74
