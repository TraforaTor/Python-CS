number = 1
counter = 0
sum = 0
inp = "placeholder"
while True:
    inp = input("Give me a number: ")
    if inp == "":
        break
    else:
        number = int(inp)
    if counter%2 == 0:
        sum = sum + number
    else:
        sum = sum - number
    counter += 1
print("This is the final sum:" , sum)