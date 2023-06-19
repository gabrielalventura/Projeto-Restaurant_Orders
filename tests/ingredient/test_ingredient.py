from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


def test_ingredient():
    ingredient1 = Ingredient("camarão")
    ingredient2 = Ingredient("caldo de carne")

    ingredient_restriction1 = {
            Restriction.ANIMAL_MEAT,
            Restriction.SEAFOOD,
            Restriction.ANIMAL_DERIVED,
        }
    assert ingredient1.name == "camarão"
    assert ingredient1.restrictions == ingredient_restriction1

    assert repr(ingredient1) == "Ingredient('camarão')"

    assert ingredient1 != ingredient2
    # return repr(self) == repr(other)
