hour = int(input('Enter hour :'))
am = 1
pm = 2
pmam = int(input('am (1) or pm (2): '))

new_hours = int(input('How many hours ahead :'))
current_time = hour + new_hours
new_time = current_time - 12
if current_time > 12:
    
    print('New hour :', new_time)
else:
    print('New hour :', new_time)