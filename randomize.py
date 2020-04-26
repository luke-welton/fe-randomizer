from typing import List, Tuple
from os.path import exists
import random
import sys

class Character:
    name: str
    classes: List[str]


def main():
    game_name = get_game_name()
    game_data = read_data(game_name)
    game_chars = parse_data(game_data)
    selected_units = select_units(game_chars, 10)

    for unit in selected_units:
        print(unit)


def get_game_name() -> str:
    game_name: str = ""
    
    if len(sys.argv) < 2:
        game_name = input("Please enter a game entry in fe# format (e.g. fe8):\t")
    else:
        game_name = sys.argv[1]
    
    data_path = "data/" + game_name + ".csv"
    if not exists(data_path):
        print("No data file found for " + game_name)
        exit()
    
    return game_name


def read_data(game_name: str) -> List[List[str]]:
    data: List[List[str]] = []

    game_file = "data/" + game_name + ".csv"
    with open(game_file, "r") as file:
        for line in file:
            data.append(line.strip().split(','))
    
    return data


def parse_data(data: List[List[str]]) -> List[Character]:
    characters: List[Character] = []

    for entry in data:
        unit = Character()
        unit.name = entry[0]

        unit.classes = []
        for i, value in enumerate(entry):
            if i == 0: continue
            unit.classes.append(value)
        
        characters.append(unit)
    
    return characters


def select_units(units: List[Character], num_units: int) -> List[Tuple[str, str]]:
    selected_units: List[Tuple[Character, str]] = []

    for _ in range(num_units):
        selected_unit = random.choice(units)
        selected_class = random.choice(selected_unit.classes)
        selected_units.append((selected_unit.name, selected_class))

    return selected_units


if __name__ == "__main__":
    main()