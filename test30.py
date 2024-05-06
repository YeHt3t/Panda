from test28 import Phone

class Smartphone(Phone):

    def __init__(link, brand, model, battery=100):
        super().__init__(brand, model, battery)

    def touch(link):
        print("Scroling")

    def game(link):
        print("Playing Game")
        while True:
            if link.battery >= 10:
                link.battery -= 10
                print("You have", link.battery, "% left")
            elif link.battery >= 30:
                print("Low Battery")

            else:
                print("Out of battery")
                break
