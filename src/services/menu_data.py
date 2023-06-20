import csv
from models.dish import Dish
from models.ingredient import Ingredient

# referencia uso DictReader :
# https://docs.python.org/3/library/csv.html
# Keys utilizadas obtidas em:
# https://github.com/tryber/sd-025-b-restaurant-orders/blob/main/tests/mocks/menu_base_data.csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load_menu_data(source_path)

    def load_menu_data(self, source_path):
        with open(source_path, 'r', newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                dish_name = row["dish"]
                price = float(row["price"])  # float conforme class Dish
                ingredient_name = row["ingredient"]
                amount = int(row["recipe_amount"])  # int conforme class Dish

                dish = self.verify_dish(dish_name, price)
                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, amount)

    def verify_dish(self, dish_name, price):
        found = None

        for dish in self.dishes:
            if dish.name == dish_name:
                found = dish

            if found is not None:
                return found

        add_dish = Dish(dish_name, price)
        self.dishes.add(add_dish)
        return add_dish
