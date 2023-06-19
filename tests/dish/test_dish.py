from models.ingredient import Ingredient
from src.models.dish import Dish  # noqa: F401, E261, E501


def test_dish():
    dish1 = Dish("Macarrão com camarão", 32.00)
    dish2 = Dish("Omelete de queijo", 18.00)
    ingredient1 = Ingredient("camarão")
    dish1.add_ingredient_dependency(ingredient1, 100)

    assert dish1.name == "Macarrão com camarão"
    assert dish1.price == 32.00

    assert repr(dish1) == "Dish('Macarrão com camarão', R$32.00)"
    # return f"Dish('{self.name}', R${self.price:.2f})"

    assert dish1 != dish2
    assert dish2 == Dish("Omelete de queijo", 18.00)
    # return self.__repr__() == other.__repr__()

    assert hash(dish1) == "Dish('Macarrão com camarão', R$32.00)"
    # return hash(self.__repr__())

    assert dish1.recipe == {
        ingredient1: 100
    }
