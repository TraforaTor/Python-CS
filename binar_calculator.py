n = 1
result = 0
while n != 0:
    n = int(input("Give me a power: "))
    s = 1
    for i in range(n):
        s = s * 2
    result = result + s
print(result)
