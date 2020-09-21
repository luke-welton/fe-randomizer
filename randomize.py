from sys import argv
from randomizers import BaseRandomizer as Randomizer, get_randomizer
from typing import List
from structs import Character


def main() -> None:
    game_name: str = get_game_name()
    randomizer: Randomizer = get_randomizer(game_name)

    randomizer.parse_data()
    randomizer.select_units()

    if randomizer.has_multiple_promotions() or randomizer.can_reclass():
        randomizer.randomize_classes()
    
    randomizer.print_selections()


def get_game_name() -> str:
    if len(argv) < 2:
        game_name: str = input("Please enter a game entry in fe# format (e.g. fe8):\t")
    else:
        game_name: str = argv[1]
    
    return game_name


if __name__ == "__main__":
    main()
