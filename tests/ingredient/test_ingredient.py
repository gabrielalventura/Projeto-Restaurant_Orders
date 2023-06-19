from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


def test_ingredient():
    ingredient = Ingredient("camarão")
    ingredient_restriction = {
            Restriction.ANIMAL_MEAT,
            Restriction.SEAFOOD,
            Restriction.ANIMAL_DERIVED,
        }
    assert ingredient.name == "camarão"
    assert ingredient.restrictions == ingredient_restriction
