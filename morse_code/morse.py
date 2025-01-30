alphabet = dict()
context = 'C:/Users/sergi/OneDrive/Documente/GitHub/Python-CS/morse_code/morse.txt'
mes_encode = 'C:/Users/sergi/OneDrive/Documente/GitHub/Python-CS/morse_code/to_encode.txt'
mes_decode = 'C:/Users/sergi/OneDrive/Documente/GitHub/Python-CS/morse_code/to_decode.txt'

def morse_dict():
    with open(context,'r') as file:
        lines = file.readlines()
        adder = ''
        for n in lines:
            for i in n:
                if i == '-' or i == '.':
                    adder = adder + i
                else:
                    alphabet[n[0]] = adder
                    adder = ''
        alphabet[n[0]] = adder
    return alphabet
            
def decode(alphabet):
    reverse_alphabet = {value: key for key, value in alphabet.items()}
    word = ''
    adder = ''
    missing = 0
    total_len = 0
    succ_words = 0
    avg_len = 0
    v = False
    with open(mes_decode,'r') as file:
        lines = file.readlines()
        for n in lines:
            for i in n:
                if i == '-' or i == '.':
                    adder = adder + i
                else:
                    if adder in reverse_alphabet:
                        word = word + reverse_alphabet[adder]
                    elif adder != '' and adder != ' ' and adder != '\n':
                        v = True
                        missing = missing + 1
                    adder = ''
            if adder in reverse_alphabet:
                word = word + reverse_alphabet[adder]
            if v:
                print(word,'(lost in translation)')
            else:
                print(word)
                total_len = total_len + len(n) - 1
                succ_words = succ_words + 1
            word = ''
    avg_len = total_len/succ_words
    print('STATISTICS for the file:')
    print(f'Characters not found: {missing}')
    print(f'Average length of successfully translated lines: {avg_len}')

def encode(alphabet):
    word = ''
    letter = ''
    missing = 0
    total_len = 0
    succ_words = 0
    avg_len = 0
    v = False
    with open(mes_encode,'r') as file:
        lines = file.readlines()
        for n in lines:
            m = n.lower()
            for i in m:
                if i.isalnum():
                    letter = alphabet[i]
                    word = word + letter + ' '
                elif not i.isspace():
                    v = True
                    missing = missing + 1
            
            if v:  
                print(word,'(lost in translation)')
            else:
                print(word)
                total_len = total_len + len(m) - 1
                succ_words = succ_words + 1
            word = '' 
            avg_len = total_len / succ_words
    print('STATISTICS for the file:')
    print(f'Characters not found: {missing}')
    print(f'Average length of successfully translated lines: {avg_len}')

def main():
    alphabet = morse_dict()
    chore = input('What do we need to do? ')
    if chore[0] == 'd':
        print('The user chose to decode')
        print('\n''TRANSLATION:')
        decode(alphabet)
    if chore[0] == 'e':
        print('\n''The user chose to encode')
        print('\n''TRANSLATION:')
        encode(alphabet)
        
if __name__ == '__main__':
    main()