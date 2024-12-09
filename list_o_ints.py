# Reading the list string
def integer_list():
    list_of_int = []
    intrare = input("Input a list of integers separated by ':' >> ")
    num = ''
    for i in intrare:
        if i != ':':
            num = num + i
        else:
            list_of_int.append(num)
            num = ''
    list_of_int.append(num)
    return list_of_int

# Turning the list into integers
def turn_list_int(original_list):
    for x in range(len(original_list)):
        original_list[x] = int(original_list[x])
    return original_list

# Removing the min and max from original list
def finding_extremas(original_list):
    list_without_extremas = original_list.copy()
    for j in original_list:
        if j == max(original_list) or j == min(original_list):
            list_without_extremas.remove(j)
    return list_without_extremas

# Removing odd numbers from original list
def finding_evens(original_list):
    list_of_evens = original_list.copy()
    for o in original_list:
        if o%2 == 1:
            list_of_evens.remove(o)
    return list_of_evens

# Removing numbers with more or less than 2 digits from original list
def finding_double(original_list):
    list_of_double = original_list.copy()
    for m in original_list:
        if m <= 9 or m >= 100:
            list_of_double.remove(m)
    return list_of_double

# Printing the lists with : between the numbers
def printing(list_to_print):
    for n in range(len(list_to_print)-1):
        print(list_to_print[n], end=':')
    print(list_to_print[-1])

# 2 points
def main():
    Mylist = turn_list_int(integer_list())
    print("This is the original list >> ", end='')
    printing(Mylist)
    print("This is the list without the max and min of original list >> ", end='')
    printing(finding_extremas(Mylist))
    print("These are the even numbers >> ", end='')
    printing(finding_evens(Mylist))
    print("These are the double digit numbers >> ", end='')
    printing(finding_double(Mylist))

# 2 points
if __name__ == '__main__':
    main()