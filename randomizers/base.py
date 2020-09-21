from typing import Dict, List, Tuple
from structs import Character
import random

class BaseRandomizer:
    def __init__(self):
        self._characters: Dict[Character] = {}

        self._num_to_select = 0
        self._guaranteed_units: List[Character] = []

        self._multiple_promotions: bool = False
        self._marriage: bool = False


    def has_multiple_promotions(self) -> bool:
        return self._branched_promotion

    def can_marry(self) -> bool:
        return self._marriage

    
    def randomize_classes(self, units: List[Character]) -> List[Character]:
        raise NotImplementedError()

    def randomize_pairings(self) -> List[Tuple[Character]]:
        raise NotImplementedError()

    def parse_data(self) -> None:
        raise NotImplementedError()

    def add_guaranteed_unit(self, unit: Character) -> None:
        self._guaranteed_units.append(unit)

    def select_units(self) -> List[Character]:
        selected_units: List[Character] = []
        selected_units.extend(self._guaranteed_units)

        while len(selected_units) - len(self._guaranteed_units) < self._num_to_select:
            unit = random.choice(list(self._characters.values()))
            if unit not in selected_units:
                selected_units.append(unit)

        return selected_units