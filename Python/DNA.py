l = input('Input long DNA sequence: ')
s = input('Input short DNA sequence: ')
if s in l :
    print('The short DNA sample is included in the long one')
print('The short string is included in the long one at position ',l.index(s, 0, 20))
print('The short string is included in the long one ' , l.count(s, 0, 20) , 'times')