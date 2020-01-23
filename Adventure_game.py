import time  # import time library
import random  # import random library


def play_again(item, enemy, weapon):  # reestart the game
    again = input("""Do you want to play again?
    1. Yes
    2. No \n """).lower()
    if "1" == again:
        game()
    elif "2" == again:
        print_pause("See you soon brave young.", 2)
    else:
        play_again(item, enemy, weapon)


def print_pause(sentences, timer):  # print a string with a pause
    print(sentences)
    time.sleep(timer)


def intro():  # print a little introduction
    print_pause("Welcome to Adventure game, the game starts soon...", 1)
    print_pause("Loading...", 3)
    print_pause("You are a simple villager, looking for what to eat.", 2)
    print_pause("You see an abandoned castle and you approach that.", 2)


def cave(item, enemy, weapon):  # verify if you can fight with the enemy
    print_pause(f"You are in the cave of {enemy}.", 2)
    choose_right = input("""What will you do to save yourself?
    1. Run away back
    2. Fight \n""").lower()
    if "1" == choose_right:
        print_pause("You turn back and run like crazy.", 2)
        print_pause("You are not brave but you are alive", 2)
        main(item, enemy, weapon)
    elif "2" == choose_right:
        if weapon in item:
            print_pause(f"You have the powerful {weapon}.", 2)
            print_pause(f"You are fighting with the {enemy}, is very"
                        " strong.", 2)
            print_pause(f"it seems that {weapon} is not enough and you are"
                        " crying and praying.", 2)
            print_pause(f"{enemy} approaches you to kill you but {enemy}"
                        "slips with your tears and dies.", 2)
            print_pause("You are a hero, you have saved the village.", 2)
            print_pause("You win the game!!!", 2)
            play_again(item, enemy, weapon)
        else:
            print_pause("You have nothing to face it other than"
                        " your hunger.", 2)
            print_pause(f"the {enemy} has killed you.", 2)
            print_pause("You lose", 2)
            play_again(item, enemy, weapon)
    else:
        cave(item, enemy, weapon)


def prision1(item, weapon):  # add an arm in your item store
    print_pause("You are in a prison of magicians", 2)
    print_pause("you see a corpse with something bright"
                "and you approach that.", 2)
    print_pause(f"it's the {weapon}.", 2)
    print_pause(f"Now you have the {weapon}.", 2)
    item.append(weapon)
    print_pause("It seems that there is not much else to do here,"
                "you go back.", 2)


def prision2():  # print that you don't need other arm
    print_pause("You had been here before, there isn't"
                "much else to do here.", 2)


def main(item, enemy, weapon):  # logic structure of the game
    # to choose to where go
    print_pause("You find yourself in a dark dungeon.", 2)
    print_pause("In front of you are two passageways.", 2)
    response = input("""which one do you choose?
    1. Cave
    2. Prision \n """).lower()
    if "1" == response:
        cave(item, enemy, weapon)
    elif ("2" == response) and weapon not in item:
        prision1(item, weapon)
        main(item, enemy, weapon)
    elif ("2" == response) and weapon in item:
        prision2()
        main(item, enemy, weapon)
    else:
        main(item, enemy, weapon)


def game():  # define some general variables and run the game
    enemy = random.choice(["Dragon", "Demon", "Assasin"])
    item = []
    weapon = random.choice(["Hyper sword", "Magic pencil", "Enchanted bow"])
    intro()
    main(item, enemy, weapon)


game()
