print("Welcome to the bet game!\n")
player1points = 0
player2points = 0
rounds = int(input("How many Rounds do you want to play? "))

for i in range(0,rounds):
    player1 = int(input("Player1's Number: "))
    print("    \n"*100)
    player2 = int(input("Player2's Number: "))
    print("    \n" * 100)

    if player1 == player2 + 1:
        print("Player1 has won 2 points!")
        player1points = player1points + 2

    elif player2 == player1 + 1:
        print("Player2 has won 2 points!")
        player2points = player2points + 2

    elif player1 > player2:
        print("Player2 Has won 1 point")
        player2points = player2points + 1

    elif  player1 < player2:
        print("Player1 Has won 1 point\n")
        player1points = player1points + 1

    else:
        print("No one gets a point...")
    print("Player1's points: " + str(player1points) + "\n"
          "Player2's points: " + str(player2points)+ "\n")

if player1points < player2points:
    print("Player2 WINS!!")
elif player1points == player2points:
    print("both Players TIED")
else:
    print("Player1 WINS!!")