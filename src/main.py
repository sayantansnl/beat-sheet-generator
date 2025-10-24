import time
import sys

from structures import STORY_STRUCTURES

def slow_print(text, delay=0.03):
    # print text with a typewriter effect
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def choose_structure():
    slow_print("\nAvailable Story Structures:\n")
    for structure in STORY_STRUCTURES:
        slow_print(f"{structure["name"]}\n")
    choice = input("\nEnter the name of the structure you'd like to use for your story: ").strip().lower()

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


def main():
    structure = choose_structure()
    slow_print(f"\nBased on \"{structure["name"]}\", fill in the following beats: \n")
    blueprint = fill_in_the_beats(structure)
    

main()