from test26 import Shop 

# c1 = Shop("Panda", "sherif")
# c1.buy_sherif()

# c2  = Shop("AuzB0t", "ghost")
# c2.buy_ghost()

# c3 = Shop("CLive", "spell")
# c3.buy_spell()

# c4 = Shop("Eli", "shorty")
# c4.buy_shorty()

name = input("""
             
                    Enter Username 
                           
             """)

choice = input("""
               
                What would you like to buy
        spell     shorty    sheriff   ghost   Classic
         200       300        800      500     free
                       You have 800 creds
               
               """)
if choice == "spell":
    c1 = Shop(name, "spell")
    c1.buy_spell()
if choice == "shorty":
    c2 = Shop(name, "shorty")
    c2.buy_shorty()
if choice == "sheriff":
    c3 = Shop(name, "sheriff")
    c3.buy_sherif()
if choice == "ghost":
    c3 = Shop(name, "ghost")
    c3.buy_ghost()
if choice == "classic":
    c3 = Shop(name, "classic")
    c3.buy_classic()

