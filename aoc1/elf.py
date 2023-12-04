from typing import List


class Elf:

    food_bag: List[int] = [0]
    total_calories_carried: int = 0

    def __init__(self, food_bag: [List[int]]) -> None:
        self.food_bag = food_bag
        self.sum_up_calories()

    def sum_up_calories(self):
        self.total_calories_carried = sum(self.food_bag)

    def add_food_item(self, food_item: int):
        self.food_bag.append(food_item)
        self.sum_up_calories()

    def __str__(self):
        return f"Calories carried: {self.total_calories_carried}, food bag: {self.food_bag}"
