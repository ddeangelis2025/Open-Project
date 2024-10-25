import random
import time
import os


from colorama import Fore

from data import animals_list,food_list,colors_list,everyday_list,sports_list
active = True
correct = 0
word = ""
new_word = ""
original_word = ""
new_time = 0
start_time = round(time.time(), 1)


def draw_ui(scrambled_word, score):
    width = 50  # Width of the UI

    # Create the top border
    print(Fore.LIGHTBLUE_EX + "┌" + "─" * (width - 2) + "┐")

    # Title section
    print("│" + " " * (width - 2) + "│")
    print("│" + Fore.LIGHTWHITE_EX + " Unscramble Game! ".center(width - 2) + Fore.LIGHTBLUE_EX + "│")
    print("│" + " " * (width - 2) + "│")

    # Display the scrambled word
    print("│" + Fore.LIGHTWHITE_EX + f" Scrambled Word: {scrambled_word} ".center(width + 3) + Fore.LIGHTBLUE_EX + "│")

    # Display score
    print("│" + Fore.LIGHTWHITE_EX + f" Score: {score} ".center(width + 3) + Fore.LIGHTBLUE_EX + "│")

    # Bottom border
    print("│" + " " * (width - 2) + "│")
    print("└" + "─" * (width - 2) + "┘")


class GameMode:
    gamemode_types = {
        "Animals": animals_list,
        "Food": food_list,
        "Everyday Items": everyday_list,
        "Sports": sports_list,
        "Colors": colors_list,
    }

    def __init__(self, mode_name: str):
        if mode_name in self.gamemode_types:
            self.mode_name = mode_name
            self.word_list = self.gamemode_types[mode_name]
        else:
            raise ValueError(f"Invalid game mode: {mode_name}")

    def get_random_word(self):
        return random.choice(self.word_list)





def play_again():
    global start_time
    start_time = 0
    again = input("\nWanna Play Again? (Y/N)").lower()
    if again == "y":
        main()
    elif again == "n":
        print("Thanks for Playing!")
    else:
        play_again()



def enter_word():
    global new_word
    global original_word
    global correct
    global active
    global new_time
    global start_time

    draw_ui(Fore.LIGHTMAGENTA_EX + new_word.lower(), Fore.LIGHTMAGENTA_EX + str(correct))

    answer = input(Fore.LIGHTWHITE_EX + "Answer:").lower()
    new_time = round(time.time(), 1)
    dif = new_time - start_time
    if dif >= 60:
        print("Game Is over!")
        correct = 0
        time.sleep(1)
        play_again()
    else:
        if answer == original_word.lower():
            print(f"Correct!\n")
            correct += 1
            if active:
                word_jumble()
            else:
                time.sleep(1)
                play_again()
        else:
            print(f"Incorrect!\n")
            if active:
                word_jumble()
            else:
                time.sleep(1)
                play_again()



def word_jumble():
    global gamemode
    global word
    global new_word
    global original_word
    word = gamemode.get_random_word()
    original_word = word
    new_word = "".join(random.sample(word, len(word)))
    enter_word()


def mode_selected():
    global start_time
    time.sleep(1)
    print("Ready..")
    time.sleep(1)
    print("Set..")
    time.sleep(1)
    print(f"GO!\n")
    time.sleep(0.5)
    start_time = round(time.time(), 1)
    word_jumble()




def main():
    global gamemode
    print("Unscramble Race!")
    print(f"How to play: You have 1 minute to correctly answer as many scrambled words as possible!\n")
    print("Gamemodes:\nAnimals\nFood\nEveryday Items\nSports\nColors\n")
    mode = input(Fore.WHITE + f"Select a Category! | {Fore.LIGHTBLUE_EX}Animals(1) {Fore.WHITE}| {Fore.BLUE}Food(2) {Fore.WHITE}| {Fore.LIGHTCYAN_EX}Everyday Items(3) {Fore.WHITE}| {Fore.CYAN}Sports(4) {Fore.WHITE}| {Fore.LIGHTBLUE_EX}Colors(5) {Fore.WHITE}|\n>> ")
    modes = {
        "1": "Animals",
        "2": "Food",
        "3": "Everyday Items",
        "4": "Sports",
        "5": "Colors",
    }
    if mode in modes:
        mode_name = modes[mode]
        print(f"{mode_name} Category Selected!")
        gamemode = GameMode(mode_name)
        mode_selected()
    else:
        print("Invalid selection. Reselect Gamemode!")
        main()


main()













