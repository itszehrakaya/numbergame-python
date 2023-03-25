# Bulls and Cows Game

This is a Python implementation of the Bulls and Cows game, also known as Mastermind. The game generates a random 4-digit number and prompts the player to guess the number. After each guess, the game gives feedback in the form of "bulls" and "cows". A "bull" means that a digit in the guess matches the corresponding digit in the secret number and is in the correct position, while a "cow" means that a digit in the guess matches a digit in the secret number but is in the wrong position.



## Getting Started

To run the game, simply run the bulls_cows-2.py file in a Python environment:

`bulls_cows()`

The game will then prompt you to enter number of digits you want to play and then to your guess, and will give you feedback after each guess until you correctly guess the secret number.

to play on the web : https://www.makerduragi.com/bulls-cows/

## Rules
The game follows these rules:

The secret number is a 3,4 or 5 - digit number with no repeated digits.
The player has 10 attempts to guess the number.
After each guess, the game gives feedback in the form of "bulls" and "cows".
The game ends when the player correctly guesses the secret number or runs out of attempts.
Example Gameplay
Here's an example gameplay session:
```py
   Enter your guess: 1234
    1 bull, 1 cow
   Enter your guess: 5678
    0 bulls, 0 cows
   Enter your guess: 3478
    1 bull, 2 cows
   Enter your guess: 3489
    2 bulls, 0 cows 
   Enter your guess: 3481
    3 bulls, 0 cows
   Enter your guess: 3482
  You guessed the number! It was 3482.
  ```
