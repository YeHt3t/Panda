class Shop():
    
    
    def __init__(link, name, weapon, creds=800):
        link.name = name
        link.weapon = weapon
        link.creds = creds


    def buy_sherif(link):
            print(link.name + " bought a sheriff")
            link.creds -= 800
            print(link.name + " has", link.creds, "creds left")

    def buy_spell(link):
            print(link.name + " bought a spell")
            link.creds -= 200
            print(link.name + " has ", link.creds, " creds left")
    def buy_ghost(link):
            print(link.name + " bought a ghost")
            link.creds -= 500
            print(link.name + " has", link.creds, "creds left")

    def buy_shorty(link):
            print(link.name + " bought a shorty")
            link.creds -= 300
            print(link.name + " has", link.creds, "creds left")

    def buy_classic(link):
            print(link.name + " bought a classic")
            link.creds -= 0
            print(link.name + " has", link.creds, "creds left")





