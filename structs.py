from __future__ import annotations
from typing import List

class Class:
    def __init__(self, name: str):
        self.name: str = name

class BranchedClass(Class):
    def __init__(self, name):
        super().__init__(name)

        self.promotions: List[Class] = []
        self.selected_promotion = None

    def has_promotions(self) -> bool:
        return len(self.promotions) > 0

    def add_promotion(self, promotion: Class) -> None:
        self.promotions.append(promotion)

class Character:
    def __init__(self, name, char_class=None):
        self.name: str = name
        self.char_class: Class = char_class

class ReclassableCharacter(Character):
    def __init__(self, name, base_class):
        super().__init__(name, base_class)

        self.classes: List[Class] = []
    
    def add_class(self, char_class: Class) -> None:
        self.classes.append(char_class)