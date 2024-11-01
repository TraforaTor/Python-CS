month = int(input('Write the number of the month(1-12): '))
if month in [1, 2, 3]:
    season = 'Winter'
elif month in [4, 5, 6]:
    season = 'Spring'
elif month in [7, 8, 9]:
    season = 'Summer'
elif month in [10, 11, 12]:
    season = 'Fall'
print('The season is: ', season)

day = int(input('Write the number of the day(1-31): '))
if month % 3 == 0 and day >= 21:
    if season == 'Winter':
        season = 'Spring'
    elif season == 'Spring':
        season = 'Summer'
    elif season == 'Summer':
        season = 'Fall'
    else:
        season = 'Winter'
print('The determined season is: ', season)