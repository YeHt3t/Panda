class character():

    def __init__(link, name, spell, hp=100):
        link.name = name
        link.spell = spell
        link.hp = hp

    def jump(link):
        print(link.name + " is jumping")

    def run(link):
        print(link.name + " is running")

    def prone(link):
        print(link.name + " is proning")

    def shoot(link):
        print(link.name + " is shooting")