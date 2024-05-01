class Shop():
    
    def __init__(link, name, weapon, creds=800):
        link.name = name
        link.weapon = weapon
        link.weapon = creds

    def buy_sherif(link):
        print(link.name + " bought a sherif")
        print(link.name + " has 0 creds left")

    def buy_spell(link):
        print(link.name + " bought a spell")
        print(link.name + " has 300 creds left")

    def buy_ghost(link):
        print(link.name + " bought a ghost")
        print(link.name + " has 200 creds left")

    def buy_shorty(link):
        print(link.name + " bought a shorty")
        print(link.name + " has 500 creds left")



