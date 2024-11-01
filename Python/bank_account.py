s = float(input("Input money"))
s0 = s 
r = 5
t = 0
while (s <= s0 * 2):
    s = s + (s * r / 100)
    t = t + 1
print(t)