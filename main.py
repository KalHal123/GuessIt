import random
import time
from time import sleep as sl
import os
import sys
from assets.libraries.json_helper import JSONHelper

# Get the directory of the executable
if getattr(sys, 'frozen', False):
    # If running as a bundled executable
    base_dir = sys._MEIPASS
else:
    # If running as a script
    base_dir = os.path.dirname(__file__)

# Paths for configuration and logs
config_path = os.path.join(base_dir, 'assets', 'config', 'config.json')
logs_dir = os.path.join(base_dir, 'assets', 'logs')
log_file_path = os.path.join(logs_dir, 'log.txt')

# Initialize JSONHelper with the path to the JSON file
jshelp = JSONHelper(config_path)

def write_to_log(input):
    """Append a message to the log file."""
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    with open(log_file_path, 'a') as file:
        file.write(input + '\n')

def main(diff, mode):
    points = 0
    turns = 1
    diff = int(diff)  # Convert to integer
    mode = int(mode)  # Convert to integer

    if diff == 1:
        turns += 9
    elif diff == 2:  
        turns += 4
    elif diff == 3:  
        turns += 2

    data = {
        "mode": f"{mode}",
        "diff": f"{diff}"
    }
    jshelp.save_data(data)
    
    comp_number = random.randint(1, 7 + (diff - 1) * 5)  # Initial random number generation
    write_to_log(f"New game started with difficulty: {diff}, mode: {mode}, and {turns} turn(s)")
    write_to_log(f"Comp_number: {comp_number}")
    write_to_log("--------------------------------------------------------------")
    
    while turns > 0:
        try:
            print(f"Say a number between 1 and {7 + (diff - 1) * 5} (including 1 and {7 + (diff - 1) * 5})!")
            user_number = input("Your Number: ")
            write_to_log(f"User number: {user_number}")
            if int(user_number) == comp_number:
                print("Your number was correct!")
                points += 1
                write_to_log(f"User guessed the number correctly and got +1 point.")
                if mode == 1:  # Hard mode: 30% chance to get 1 extra turn
                    if random.random() < 0.3:
                        turns += 1
                        print("You got an extra turn!")
                        print("+1 turn!")
                        write_to_log("User got an extra turn.")
                else:  # Normal mode: Guaranteed chance to get 1 extra turn and 50% chance for 2 extra turns
                    turns += 1
                    print("You got an extra turn!")
                    print("+1 turn!")
                    write_to_log("User got an extra turn.")
                    if random.random() < 0.5:
                        turns += 1
                        print("You got an additional extra turn!")
                        print("+2 turns!")
                        write_to_log("User got an additional extra turn.")
                comp_number = random.randint(1, 7 + (diff - 1) * 5)  # Change the number after correct guess
                write_to_log(f"New random number generated: {comp_number}")
            else:
                print(f"You sadly didn't guess the right number.")
                write_to_log(f"User didn't guess the right number, new turn. Correct number: {comp_number}")
            turns -= 1
            if turns > 0:  
                print(f"New turn! You now have {turns} turn(s) left.")
                write_to_log(f"New turn! User now has {turns} turn(s) left")
        except Exception as e:
            print("Oh no, something went wrong!")
            write_to_log(f"Error: {str(e)}")
            # Ensure turns are not decremented even if an exception occurs
            continue
    
    print("You are now out of turns and the game is over!")
    print(f"You have collected {points} points!")
    print('The entire game\'s history can be found in the "log.txt" file located in "assets/logs".')
    write_to_log("--------------------------------------------------------------")
    write_to_log(f"Game Over. User collected a total of {points} point(s).")
    write_to_log("--------------------------------------------------------------")
    print("New Game? Y/N")
    yn = input(">")
    if yn.lower() == "y":
        start()
    elif yn.lower() == "n":
        print("Ok, Game Over.")
    else:
        print("Wrong Input, Please only put Y or N")

def start():
    print("Welcome to the number game where you have to guess a randomly generated number! You can choose between 3 difficulty grades!")
    print("1: You get 10 turns and the number is between 1 and 7")
    print("2: You get 5 turns and the number is between 1 and 10")
    print("3: You get 3 turns and the number is between 1 and 15")
    diff = input("Put your preferred difficulty grade here: ")

    print("Choose the game mode:")
    print("1: Hard mode (New number generated every turn)")
    print("2: Normal mode (Number remains same until guessed or game over)")
    mode = input("Choose game mode: ")

    print("So shall the game begin!")
    write_to_log("--------------------------------------------------------------")
    sl(1)
    main(diff, mode)

if __name__ == "__main__":
    start()
