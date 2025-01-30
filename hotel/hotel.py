hotel = 'C:/Users/sergi/OneDrive/Documente/GitHub/Python-CS/hotel/hotel.txt'
request = 'C:/Users/sergi/OneDrive/Documente/GitHub/Python-CS/hotel/booking.txt'

def read_file(filename):
    file = open(filename,'r')
    data = file.read()
    return data




def main():
    hotels = read_file(hotel)
    bookings = read_file(request)
    Unrequest = list()
    reservs = 0

# create a dict with all the hotel_ids and their repective free rooms
    adder = ''
    all_rooms = dict()
    s = 0
    for i in hotels:
        if i != ':':
            adder = adder + i
        else:
            s = s + 1
            if s == 1:
                adder = ""
            if s == 2:
                prev_adder = adder
                adder = ""
            if s == 3:
                all_rooms[prev_adder] = adder
                s = 0     

# read all requests and remove number of rooms from hotel
    s = 0
    for i in bookings:
        
        if i != ' ' and i != '\n' and i != '':
            adder = adder + i
            if adder in all_rooms:
                temp_adder = adder
        else:
            s = s + 1
            if s == 1 :
                book_id = adder
            if adder.isnumeric():
                reservs = reservs + 1
                s = 0
                if int(all_rooms[temp_adder]) - int(adder) < 0:
                    all_rooms[temp_adder] = 0
                    Unrequest.append(book_id)
                    book_id = ''
                else:
                    book_id = ''
                    all_rooms[temp_adder] = int(all_rooms[temp_adder]) - int(adder)
            adder = ""

# iterating on the last character
    if adder.isnumeric():
        s = 0
        if int(all_rooms[temp_adder]) - int(adder) < 0:
            all_rooms[temp_adder] = 0
            Unrequest.append(book_id)
            book_id = ''
        else:
            book_id = ''
            all_rooms[temp_adder] = int(all_rooms[temp_adder]) - int(adder)
    adder = ""

    freehotel = dict(sorted(all_rooms.items(), key=lambda item: item[1], reverse=True))
    freehotels = next(iter(freehotel))

    for code in Unrequest:
        print(f"Uncofirmed request: code {code}")
    print(f'confirmed reservations: {reservs}, unconfirmed requests: {len(Unrequest)}')
    print('\n')
    print('Hotel status:')
    for key, value in all_rooms.items():
        print(f"{key}: {value}")
    print('\n')
    print(f"Hotel with most free rooms: {freehotels}")
    


if __name__ == '__main__':
    main()