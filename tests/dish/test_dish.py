from src.models.dish import Dish  # noqa: F401, E261, E501


def test_dish():
    dish1 = Dish("Macarrão com camarão", 32.00)

    assert dish1.name == "Macarrão com camarão"
    assert dish1.price == 32.00

    assert repr(dish1) == "Dish('Macarrão com camarão', R$32.00)"
    # return f"Dish('{self.name}', R${self.price:.2f})"
