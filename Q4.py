import math
# Name: - Neeraj Kumar
# ID: - 2047559



height = float(input('Enter wall height (feet):\n'))
width = float(input('Enter wall width (feet):\n'))
area = float(height * width)
print('Wall area:', int(area), 'square feet')

areaPerGallon = float(1 / 350)
amt_paint = area * areaPerGallon
print('Paint needed:', f'{amt_paint:.2f}', 'gallons')


paintCans = math.ceil(amt_paint)
print(f'Cans needed: {paintCans} can(s)')

inputColor = input('\nChoose a color to paint the wall:\n')

colors = {
   'red': 35,
   'blue': 25,
   'green': 23
}

if inputColor in colors:
  price = colors[inputColor]
  totalPrice = int(price) * paintCans
  print(f'Cost of purchasing {inputColor} paint: ${totalPrice}')
else:
  print('Invalid Color Choice!')