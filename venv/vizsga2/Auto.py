from abc import ABC


class Auto(ABC):
    def __init__(self, auto_number, rendszam, tipus, price):
        self.auto_number = auto_number
        self.rendszam = rendszam
        self.tipus =tipus
        self.price = price
        self.is_booked = False
        self.extras = []

    def book_Auto(self):
        pass

    def unbook_Auto(self):
        pass
