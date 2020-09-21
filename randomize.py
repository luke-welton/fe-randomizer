from sys import argv
import randomizers as Randomizer

def main() -> None:
    game_name: str = get_game_name()
    randomizer: Randomizer.BaseRandomizer = get_randomizer(game_name)
    randomizer.parse_data()


def get_randomizer(game_name: str) -> Randomizer.BaseRandomizer:
    switch = {
        "fe8": Randomizer.SacredStonesRandomizer()
    }

    return switch.get(game_name, lambda: Randomizer.BaseRandomizer())


def get_game_name() -> str: 
    game_name: str = ""
    
    if len(argv) < 2:
        game_name = input("Please enter a game entry in fe# format (e.g. fe8):\t")
    else:
        game_name = argv[1]
    
    return game_name

if __name__ == "__main__":
    main()
