from __future__ import annotations
from typing import List


class Class:
    def __init__(self, name: str):
        self.name: str = name


class BranchedClass(Class):
    def __init__(self, name: str):
        super().__init__(name)

        self.promotions: List[BranchedClass] = []

    def has_promotions(self) -> bool:
        return len(self.promotions) > 0

    def add_promotion(self, promotion: BranchedClass) -> None:
        self.promotions.append(promotion)

    def get_final_promotions(self) -> List[BranchedClass]:
        if self.has_promotions():
            promotions_list: List[BranchedClass] = []

            for promotion in self.promotions:
                promotions_list.extend(promotion.get_final_promotions())

            return list(dict.fromkeys(promotions_list))
        else:
            return [self]


class Character:
    def __init__(self, name: str):
        self.name: str = name


class ReclassableCharacter(Character):
    def __init__(self, name: str):
        super().__init__(name)

        self.classes: List[Class] = []
    
    def add_class(self, char_class: Class) -> None:
        self.classes.append(char_class)
