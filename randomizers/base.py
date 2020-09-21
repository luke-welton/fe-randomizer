from typing import Dict, List
from structs import Character
import random


class BaseRandomizer:
    def __init__(self,
        num_to_select: int = 0,
        branched_promotions: bool = False,
        reclassing: bool = False,
        marriage: bool = False
    ):
        self._characters: Dict[Character] = {}

        self._num_to_select = num_to_select
        self._guaranteed_units: List[Character] = []
        self._selected_units: List[Character] = []

        self._branched_promotions: bool = branched_promotions
        self._reclassing: bool = reclassing
        self._marriage: bool = marriage


    def has_multiple_promotions(self) -> bool:
        return self._branched_promotions

    def can_reclass(self) -> bool:
        return self._reclassing

    def can_marry(self) -> bool:
        return self._marriage

    
    def randomize_classes(self) -> None:
        raise NotImplementedError()

    def randomize_pairings(self) -> None:
        raise NotImplementedError()

    def parse_data(self) -> None:
        raise NotImplementedError()


    def add_guaranteed_unit(self, unit: Character) -> None:
        self._guaranteed_units.append(unit)


    def select_units(self) -> None:
        selected_units: List[Character] = []
        selected_units.extend(self._guaranteed_units)

        while len(selected_units) - len(self._guaranteed_units) < self._num_to_select:
            unit = random.choice(list(self._characters.values()))
            if unit not in selected_units:
                selected_units.append(unit)

        self._selected_units = selected_units

    def print_selections(self) -> None:
        for unit in self._selected_units:
            print(unit.name)
