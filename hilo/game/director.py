
from game.deck import Deck


class Director():
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        score (int): The current score for one round of play.
        right_wrong (str): Check if guessed value was correct and used to print related message
        current_card (int): holds the current card number
        next_card (int): holds the next card number
        current_suit (str): holds the current card suit icon
        next_suit (str): holds the next card suit icon
        guess (str): hold "h" or "l" depending on user input
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
        If yes: draws a new card from deck class.
        Ask the user to guess High or Low (h/l).
        Draws the next card from deck class.

        Args:
            self (Director): An instance of Director.
        """

        print()
        pick_card = input("pick a card? [y/n] ")
        self.is_playing = (pick_card == "y")

        if pick_card == "n":
            self.print_ending_score()

        if pick_card == "y":
            if self.current_card != self.next_card:
                deck = Deck() # create an instance of the deck class
                deck.draw() # run the .draw method in the instance 
                card = deck.value # retrieve the variable .value from the draw method
                suit = deck.suit # retrieve the variable .suit from the draw method
                self.current_card = card # update the global value for self.current_card in the director class
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
        Updates if the user guessed right or wrong with the right_wrong class variable.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        if self.guess.lower() == "l":
            if self.next_card > self.current_card:
                self.score -= 75
                self.right_wrong = "w"
                
            elif self.next_card < self.current_card:
                self.score += 100
                self.right_wrong = "r"
            else:
                self.right_wrong = "t"

        elif self.guess.lower() == "h":
            if self.next_card < self.current_card:
                self.score -= 75
                self.right_wrong = "w"

            elif self.next_card > self.current_card:
                self.score += 100
                self.right_wrong = "r"
            else:
                self.right_wrong = "t"
        

    def do_outputs(self):
        """Displays the card and the score. Also makes ending card be the begining card for the next interation
        
        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        print()
        print(f"The next card is: {self.next_card}{self.next_suit}")

        if self.right_wrong == "r":
            print(f"You gained 100 points!")
        elif self.right_wrong == "w":
            print(f"You lost 75 points!")
        elif self.right_wrong == "t":
            print("You got the same number, no points!")

        print()
        print(f"You now have a total score of {self.score} points")
        
        self.current_card = self.next_card # change current_card value to the next_card value
        self.current_suit = self.next_suit # change current_suit value to the next_suit value

        self.is_playing == (self.score > 0)
        
    def print_ending_score(self):
        """Displays the players ending score and ends the game
        
        Args:
            self (Director): An instance of Director.
        """
        
        print()
        print(f"Game Over!")
        print(f"Your score is: {self.score}")
        print()

        self.is_playing = False
