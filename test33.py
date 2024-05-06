import time
class Smartphone():

    def __init__(link, brand, model, battery=100, games = 0):
        link.brand = brand
        link.model = model
        link.battery = battery
        link.games = games

    def bat(link):
        while link.battery > 8:
            print("Playing")
            link.battery -= 10
            link.games += 1
            print(link.games , " game done", link.battery)
            time.sleep(1)
            if link.battery <= 30:
                print("Low battery")
                break
