class Phone():
    def __init__(link, brand, model, battery=100, games = 0):
        link.brand = brand
        link.model = model
        link.battery = battery
        link.games = games

    def camera(link):
        print(link.brand + " is filming. Cha Luck!")

    def call(link):
        print(link.brand + " is calling. kuru kuru, kuru rin!")