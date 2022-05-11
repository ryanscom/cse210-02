class Introduction:
    def _init_(self):
        self.first_name = ""
        self.last_name = ""
    def get_name(self):
        self.get_input()
        self.print_outputs()
    def get_input(self):
        print()
        self.first_name = input("Enter first name: ")
        self.last_name = input("Enter last name: ")
    def print_outputs(self):
        print()
        print(f"Welcome {self.first_name} {self.last_name}")
        print(f"Let's play!")
        print("The player starts the game with 300 points. Individual cards are represented as a number from 1 to 13.")
        print()
