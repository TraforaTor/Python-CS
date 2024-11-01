a = b = c = int(1)
for x in range(10):
    a = b
    b = c
    c = a+b
    print(a+b)