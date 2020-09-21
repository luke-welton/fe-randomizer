from sys import argv
from randomizers import BaseRandomizer as Randomizer, get_randomizer
from typing import List
from structs import Character

def main() -> None:
    game_name: str = get_game_name()
    randomizer: Randomizer = get_randomizer(game_name)

    randomizer.parse_data()
    selected_units: List[Character] = randomizer.select_units()

    for unit in selected_units:
        print(unit.name)


def get_game_name() -> str: 
    game_name: str = ""
    
    if len(argv) < 2:
        game_name = input("Please enter a game entry in fe# format (e.g. fe8):\t")
    else:
        game_name = argv[1]
    
    return game_name

if __name__ == "__main__":
    main()
