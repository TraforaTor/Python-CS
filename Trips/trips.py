trips = 'C:/Users/sergi/OneDrive/Documente/GitHub/Python-CS/Trips/trips.txt'
stones = 'C:/Users/sergi/OneDrive/Documente/GitHub/Python-CS/Trips/stones.txt'

# read the files for further use
def read(file_name):
    with open(file_name,"r") as data:
        lines = data.readlines()
    return lines

# define the dictionaries of the trips and stones to be reused in calculations
def dictionary(lines):
    s = 0
    values = list()
    result = dict()
    adder = ''
    key = ''
    for i in lines:
        for n in i:
            if n != '':
                if n == ',' or n == '\n':
                    if s == 0:
                        key = adder
                    else:
                        values.append(adder)
                    s = s + 1
                    adder = ''
                else:
                    adder = adder + n
            else:
                values.append(adder)
        if adder != '\n' and adder != '':
            values.append(adder)     
        result[key] = values  
        values = list()
        adder = ''
        key = ''
        s = 0
    return result

# Calculate the average length of the trips
def length(trips):
    total = 0
    avg_len = 0
    nr = 0
    for val in trips.values():
        total = total + int(val[0])
        nr = nr + 1
    avg_len = total / nr
    return avg_len

# Calculate the total passangers of the trips (could be combined with length())
def passengers(trips):
    total = 0
    for val in trips.values():
        total = total + int(val[1])
    return total

# Find the stones found in the islands visited
def all_stones(trips,stones):
    total_stones = list()
    for key in trips.keys():
        for val in stones[key]:
            total_stones.append(val)
    return total_stones

# Find the repeated stones
def most_stones(all_stones):
    common_stones = list()
    for i in all_stones:
        all_stones.remove(i)
        if i in all_stones:
            common_stones.append(i)
    return common_stones

def main():
    info_trips = dictionary(read(trips))
    info_stones = dictionary(read(stones))
    list_of_stones = all_stones(info_trips,info_stones) # Declare the list of the total stones found to be able to find the repeated ones
    print(f'Average duration of trips: {length(info_trips)}')
    print(f'Total number of passengers: {passengers(info_trips)}')
    print(f'Types of gemstones found: {', '.join(set(list_of_stones))}') # Use join to printf the list in a regular fashion and not as a list
    print(f'The most common types of gemstones: {', ' .join(set(most_stones(list_of_stones)))}')

if __name__ == "__main__":
    main()