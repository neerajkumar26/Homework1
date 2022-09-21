# Name: - Neeraj Kumar
# ID: - 2047559

amtLemon = float(input('Enter amount of lemon juice (in cups):\n'))
amtWater = float(input('Enter amount of water (in cups):\n'))
amtAgave = float(input('Enter amount of agave nectar (in cups):\n'))
amtservings = float(input('How many servings does this make?\n'))

print()
print ('Lemonade ingredients - yields',f"{amtservings:.2f}",'servings')
print (f'{amtLemon:.2f}','cup(s) lemon juice')
print (f'{amtWater:.2f}','cup(s) water')
print (f'{amtAgave:.2f}','cup(s) agave nectar')

totalAmt = float(input('\nHow many servings would you like to make?\n'))
totalServeAmt = (totalAmt / amtservings)
totalLemonAmt = (totalServeAmt * amtLemon)
totalWaterAmt = (totalServeAmt * amtWater)
totalAgaveAmt = (totalServeAmt * amtAgave)

print()
print ('Lemonade ingredients - yields',f'{totalAmt:.2f}','servings')
print (f'{totalLemonAmt:.2f}','cup(s) lemon juice')
print (f'{totalWaterAmt:.2f}','cup(s) water')
print (f'{totalAgaveAmt:.2f}','cup(s) agave nectar')

galon = 16.0
totalLemonAmtgalon = (totalLemonAmt / galon)
totalWaterAmtgalon = (totalWaterAmt / galon)
totalAgaveAmtgalon = (totalAgaveAmt / galon)

print()
print ('Lemonade ingredients - yields',f'{totalAmt:.2f}','servings')
print (f'{totalLemonAmtgalon:.2f}','gallon(s) lemon juice')
print (f'{totalWaterAmtgalon:.2f}','gallon(s) water')
print (f'{totalAgaveAmtgalon:.2f}','gallon(s) agave nectar')