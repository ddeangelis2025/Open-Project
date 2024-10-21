import random
import time

from colorama import Fore

from data import animals_list,food_list,colors_list,everyday_list,sports_list
active = True
correct = 0
gamemode = None
word = ""
new_word = ""
original_word = ""
new_time = 0
start_time = round(time.time(), 1)





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

    print(Fore.WHITE + f"Score:{Fore.GREEN} {correct}")
    print(Fore.LIGHTWHITE_EX + "Unscramble the Word!")

    print(Fore.LIGHTBLUE_EX + new_word.lower() + Fore.LIGHTWHITE_EX)
    try:
        answer = input("Answer:").lower()
        new_time = round(time.time(), 1)
        dif = new_time - start_time
        if dif >= 60:
            print("Game Is over!")
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
    except Exception:
        answer = 'Your time is over!'
        print(answer)


def word_jumble():
    global gamemode
    global word
    global new_word
    global original_word
    word = random.choice(gamemode)
    new_word = ""
    original_word = word
    for ch in range(len(word)):
        r = random.randint(0, len(word) - 1)
        new_word += word[r]
        word = word.replace(word[r], "", 1)
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
    mode = input(
        Fore.WHITE + f"Select a Category! | {Fore.LIGHTBLUE_EX}Animals(1) {Fore.WHITE}| {Fore.BLUE}Food(2) {Fore.WHITE}| {Fore.LIGHTCYAN_EX}Everyday Items(3) {Fore.WHITE}| {Fore.CYAN}Sports(4) {Fore.WHITE}| {Fore.LIGHTBLUE_EX}Colors(5) {Fore.WHITE}|\n>> ")
    if mode == "1":
        print("Animals Category Selected!")
        gamemode = animals_list
        mode_selected()
    elif mode == "2":
        print("Food Category Selected!")
        gamemode = food_list
        mode_selected()
    elif mode == "3":
        print("Everyday Items Category Selected!")
        gamemode = everyday_list
        mode_selected()
    elif mode == "4":
        print("Sports Category Selected!")
        gamemode = sports_list
        mode_selected()
    elif mode == "5":
        print("Colors Category Selected!")
        gamemode = colors_list
        mode_selected()
    else:
        print("Reselect Gamemode!")
        main()

main()













