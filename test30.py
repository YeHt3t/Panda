import time

class Smartphoneif():

    def __init__(self, brand, model, battery=100, games=0):
        self.brand = brand
        self.model = model
        self.battery = battery
        self.games = games

    def game(self):
        print("Playing Game")

        while True:
            if self.battery >= 10:
                self.battery -= 10
                self.games += 1
                print(self.games, " game done")
                print("You have", self.battery, "% left")
                time.sleep(1)

                if self.battery <= 30:
                    print("Low Battery")
                    break


