year = int(input('Enter a year to check leap year :'))
if year % 4 == 0 and year % 400 == 0:
    print(year,' is a leap year.')
    if year % 100 == 0:
        print(year, ' is not a leap yaer')
    else:
        print(year, ' is a leap year')
else:
    print(year ,' is not a leap year')

print(year.__dir__)