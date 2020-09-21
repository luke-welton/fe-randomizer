from __future__ import annotations
from typing import List

class Class:
    def __init__(self, name: str):
        self.name: str = name
        self.promotions: List[Class] = []

    def has_promotions(self) -> bool:
        return len(self.promotions) > 0

    def add_promotion(self, promotion: Class) -> None:
        self.promotions.append(promotion)


class Character:
    def __init__(self, name, char_class=None):
        self.name: str = name
        self.base_class: Class = char_class
