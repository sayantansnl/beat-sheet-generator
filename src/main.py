from outline import slow_print, choose_structure, fill_in_the_beats

def main():
    structure = choose_structure()
    slow_print(f"\nBased on \"{structure["name"]}\", fill in the following beats: \n")
    blueprint = fill_in_the_beats(structure)
    

main()