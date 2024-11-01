a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
print(a+b+c)
print(a-b-c)
print(a*b*c)
print((a+b+c)/3)
print(abs(a-b-c))
if a < b and a < c:
    print('a is the smallest')
if b < a and b < c:
    print('b is the smallest')
if c < b and c < a:
    print('c is the smallest')