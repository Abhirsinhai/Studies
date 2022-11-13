import random
import time

#TODO: Fix life system

print("""   
 ______     ______     ______     ______      ______   __  __     ______        __         __     ______     ______  
/\  ___\   /\  __ \   /\  == \   /\__  _\    /\__  _\ /\ \_\ \   /\  ___\      /\ \       /\ \   /\  ___\   /\__  _\ 
\ \___  \  \ \ \/\ \  \ \  __<   \/_/\ \/    \/_/\ \/ \ \  __ \  \ \  __\      \ \ \____  \ \ \  \ \___  \  \/_/\ \/ 
 \/\_____\  \ \_____\  \ \_\ \_\    \ \_\       \ \_\  \ \_\ \_\  \ \_____\     \ \_____\  \ \_\  \/\_____\    \ \_\ 
  \/_____/   \/_____/   \/_/ /_/     \/_/        \/_/   \/_/\/_/   \/_____/      \/_____/   \/_/   \/_____/     \/_/
                                                                                                                    """)
print(
"""
How To Play:
You have to sort the list correctly, if you make a mistake you will loose one live. 
You will have three lives and if you loose all three lives you will loose.
There are three different difficulty levels, there is one custom difficulty that you can customize.
The three different difficulty levels are easy, medium and hard.
""")

lives = 3

def myGameEasy():
    my_list = []
    for i in range(5): 
        my_list.append(random.randint(1,10))
    print(my_list)

    new = []
    for i in range(len(my_list)):
        x = int(input("enter the number: "))
        new.append(x)
        if new[i] != my_list[i]:
            lives = lives - 1
            if lives == 0:
                print("Game over!")
            else:
                print("You lost 1 live, now you have", lives, "lives")
                
def myGameMedium():
    my_list = []
    for i in range(10): 
        my_list.append(random.randint(1,50))
    print(my_list)

    new = []
    for i in range(len(my_list)):
        x = int(input("enter the number: "))
        new.append(x)
        if new[i] != my_list[i]:
            lives = lives - 1
            if lives == 0:
                print("Game over!")
            else:
                print("You lost 1 live, now you have", lives, "lives")

def myGameHard():
    my_list = []
    for i in range(5): 
        my_list.append(random.randint(1,100))
    print(my_list)

    new = []
    for i in range(len(my_list)):
        x = int(input("enter the number: "))
        new.append(x)
        if new[i] != my_list[i]:
            lives = lives - 1
            if lives == 0:
                print("Game over!")
            else:
                print("You lost 1 live, now you have", lives, "lives")

def myGameCustom():
    my_list = []
    for i in range(customListAmount): 
        my_list.append(random.randint(1, customListRange))
    print(my_list)

    new = []
    for i in range(len(my_list)):
        x = int(input("enter the number: "))
        new.append(x)
        if new[i] != my_list[i]:
            lives = lives - 1
            if lives == 0:
                print("Game over!")
            else:
                print("You lost 1 live, now you have", lives, "lives")
                


difficultySelector = input("Please enter the difficulty you want to play. (easy, medium, hard, custom): ")
if difficultySelector == "easy":
    myGameEasy()
elif difficultySelector == "medium":
    myGameMedium()
elif difficultySelector == "hard":
    myGameHard()
elif difficultySelector == "custom":
    customListAmount = int(input("Please enter how many numbers would you like?"))
    customListRange = int(input("Please enter the range of number's you want, 1 to: "))
    myGameCustom()