from typing import List, Tuple
import random

class Character:
    name: str
    classes: List[str]


def main():
    #TODO: add support for other games
    game_name: str = "fe8"

    game_data = readData(game_name)
    game_chars = parseData(game_data)
    selected_units = select_units(game_chars, 10)

    for unit in selected_units:
        print(unit)

    return


def readData(game_name: str) -> List[List[str]]:
    data: List[List[str]] = []

    game_file = "data/" + game_name + ".csv"
    with open(game_file, "r") as file:
        for line in file:
            data.append(line.strip().split(','))
    
    return data


def parseData(data: List[List[str]]) -> List[Character]:
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