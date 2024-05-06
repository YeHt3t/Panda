from test28 import Phone

class Smartphone(Phone):

    def __init__(link, brand, model, battery=100):
        super().__init__(brand, model, battery)

    def touch(link):
        print("Scroling")

    def game(link):
        print("Playing Game")