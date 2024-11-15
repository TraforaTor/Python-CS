import random
Mylist = []
even_index_Mylist = []
even_Mylist = []

#Randomizing list
for i in range(10):
    Mylist.append(random.randint(1,100))
print(f"This is the random list {Mylist}")

#Print even index
for i in range(10):
    if i%2 == 0:
        even_index_Mylist.append(Mylist[i])
print("These are the numbers in the even index: ", *even_index_Mylist)

#Print even numbers
for i in Mylist:
    if i%2 == 0:
        even_Mylist.append(i)
print("The even numbers are:",*even_Mylist)

#Inversing list
Mylist.reverse()
print("This is the inverse of the list:", *Mylist)

#First and last elements
print(f"These are the first and last number of the list: {Mylist[-1]} {Mylist[1]}") # indexes are reversed because the list is also reversed