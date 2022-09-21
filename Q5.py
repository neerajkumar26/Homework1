# Name: - Neeraj Kumar
# ID: - 2047559


total = 0

print ('Davy\'s auto shop services')
print ('Oil change -- $35')
print ('Tire rotation -- $19')
print ('Car wash -- $7')
print ('Car wax -- $12\n')


service1 = ""
service2 = ""

service1 = input('Select first service:')
print()
service2 = input('Select second service:')
print('\n')

services = {'Oil change' : 35, '-': 0, 'Car wash' : 7, 'Car wax' : 12, 'Tire rotation' : 19}

print ('Davy\'s auto shop invoice\n')
if(service1 == '-'):
  print('Service 1: No service')
else:
  print(f'Service 1: {service1}, ${services.get(service1)}')
if(service2 == '-'):
  print('Service 2: No service')
else:
  print(f'Service 2: {service2}, ${services.get(service2)}')

total = services.get(service1) + services.get(service2)
print()
print(f'Total: ${total}')