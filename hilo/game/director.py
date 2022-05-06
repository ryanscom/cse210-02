from game.deck import Deck


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
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

        self.card = []
        deck = Deck()
        self.card.append(deck)

    
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            guess, current_card, next_card = self.get_inputs()

            self.do_updates(guess, current_card, next_card)
            self.do_outputs(next_card)

    def get_inputs(self):
        """Ask the user if they want to pick a card.

        Args:
            self (Director): An instance of Director.
        """
        
        draw_card = self.card[0]

        pick_card = input("pick card? [y/n] ")
        self.is_playing = (pick_card == "y")

        current_card = draw_card.draw()
        print(f"The card is: {current_card}")

        guess = input(f"Higher or lower? [h/l] ")

        next_card = draw_card.draw()

        return guess, current_card, next_card
       

    def do_updates(self, guess, current_card, next_card):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        if guess.lower() == "l":
            if next_card > current_card:
                self.score -= 75
            if next_card < current_card:
                self.score += 100

        if guess.lower() == "h":
            if next_card < current_card:
                self.score -= 75
            if next_card > current_card:
                self.score += 100
        

    def do_outputs(self, next_card):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
      

        print(f"The next card was: {next_card}")
        print(f"This roll gave you {self.score} points")
        print(f"Your score is: {self.total_score}\n")

        self.is_playing == (self.score > 0)
        