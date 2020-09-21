from __future__ import annotations
import json
import random
from typing import Dict, List
from randomizers import BaseRandomizer
from structs import Character, BranchedClass


class SacredStonesCharacter(Character):
    def __init__(self, name: str, base_class: BranchedClass):
        super().__init__(name)

        self.base_class: BranchedClass = base_class
        self.selected_promotion: BranchedClass = None

    def get_final_promotions(self) -> List[BranchedClass]:
        return self.base_class.get_final_promotions()


class MultiTierBranchedClass(BranchedClass):
    def get_final_promotions(self) -> List[MultiTierBranchedClass]:
        if self.has_promotions():
            promotions_list: List[MultiTierBranchedClass] = []

            for promotion in self.promotions:
                promotions_list.extend(promotion.get_final_promotions())

            return list(dict.fromkeys(promotions_list))
        else:
            return [self]


class SacredStonesRandomizer(BaseRandomizer):
    def __init__(self):
        super().__init__(
            num_to_select=10,
            branched_promotions=True
        )

        self._classes: Dict[MultiTierBranchedClass] = {}


    def parse_data(self) -> None:
        with open("data/fe8.json", "r") as f:
            data: dict = json.load(f)

            self.parse_classes(data)
            self.parse_characters(data)
        
        self.add_guaranteed_unit(self._characters["Eirika"])
        self.add_guaranteed_unit(self._characters["Ephraim"])

    def parse_classes(self, data: dict) -> None:
        for classJSON in data["classes"]:
            class_name: str = classJSON["name"]

            if class_name not in self._classes:
                self._classes[class_name] = MultiTierBranchedClass(class_name)
            
            class_obj = self._classes[class_name]

            for promotion_name in classJSON["promotions"]:
                if promotion_name not in self._classes:
                    self._classes[promotion_name] = MultiTierBranchedClass(promotion_name)

                promotion_obj: MultiTierBranchedClass = self._classes[promotion_name]
                class_obj.add_promotion(promotion_obj)

    def parse_characters(self, data: dict) -> None:
        for characterJSON in data["characters"]:
            char_name: str = characterJSON["name"]
            char_class: MultiTierBranchedClass = self._classes[characterJSON["class"]]

            self._characters[char_name] = SacredStonesCharacter(char_name, char_class)


    def randomize_classes(self):
        for unit in self._selected_units:
            final_promotions: List[MultiTierBranchedClass] = unit.get_final_promotions()
            unit.selected_promotion = random.choice(final_promotions)


    def print_selections(self):
        for unit in self._selected_units:
            print(f"{unit.name} - {unit.selected_promotion.name}")
