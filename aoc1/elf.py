class Elf:

    food_bag = [0]
    total_calories_carried = 0

    def __init__(self, food_bag):
        self.food_bag = food_bag
        self.sum_up_calories()

    def sum_up_calories(self):
        self.total_calories_carried = sum(self.food_bag)

    def add_food_item(self, food_item):
        self.food_bag.append(food_item)
        self.sum_up_calories()
