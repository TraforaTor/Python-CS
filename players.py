PLAYER_FILE = 'players.csv'

def playerscore(filename):
    try:
        with open(filename,'r') as file:
            titlu = file.read()
    except OSError:
        titlu = list()
    return titlu

def main():
    filewhatever = PLAYER_FILE
    result = playerscore(filewhatever)
    print(result)

if __name__ == '__main__':
    main()