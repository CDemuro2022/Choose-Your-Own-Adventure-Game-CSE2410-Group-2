import random

# import the colorama module
import colorama
from colorama import Fore

from music_player import *
from GUI.GUI import GUIInstance

colorama.init(convert=True)

def chapter_into_the_unknown():
    if GUIInstance.ask_question("You are on a dirt road. Which way do you want to go left or right?", ["Left", "Right"])==0:
        random.choice(chapter_list)()
    else:
        random.choice(chapter_list)()


def chapter_river():
    if GUIInstance.ask_question("You come to a river, you can walk around it or swim across.", ["Walk", "Swim"])==0:
        # 1. Walk
        if GUIInstance.ask_question("You walked for many miles, ran out of water and remembered that there was a shop far away which supplies water. Do you want to go there?", ["Yes", "No"])==0:
            # 2. Yes
            if GUIInstance.ask_question("You went 10 miles walking and bought 10 liters of drinking water. Do you want to drink the water?", ["Yes", "No"])==0:
                # 3. Yes
                GUIInstance.text_until_enter("You drank 5 liters of water and now you feel refreshed.")
                if GUIInstance.ask_question("Do you want to walk further or go back home?", ["Further", "Home"])==0:
                    # 4. Further
                    game_over("You walked 100 more miles and you WIN the game! \U0001f3c6", win=True)
                else:
                    # 4. Home
                    game_over("A car crashed you and you were rushed to hospital. Although, it was too late by the time you reached the hospital, and you had already died. \U0001F480")

            else:
                # 3. No
                game_over("You died of thirst.\U0001F480")

        else:
            # 2. No
            game_over("You were very de-hydrated and died of thirst when you were walking. \U0001F480")

    else:
        # 1. Swim
        game_over("You swam across the river and were eaten by an aligator \U0001F480")



def chapter_bridge():
    if GUIInstance.ask_question("You come to a bridge, it looks wobbly. Do you want to cross it or do you want to head back?", ["Cross", "Back"])==0:
        # 1. Cross
        chapter_stranger()

    else:
        # 1. Back
        if GUIInstance.ask_question("You go back to the main road. Now you can decide to drive forward or turn left.", ["Forward", "Left"])==0:
            # 2. Forward
            game_over("You drive forward and crash into a tree and die.\U0001F480")
        else:
            # 2. Left
            chapter_lake()


def chapter_stranger():
    if GUIInstance.ask_question("You cross the bridge and meet a stranger, do you talk to them?", ["Yes", "No"])==0:
        # 1. Yes
        if GUIInstance.ask_question("You talk a wizard and he asks you, do you want to be a wizard?", ["Yes", "No"])==0:
            # 2. Yes
            game_over("You bacome a wizard and WIN the game! \U0001f3c6", win=True)
        else:
            # 2. No
            game_over("The stranger was not pleased by you and murdered you. \U0001F480")
    else:
        # 1. No
        game_over("The stranger was not pleased by you and murdered you. \U0001F480")


def chapter_mountain():
    if GUIInstance.ask_question("You reached a mountain. Do you want to climb it?", ["Yes", "No"])==0:
        # 1. Yes
        if GUIInstance.ask_question("You start climbing the mountain. You see a rope bridge ahead. Do you want to cross it?", ["Yes", "No"])==0:
            # 2. Yes
            game_over("You walk on the bridge, but suddenly it collapses. You fall to the ground and die \U0001F480")
        else:
            # 2. No
            if GUIInstance.ask_question("Do you want to continue climbing or go back down?", ["Climb", "Back"])==0:
                # 3. Climb
                game_over("You climb the mountain for many days, and you finally reach the top. You WIN the game! \U0001f3c6", win=True)
            else:
                # 3. Back
                GUIInstance.text_until_enter("You climb down safely.")
                random.choice(chapter_list)()

    else:
        # 1. No
        random.choice(chapter_list)()


def chapter_lake():
    if GUIInstance.ask_question("You turned left and you come to a lake, do you want to swim or go back?", ["Swim", "Back"])==0:
        # 1. Swim
        game_over("You swam across the lake and were eaten by a shark. \U0001F480 ")
    else:
        # 1. Back
        if GUIInstance.ask_question("You go back to the main road. Now you can decide to drive forward or turn left.", ["Forward", "Left"])==0:
            # 2. Forward
            game_over("You died. \U0001F480") # Swapped these two answers around because there is a same question with different answer 
        else:
            # 2. Left
            chapter_tree()


def chapter_tree():
    if GUIInstance.ask_question("You are very hungry and you see a tree with apples, do you want to eat the fruit?", ["Yes", "No"])==0:
        # 1. Yes
        game_over("You ate the fruit but it was poisonous and you died. \U0001F480")
    else:
        # 1. No
        if GUIInstance.ask_question("You are nearly starving to death. Do you want to eat Pears instead of apples?", ["Yes", "No"])==0:
            # 2. Yes
            game_over("You ate the pears but they were poisonous and you died. \U0001F480")
        else: 
            # 2. No
            game_over("You were super hungry and nearly died, but a lovely gentleman gave you some food and you WIN the game! \U0001f3c6", win=True)

#Start of personal story (actually multiple paths, but declared before the function)
def chapter_nightfall():
        answer = GUIInstance.ask_question("You become unsure of your surroundings in the dark", ["Continue to trek\nforward","Look for \nshelter"])
        if answer == 0:
            chance_of_encounter = random.randint(0, 2)
            if chance_of_encounter == 0:
                GUIInstance.text_until_enter("Thorny branches block your way.")
                chapter_guardian()
            if chance_of_encounter == 1:
                GUIInstance.text_until_enter("A figure emerges from the shadows.")
                GUIInstance.text_until_enter("He wants to help you find your way home.")
                GUIInstance.text_until_enter("He then points to a path and says to go this way.")
                GUIInstance.text_until_enter("You turn back to thank him, but he is gone.")
                answer = GUIInstance.ask_question("Do you want to follow the path he pointed to?", ["Yes", "No"])
                if answer == 0:
                    GUIInstance.text_until_enter("You follow the path and it leads you to a camp of a cult indian tribe.")
                    GUIInstance.text_until_enter("You were betrayed!")
                    chapter_guardian()
                elif answer == 1:
                    chance_of_encounter = random.randint(0, 1)
                    if chance_of_encounter == 0:
                        GUIInstance.text_until_enter("You think you are back on the main path.")
                        chapter_into_the_darkness()
                    if chance_of_encounter == 1:
                        GUIInstance.text_until_enter("You have found the main path again!")
                        GUIInstance.text_until_enter("Feeling safe, decide to make camp for the night.")
                        game_over("You wake up and decide to head back home. You WIN the game! \U0001f3c6", win=True)
            if chance_of_encounter == 2:
                GUIInstance.text_until_enter("You found a cave even though you feel lost.")
                chapter_cave()
        elif answer == 1:
            chance_of_encounter = random.randint(0, 1)
            if chance_of_encounter == 0:
                GUIInstance.text_until_enter("You find a small cave.")
                chapter_cave()
            if chance_of_encounter == 1:
                GUIInstance.text_until_enter("while wandering in the dark, you fall into a pit.")
                GUIInstance.text_until_enter("Darkness swallows you whole.")
                game_over("You died. \U0001F480")
    
def chapter_into_the_darkness():
    answer = GUIInstance.ask_question("Now you really feel lost! Hope is fading, but you think you see lights.", ["Follow the\n mystical lights","Rest and meditate\n for guidance","Attempt to navigate\n by the stars","Set up\n a campfire"])
    if answer == 0:
        GUIInstance.text_until_enter("Dancing orbs lead you deeper.")
        chapter_guardian()
    elif answer == 1:
        GUIInstance.text_until_enter("You sit and meditate, but you feel no guidance.")
        chapter_journey_end()
    elif answer == 2:
        GUIInstance.text_until_enter("The heavens offer guidance.")
        GUIInstance.text_until_enter("you casually happen upon a cave.")
        chapter_cave()
    elif answer == 3:
        game_over("you set up and campfire and it comforts you through the night. \U0001f3c6", win=True)

def chapter_guardian():
    GUIInstance.text_until_enter("He who calls himself the guardian of the woods steps forward")
    answer = GUIInstance.ask_question("He seems hostile.", ["Ask for\n help","Run away"])
    if answer == 0:
        chance_of_encounter = random.randint(0, 1)
        if chance_of_encounter == 0:
            GUIInstance.text_until_enter("He leads you to a path that leads you home.")
            game_over("You wake up and decide to head back home. You WIN the game! \U0001f3c6", win=True)
        if chance_of_encounter == 1:
            GUIInstance.text_until_enter("He tells you to turn back and leave.")
            answer = GUIInstance.ask_question("Do you despertly beg to stay?", ["Yes", "No"])
            if answer == 0:
                game_over("He becomes angry and kills you. \U0001F480")
            elif answer == 1:
                GUIInstance.text_until_enter("You stumble upon a cave.")
                chapter_cave()
    elif answer == 1:
        game_over("He becomes angry you decided to retreat without talking and kills you. \U0001F480")
    

def chapter_cave():
    answer = GUIInstance.ask_question("You could stay at the cave for the night or maybe look around", ["Stay and\n rest","explore the\n cave","Follow the sound\n of water"])
    if answer == 0:
        game_over("You wake up and decide to head back home. You WIN the game! \U0001f3c6", win=True)
    elif answer == 1:
        chance_of_encounter = random.randint(0, 1)
        if chance_of_encounter == 0:
            game_over("You find a hidden passage that leads you to a hidden treasure. You WIN the game! \U0001f3c6", win=True)
        if chance_of_encounter == 1:
            game_over("The Cave collapses, and you are trapped for eternity. \U0001F480")
    elif answer == 2:
        chance_of_encounter = random.randint(0, 1)
        if chance_of_encounter == 0:
            GUIInstance.text_until_enter("You follow the river and it leads nowhere.")
            GUIInstance.text_until_enter("You decide rest here for the night.")
            chapter_journey_end()

def chapter_journey_end():
    answer = GUIInstance.ask_question("It is a new day, and you feel:", ["Hopeful","Lost"])
    if answer == 0:
        answer = GUIInstance.ask_question("What will you do with your new hope?", ["Continue \nthe journey","wait for\nrescue"])
        if answer == 0:
            chapter_multiple_paths()
        if answer == 1:
            chance_of_encounter = random.randint(0, 1)
            if chance_of_encounter == 0:
                GUIInstance.text_until_enter("You wait for rescue, but it never comes.")
                game_over("You died. \U0001F480")
            if chance_of_encounter == 1:
                GUIInstance.text_until_enter("You are found by a search party.")
                game_over("You are saved and WIN the game! \U0001f3c6", win=True)
    elif answer == 1:
        answer = GUIInstance.ask_question("What now?", ["Accept \nbeing lost","Embrace the \nwilderness as\n your new home"])
        if answer == 0:
            game_over("You accept being lost and die. \U0001F480")
        if answer == 1:
            game_over("You become one with the wilderness and WIN the game! \U0001f3c6", win=True)

def chapter_multiple_paths():
    answer = GUIInstance.ask_question("You are at the crossroads of hiking in the middle of the woods", ["Follow the main path \ndeeper into the forest.", "Take the overgrown\n trail to the right.", "Explore the underbrush\n to the left","Climb a tree\n for a better view.","Listen for\ndanger","Make camp\n for the night."])
    if answer == 0:
        GUIInstance.text_until_enter("The path winds into darkness.")
        chapter_into_the_darkness()
    elif answer == 1:
        GUIInstance.text_until_enter("Thick foliage obscures your path.")
        chapter_into_the_darkness()
    elif answer == 2:
        GUIInstance.text_until_enter("Strange sounds emanate from the shadows.")
        chance_of_encounter = random.randint(0, 1)
        if chance_of_encounter == 0:
            GUIInstance.text_until_enter("A bear emerges from the underbrush.")
            game_over("The bear mauls you to death. \U0001F480")
        else:
            GUIInstance.text_until_enter("The sun sets and it becomes very dark.")
            chapter_nightfall()
    elif answer == 3:
        GUIInstance.text_until_enter("You see a troop of indians that look dangerous by a fire.")
        chapter_into_the_darkness()
    elif answer == 4:
        GUIInstance.text_until_enter("You hear nothing but the wind in the trees.")
        chapter_into_the_darkness()
    elif answer == 5:
        GUIInstance.text_until_enter("The night wraps around your campsite.")
        chapter_journey_end()


def game_over(message: str = None, *, win=False):
    "Shows Game over message"
    if not GUIInstance.run_gui:
        # No gui
        if win:
            print(Fore.YELLOW + message)
        else:
            print(Fore.RED + message)

    elif message:
        # Gui and message
        GUIInstance.text_until_enter(message)

    if GUIInstance.ask_question("Thanks for playing!", ["Play Again", "Quit"])==0:
        # Play again
        GUIInstance.chapter_directory()
    else:
        # Quit
        GUIInstance.exit_func()


chapter_list = [chapter_multiple_paths, chapter_bridge, chapter_lake, chapter_mountain, chapter_river, chapter_into_the_unknown]
