class ChooseDifficulty:

    def __init__(self):
        self.lives=self.choose_difficulty()



    def choose_difficulty(self):
        '''loops until the user chooses the difficulty out of the two options'''
        while True:
            setting=input("Choose a difficulty level!\n"
                      "\tEasy is 10 lives.\n"
                      "\t\tHard is 5 lives!\n").lower()
            if setting in ("easy","hard"):
                if setting=="easy":
                    return 10

                elif setting=="hard":
                    return 5
            else:
                print(f"{setting} is not a valid option. Try again!!\n")