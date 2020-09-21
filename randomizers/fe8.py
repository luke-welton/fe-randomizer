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


class SacredStonesRandomizer(BaseRandomizer):
    def __init__(self):
        super().__init__(
            num_to_select=10,
            branched_promotions=True
        )

        self._classes: Dict[BranchedClass] = {}


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
            self._classes[class_name] = BranchedClass(class_name)
        
        for classJSON in data["classes"]:
            class_obj: BranchedClass = self._classes[classJSON["name"]]

            for promotion_str in classJSON["promotions"]:
                promotion: BranchedClass = self._classes[promotion_str]
                class_obj.add_promotion(promotion)

    def parse_characters(self, data: dict) -> None:
        for characterJSON in data["characters"]:
            char_name: str = characterJSON["name"]
            char_class: BranchedClass = self._classes[characterJSON["class"]]

            self._characters[char_name] = SacredStonesCharacter(char_name, char_class)


    def randomize_classes(self):
        for unit in self._selected_units:
            final_promotions: List[BranchedClass] = unit.get_final_promotions()
            unit.selected_promotion = random.choice(final_promotions)


    def print_selections(self):
        for unit in self._selected_units:
            print(f"{unit.name} - {unit.selected_promotion.name}")
