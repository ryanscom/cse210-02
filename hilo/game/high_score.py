import os

class High_score:
    """ Saves and retrieves a high score in a text file.

    Attributes:
        high_score (int): holds the high_score variable. 
    """

    def __init__(self, current_score, first_name, last_name):
        """Constructs a new instance of High_score. 

        Args:
            self (High_score): An instance of High_score.
            current_score (int): current score of the player
            first_name (str): first name of player / highest score player's first name
            last_name (str): last name of player / highest score player's last name
        """
        self.high_score = 0
        self.compare_score = current_score
        self.first_name = first_name
        self.last_name = last_name

    def compare_and_store(self):
        """ 
        Compares players score with the current high score. If the players high score in bigger stores the players score as the
        new high score in the High_Score.txt file. Updates class variables with the first name, last name, and hight score from the High_Score.txt file

        
        Args:
            self (High_score): An instance of High_score.
        """
      
        with open(os.path.abspath('cse210-02/hilo/game/High_Score.txt'), "r") as file: # Open file
            high_score_info = file.readlines() # get the info from first line as a string and placed in the first index of a string.
            high_score_info = str(high_score_info[0]) # take the info in the first index of the list and make it a string
            high_score_info = high_score_info.split() # make a new list with each part of the string placed in a seperate index
            self.high_score = high_score_info[2] # get the hight score from list and update class high score variable
            # file closes at this point

        if int(self.high_score) < int(self.compare_score): # compare current high score with player high score
            self.high_score = self.compare_score # make the player's hight score the class high score

            string_high_score = str(self.high_score) # make class high score a string
            string_first_name = str(self.first_name) # make class first name a string
            string_last_name = str(self.last_name) # make class last name a string

            with open(os.path.abspath('cse210-02/hilo/game/High_Score.txt'), "w") as file: # open text file 
                file.truncate(0)  # delete the info in the file
                file.write(f"{string_first_name} {string_last_name} {string_high_score}") # write new high score to file
                # file closes at this point
                
        with open(os.path.abspath('cse210-02/hilo/game/High_Score.txt'), "r") as file: # Open file
            high_score_info = file.readlines() # get the info from first line as a string and placed in the first index of a string.
            high_score_info = str(high_score_info[0]) # take the info in the first index of the list and make it a string
            high_score_info = high_score_info.split() # make a new list with each part of the string placed in a seperate index
            self.first_name = high_score_info[0] # get the first name from list and update class high score variable
            self.last_name = high_score_info[1] # get the last name from list and update class high score variable
            self.high_score = high_score_info[2] # get the hight score from list and update class high score variable
            # file closes at this point
            
    def retrieve_high_score(self):
        """ 
        Updates class variables with the first name, last name, and hight score from the High_Score.txt file

        Args:
            self (High_score): An instance of High_score.
        """

        with open(os.path.abspath('cse210-02/hilo/game/High_Score.txt'), "r") as file: # Open file
            high_score_info = file.readlines() # get the info from first line as a string and placed in the first index of a string.
            high_score_info = str(high_score_info[0]) # take the info in the first index of the list and make it a string
            high_score_info = high_score_info.split() # make a new list with each part of the string placed in a seperate index
            self.first_name = high_score_info[0] # get the first name from list and update class high score variable
            self.last_name = high_score_info[1] # get the last name from list and update class high score variable
            self.high_score = high_score_info[2] # get the hight score from list and update class high score variable
            # file closes at this point