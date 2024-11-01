string_input=input("Input your string here: ")
string_upper=""
string_even=""
string_vowel=""
numbers=0
pos=0

#Uppercase characters
for character in string_input:
    if character.isupper() :
        string_upper = string_upper + character
print(string_upper)

#Even characters
for character in string_input[0:len(string_input):2] :
    string_even = string_even + character
print(string_even)

#Vowels to _
for character in string_input:
    if character in ["A","a","A","e","I","i","O","o","U","u"] :
        string_vowel = string_vowel + "_"
    else:
        string_vowel = string_vowel + character
print("The string replaced with vowels is ", string_vowel)

#Number of numbers
for character in string_input:
    if character.isdecimal() :
        numbers=numbers+1
print("There are {numbers} decimal numbers")

#Position of Vowels
for character in string_input:
    if character in ["A","a","A","e","I","i","O","o","U","u"] :
        print("There are vowels in positions: ",pos, end=" ")
    pos=pos+1