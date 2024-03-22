class GuessInput:

    def __init__(self):
        self.previous_guess=None
        self.current_guess=0

    def hand_in_guess(self):
        '''loops until the user passes in a number
        in the range of 1 to 100'''
        while True:
            try:
                self.current_guess=int(input("Guess the number\n"))
            except ValueError:
                print(f"Input is not valid. Please enter a number!!\n")
                pass
            else:
                if self.current_guess>1 and self.current_guess<100:
                    return self.current_guess
                elif self.current_guess<100:
                    print(f"{self.current_guess} is over 100!!\n"
                          f"Please enter a number between 1-100!!\n")