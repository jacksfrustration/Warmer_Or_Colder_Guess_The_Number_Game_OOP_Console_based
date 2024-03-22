class Counter:

    def __init__(self):
        self.lives=0
        self.score=0
        self.total_matches=0
        self.highest_score=self.saved_score()


    def saved_score(self):
        '''returns high score that is stored inside the text file
        if the file doesnt exists it creates the text file
        and assigns the highest score to a default of 0'''
        try:
            with open("high_score.txt","r")as file:
                highest_score=int(file.read())
        except FileNotFoundError:
            with open("high_score.txt","w") as file:
                file.write(str(0))
            highest_score=0
        finally:
            return highest_score

    def write_new_score(self):
        '''triggred every time the player wins a match
        dependent upon whether the user's current score is higher than
        the text files saved highest score
        '''
        with open("high_score.txt","w") as file:
            file.write(str(self.score))