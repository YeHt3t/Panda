import time
from test28 import Phone

class Smartphone(Phone):

    def __init__(link, brand, model, battery=100, games = 0):
        super().__init__(brand, model, battery, games = 0)

    def bat(link):
        while link.battery > 8:
            print("Playing")
            link.battery -= 10
            link.games += 1
            print(" game done", link.battery)
            time.sleep(2)
            if link.battery <= 30:
                print("Low battery")
                break