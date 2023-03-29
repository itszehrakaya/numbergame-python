import random
import datetime as dt
import time

class BullsAndCows:
    def __init__(self):
        self.start_time = int(time.time())
        self.current_time = dt.datetime.now()
        self.secret_number = None
        self.number_of_digits = None
        self.attempts = 0
    
    def start_game(self):
        print("Welcome to Bulls and Cows game!")
        print(self.current_time.strftime("%d %b %Y %A %H:%M"))
        print("To give up and learn the secret code, please type any string.\n")
        self.get_number_of_digits()
        self.generate_secret_number()
        self.play_game()
    
    def get_number_of_digits(self):
        while True:
            try:
                self.number_of_digits = int(input("How many digits do you want to play? Please type a number among 3, 4, 5: "))
                if self.number_of_digits not in range(3, 6):
                    print("Wrong input. Please enter a number among 3, 4, 5.")
                else:
                    break
            except ValueError:
                print("Wrong input. Please enter a number among 3, 4, 5.")
    
    def generate_secret_number(self):
        digits = [i for i in range(10)]
        self.secret_number = []
        for i in range(self.number_of_digits):
            if i == 0:
                self.secret_number.append(random.choice(digits[1:]))
            else:
                self.secret_number.append(random.choice(digits))
            digits.remove(self.secret_number[-1])
    
    def play_game(self):
        while True:
            
            guess = input("Guess: ")
            tial = guess
            if guess == "":
                print("The secret number is {}. Better luck next time!".format("".join(map(str, self.secret_number))))
                break
            
            try:
                guess = list(map(int, guess))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            if len(guess) != self.number_of_digits:
                print("Your guess must contain {} digits.".format(self.number_of_digits))
                continue
            
            if guess[0] == 0:
                print("First digit mustn't be 0.")
                continue
            
            if len(set(guess)) != self.number_of_digits:
                print("Digits must be different from each other.")
                continue
            
            self.attempts += 1
            bulls = 0
            cows = 0
            
            for i in range(self.number_of_digits):
                if guess[i] == self.secret_number[i]:
                    bulls += 1
                elif guess[i] in self.secret_number:
                    cows += 1
            
            print("{}. {}: {}️➕ {}️➖".format(self.attempts, tial, bulls, cows))
            
            if bulls == self.number_of_digits:
                print("Congrats! You've won in {} attempts.".format(self.attempts))
                end_time = int(time.time())
                elapsed_time = end_time - self.start_time
                print("Digits: {}\nTime (sec): {}\nAttempts: {}".format(self.number_of_digits, elapsed_time, self.attempts))
                break
game = BullsAndCows()
game.start_game()
