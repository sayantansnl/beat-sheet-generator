import time
import sys
import os

from structures import STORY_STRUCTURES

def slow_print(text, delay=0.03):
    # print text with a typewriter effect
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def create_structure():
    structure = {}
    slow_print("\nThe choice for the true auteurs, the ones who like to make their own rules.\n", delay=0.02)
    time.sleep(0.5)

    slow_print("\nWhat would you like to call your story structure?\n")
    name = input("\nEnter the name of your structure: ")
    time.sleep(0.5)

    slow_print("\nCan you tell us a few things about your approach?")
    description = input("\nDescribe your structure in two or three sentences: ")
    time.sleep(0.5)

    slow_print("\nGive us a few examples of movies with unique story structures: ")
    examples = input("\nEnter some examples: ").strip()
    time.sleep(0.5)

    slow_print("\nIt's time to form the beats of your story...")

    beats = []
    while True:
        beat_name = input("\nEnter beat name (Press Enter to stop): ").strip()
        if not beat_name:
            break
        beat_description = input(f'Describe "{beat_name}" in a single sentence: ').strip()
        beats.append((beat_name, beat_description))
    
    structure["name"] = name
    structure["description"] = description
    structure["beats"] = beats
    structure["examples"] = examples

    return structure
    
def choose_structure():
    slow_print("\nAvailable Story Structures:\n")
    for structure in STORY_STRUCTURES:
        slow_print(f"{structure["name"]}\n")
    choice = input("\nEnter the name of the structure you'd like to use for your story (or type \"create\" to create your own): ").strip().lower()

    if choice == "create":
        structure = create_structure()
        slow_print(f'Are you sure you want to use "{structure["name"]}" for your story? ', delay=0.02)
        option = input("y/n: ")
        if option == "Y" or option == "y":
            slow_print(f"\nNice choice. Movies like {structure["examples"]} were written defying the norms of structure.\n")
            return structure
        elif option == "N" or option == "n":
            return choose_structure()

    for structure in STORY_STRUCTURES:
        if choice == structure["name"].lower():
            time.sleep(0.5)
            print()
            slow_print(f"\n{structure["description"]}\n", delay=0.02)
            time.sleep(1)
            print()
            slow_print(f'\nHere are the list of beats that form "{structure["name"]}":\n', delay=0.02)
            time.sleep(0.5)

            for beat in structure["beats"]:
                slow_print(f"{beat[0]} -- {beat[1]}\n", delay=0.02)
                time.sleep(0.4)  # small pause between beats
            
            slow_print(f'Are you sure you want to use "{structure["name"]}" for your story? ', delay=0.02)
            option = input("y/n: ")
            if option == "Y" or option == "y":
                slow_print(f"\nNice choice. Movies like {structure["examples"]} were written using \"{structure["name"]}.\"\n")
                return structure
            elif option == "N" or option == "n":
                return choose_structure()
    
    slow_print("\nStructure not found. Please check your spelling, or the list again. Use './main.sh' in the command line again.\n")
    return None

def fill_in_the_beats(structure):
    title = input("\nEnter the title of your movie: ")
    name = structure["name"]
    beats = {}
    for beat in structure["beats"]:
        beats[beat[0]] = input(f"{beat[0]} -- \n")
    slow_print("\nAnalyzing the beats...\n")
    option = input("\nFinalize the story beats? y/n\n")
    if option == "y" or option == "Y":
        slow_print("\n===== Finalizing the beats =====\n")
        time.sleep(0.5)
        slow_print(f'\nStructure Chosen: {name} for {title}\n')
        slow_print("\nDisplaying the beats:\n")
        for key in beats.keys():
            slow_print(f"{key} -- {beats[key]}\n")
        return {
            "title": title,
            "structure_name": name,
            "beats": beats
        }
    elif option == "n" or option == "N":
        return fill_in_the_beats(structure)