# Name: - Neeraj Kumar
# ID: - 2047559
from datetime import date

print("Birthday Calculator")
print("Current day")
month = int(input('Month: '))
day = int(input('Day: '))
year = int(input('Year: '))
currentDay = date(year, month, day)
print('Birthday')
_month = int(input('Month: '))
_day = int(input('Day: '))
_year = int(input('Year: '))
birthday = date(_year, _month, _day)

age =  currentDay.year - birthday.year - \
        ((currentDay.month, currentDay.day) < (birthday.month, birthday.day))

if age:
    print(f'You are {age} years old.')
else:
     print("Happy Birthday!")
