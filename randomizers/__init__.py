from .base import BaseRandomizer
from .fe8 import SacredStonesRandomizer


def get_randomizer(game_name: str) -> BaseRandomizer:
    switch = {
        "fe8": SacredStonesRandomizer()
    }

    return switch.get(game_name, lambda: BaseRandomizer())