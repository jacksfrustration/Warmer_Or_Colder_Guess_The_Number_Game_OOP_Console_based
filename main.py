from number_generator import NumberGenerator
from guesser import GuessInput
from difficulty import ChooseDifficulty
from counter import Counter

def play_game():
    '''Main Game Function'''
    while True:
        difficulty = ChooseDifficulty()
        num_generator = NumberGenerator()
        guess_input = GuessInput()
        play_round(difficulty, num_generator, guess_input)

def play_round(difficulty, num_generator, guess_input):
    """Play a single round of the game."""
    while difficulty.lives > 0:
        guess_input.guessed_number = guess_input.hand_in_guess()
        if num_generator.number == guess_input.guessed_number:
            handle_win(difficulty, num_generator, guess_input)
            break
        else:
            handle_guess(difficulty, num_generator, guess_input)

def handle_win(difficulty, num_generator, guess_input):
    """Handle winning scenario."""
    counter.score += 1
    counter.total_matches += 1
    if counter.score > counter.highest_score:
        counter.write_new_score()
    print(f"You have won!!\n"
          f"The number was {num_generator.number}\n"
          f"You have won {counter.score}/{counter.total_matches} matches played!\n")

def handle_guess(difficulty, num_generator, guess_input):
    """Handle a guess."""
    if guess_input.previous_guess is not None:
        if abs(guess_input.guessed_number - num_generator.number) < abs(guess_input.previous_guess - num_generator.number):
            print("Warmer!\n")
        elif abs(guess_input.guessed_number - num_generator.number) > abs(guess_input.previous_guess - num_generator.number):
            print("Colder!\n")
    else:
        print("Let's see if you are warmer or colder!\n")
    difficulty.lives -= 1
    print(f"You have {difficulty.lives} lives left!!")
    if difficulty.lives == 0:
        counter.total_matches += 1
        print(f"Sorry, you lost. The correct number was {num_generator.number}.\n"
              f"You have won {counter.score}/{counter.total_matches}\n"
              f"Your highest score is {counter.saved_score()}!!")
    guess_input.previous_guess=guess_input.current_guess

if __name__ == "__main__":
    counter = Counter()
    play_game()