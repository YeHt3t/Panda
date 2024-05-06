class Shop():
    
    
    def __init__(self, name, weapon, creds=800):
        self.name = name
        self.weapon = weapon
        self.creds = creds


    def buy_sherif(self):
            print(self.name + " bought a sheriff")
            self.creds -= 800
            print(self.name + " has", self.creds, "creds left")

    def buy_spell(self):
            print(self.name + " bought a spell")
            self.creds -= 200
            print(self.name + " has ", self.creds, " creds left")
    def buy_ghost(self):
            print(self.name + " bought a ghost")
            self.creds -= 500
            print(self.name + " has", self.creds, "creds left")

    def buy_shorty(self):
            print(self.name + " bought a shorty")
            self.creds -= 300
            print(self.name + " has", self.creds, "creds left")

    def buy_classic(self):
            print(self.name + " bought a classic")
            self.creds -= 0
            print(self.name + " has", self.creds, "creds left")





