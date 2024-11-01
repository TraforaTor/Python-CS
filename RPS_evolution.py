import random
import matplotlib.pyplot as plt
import array
player_number = int(input("How many players do you want: "))
rock_number = player_number//3
paper_number = player_number//3
scissors_number = player_number//3
moves = [0,1,2]
step = 0
rounds = array.array('i' , [0])
rock_history = array.array('i' , [0])
paper_history = array.array('i' , [0])
scissors_history = array.array('i' , [0])
rounds.append(step)
rock_history.append(rock_number)
paper_history.append(paper_number)
scissors_history.append(scissors_number)

# Battling
def round(p1,p2):
    if p1 == p2:
        return 0
    elif p1 == 0:
        if p2 == 1:
            return "player2"
        else:
            return "player1"
    elif p1 == 1:
        if p2 == 2:
            return "player2"
        else:
            return "player1"
    elif p1 == 2:
        if p2 == 0:
            return "player2"
        else:
            return "player1"

# Modifying The Counters
def addition(counter1, counter2):
    counter1 += 1
    counter2 -= 1
    return counter1,counter2

# Main
while sum(x > 0 for x in [rock_number, paper_number, scissors_number]) >= 2:
    player1_move = random.choice(moves)
    player2_move = random.choice(moves)
# Remove Choice
    if rock_number == 0 and (0 in moves):
        moves.remove(0)
    if paper_number == 0 and (1 in moves):
        moves.remove(1)
    if scissors_number == 0 and (2 in moves):
        moves.remove(2)
# Player1 Wins
    if round(player1_move,player2_move) == "player1":
        if player1_move == 0:
           rock_number,scissors_number = addition(rock_number,scissors_number)
        elif player1_move == 1:
           paper_number,rock_number = addition(paper_number,rock_number)
        elif player1_move == 2:
           scissors_number,paper_number = addition(scissors_number,paper_number)
# Player2 Wins
    elif round(player1_move,player2_move) == "player2":
        if player2_move == 0:
           rock_number,scissors_number = addition(rock_number,scissors_number)
        elif player2_move == 1:
           paper_number,rock_number = addition(paper_number,rock_number)
        elif player2_move == 2:
           scissors_number,paper_number = addition(scissors_number,paper_number)
    print(rock_number,paper_number,scissors_number)
    rock_history.append(rock_number)
    paper_history.append(paper_number)
    scissors_history.append(scissors_number)
    step += 1
    rounds.append(step)

# Graph
plt.plot(rounds, rock_history, color="#218f29", label = "Rock")
plt.plot(rounds, paper_history, color="#c72cb6", label = "Paper")
plt.plot(rounds, scissors_history, color="blue", label = "Scissors")

# Naming The Axis
plt.xlabel("Rounds")
plt.ylabel("Numbers")

# Display Graph
plt.title("Rock Paper Scissors")
plt.legend()
plt.show()