def turn_string_to_list(names):
    file_name = ''
    file_list = []
    for title in names:
        if title != ',':
            file_name = file_name + title
        if title == ',':
            file_list.append(file_name)
            file_name = ''
    file_list.append(file_name)
    return file_list

def find_word(file_list, to_find):
    for i in file_list:
        lines_of_file = read_file(i)
        for j in lines_of_file:
            entire_line = j
            temporary_j = j.lower()
            if to_find in temporary_j:
                print(f"{i}: {entire_line}")

def read_file(file_name):
    DIR = "Find_ring/"
    lines = []
    file_path = DIR + file_name + ".txt"
    try:
        file = open(file_path)
        lines = file.readlines()
        file.close()
    except FileNotFoundError:
        print(f'{file_path}.txt doesnt exist')
    except PermissionError:
        print('Permision')
    return lines

def main():
    files = input('Through which files should we look for (separated by coma ","): ')
    word = input('What word would you like to look for: ')
    files_list = turn_string_to_list(files)
    find_word(files_list, word)


if __name__ == '__main__':
    main()