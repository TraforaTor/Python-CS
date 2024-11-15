#computer_science_peer_review_5
import random
random_integer_list = []
numbers_in_even_places = []
even_numbers = []


#LET'S INITIALIZE THE PROGRAMME AND CREATE A LIST
i = 0
while i <= 9: #why 9, counting from 0 to 9 equals to 10 character
    random_number = random.randint(0, 100)
    random_integer_list.append(random_number)
    i += 1

print(f"A random list has been created, your numbers are: {random_integer_list}")

#STEP I: FINDING NUMBERS AT EVEN INDEXES
for index in range(len(random_integer_list)):
    if index % 2 == 0:
        numbers_in_even_places.append(random_integer_list[index])
print(f"Numbers in even places are as follows: {numbers_in_even_places}")

#STEP II: FINDING THE EVEN NUMBERS IN THE LIST
for num in random_integer_list:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"Even numbers are as follows: {even_numbers}")

#STEP III: SORTING THE LIST IN REVERSE
print(f"The original list in reverse is as follows: {random_integer_list[::-1]}")

#STEP IV: FINDING THE FIRST AND THE LAST ITEM OF THE LIST
print(f"The first item of the list is {random_integer_list[0]} and the last item is {random_integer_list[-1]}")