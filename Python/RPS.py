import random
import matplotlib.pyplot as plt
import array
x = array.array('i' , [0])
y1 = array.array('i' , [0])
y2 = array.array('i' , [0])
y3 = array.array('i' , [0])
step = 0
player1_score = 0
player2_score = 0
moves = ["rock","paper","scissors"]
win = ["rockscissors","scissorspaper","paperrock"]
player1 = input("Name of player 1: ")
player2 = input("Name of player 2: ")
# Getting the result
def results(p1, p2):
    if p1 == p2:
        return 0
    elif p1 + p2 in win:
        return "Player1"
    else:
        return "Player2"

# Getting the score
while step < 1000:
    player1_move = random.choice(moves)
    player2_move = random.choice(moves)
    if results(player1_move, player2_move) == "Player1":
        player1_score += 1
    elif results(player1_move, player2_move) == "Player2":
        player2_score += 1
    print(f"{player1} score is {player1_score} and {player2} score is {player2_score}")
    step += 1
    y1.append(player1_score)
    y2.append(player2_score)
    y3.append(abs(player1_score-player2_score))
    x.append(step)

# Plotting The Values
plt.plot(x, y1, color='#218f29', label = {player1})
plt.plot(x, y2, color='#c72cb6', label = {player2})
plt.plot(x, y3, color='blue', label = "Difference")

# Naming The Axis
plt.xlabel('Rounds')
plt.ylabel('Points')

# Display Graph
plt.title('Scores')
plt.legend()
plt.show()