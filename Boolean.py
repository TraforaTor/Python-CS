expression = input("Whichever expression you want: ")
lower_alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
list_of_inputs = []
j = False
# Finding the changable inputs
for i in range(len(expression)):
    if expression[i] in lower_alphabet:
        list_of_inputs.append(expression[i])
list_of_inputs = list(dict.fromkeys(list_of_inputs))
list_of_inputs = sorted(list_of_inputs)
list_of_inputs1 = list_of_inputs # Keep a record of letter positions

for j in range(len(list_of_inputs)):
    list_of_inputs[j] = "0"

# Changing output
def changer(m):
    for m in range(len(expression)):
                if expression[m] == "!":
                    if expression[m+1] == 1:
                        expression [m] = 0
                    else:
                        expression [m] = 1

for c in range(1):
    for d in range(1):
        for b in range(1):
            

print(list_of_inputs)