import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load_menu_data(source_path)
