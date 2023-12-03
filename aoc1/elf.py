class Elf:

    food_bag = [0]
    total_calories_carried = 0

    def __init__(self, foodbag):
        self.food_bag = foodbag
        self.sum_up_calories()

    def sum_up_calories(self):
        self.total_calories_carried = sum(self.food_bag)

    def add_food_item(self, fooditem):
        self.food_bag.append(fooditem)
        self.sum_up_calories()
