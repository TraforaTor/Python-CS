PLAYER_FILE = 'players.csv'

def playerscore(filename):
    try:
        with open(filename,'r') as file:
            titlu = file.read()
        return titlu
    except OSError:
        return 'haha'

filewhatever = PLAYER_FILE
result = playerscore(filewhatever)
print(result)