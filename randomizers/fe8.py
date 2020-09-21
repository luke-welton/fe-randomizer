import json
import random
from typing import Dict
from randomizers import BaseRandomizer
from structs import Character, BranchedClass


class SacredStonesRandomizer(BaseRandomizer):
    def __init__(self):
        super().__init__()

        self._num_to_select = 10
        self._branched_promotions = True

        self._classes: Dict[Class] = {}


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
            char_class: Class = self._classes[characterJSON["class"]]

            self._characters[char_name] = Character(char_name, char_class)


    def randomize_classes(self):
        for selected_unit in self._selected_units:
            current_class: BranchedClass = selected_unit.char_class

            while current_class.has_promotions():
                current_class.selected_promotion = random.choice(current_class.promotions)
                current_class = current_class.selected_promotion


    def print_selections(self):
        for unit in self._selected_units:
            unit_class: BranchedClass = unit.char_class
            while (unit_class.has_promotions()):
                unit_class = unit_class.selected_promotion
            
            print(f"{unit.name} - {unit_class.name}")