<<<<<<< HEAD
from game.deck import Deck
=======
<<<<<<< HEAD
from game.deck import Deck


class Director():
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        self.is_playing = True
        self.score = 300
        self.right_wrong = "x"
        self.current_card = 0
        self.next_card = -1
        self.current_suit = "a"
        self.next_suit = "b"
        self.guess = ""
    
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to pick a card.

        Args:
            self (Director): An instance of Director.
        """

        pick_card = input("pick card? [y/n] ")
        self.is_playing = (pick_card == "y")

        if self.current_card != self.next_card:
            deck = Deck()
            deck.draw()
            card = deck.value
            suit = deck.suit
            self.current_card = card
            self.current_suit = suit

        print(f"The card is: {self.current_card}{self.current_suit}")

        self.guess = input(f"Higher or lower? [h/l] ")

        deck = Deck()
        deck.draw()
        card = deck.value
        suit = deck.suit
        self.next_card = card
        self.next_suit = suit
        

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        if self.guess.lower() == "l":
            if self.next_card > self.current_card:
                self.score -= 75
                self.right_wrong = "w"
                
            if self.next_card < self.current_card:
                self.score += 100
                self.right_wrong = "r"

        if self.guess.lower() == "h":
            if self.next_card < self.current_card:
                self.score -= 75
                self.right_wrong = "w"

            if self.next_card > self.current_card:
                self.score += 100
                self.right_wrong = "r"
        

    def do_outputs(self):
        """Displays the card and the score. Also asks the player if they want to pick another card. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        

        print(f"The next card was: {self.next_card}{self.next_suit}")

        if self.right_wrong == "r":
            print(f"You gained 100 points!")
        if self.right_wrong == "w":
            print(f"You lost 75 points!")

        print(f"You now have a total score of {self.score} points")
        
        self.current_card = self.next_card
        self.current_suit = self.next_suit

        self.is_playing == (self.score > 0)
        
