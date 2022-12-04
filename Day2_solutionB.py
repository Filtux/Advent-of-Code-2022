with open("Day2_input.txt") as file:
    input = file.readlines()

player1Score = 0
player2Score = 0

for line in input:

    if line.startswith("A"): #Rock

        player1Score += 1

        if line[-2] == ("X"): #Lose

            player2Score += 3
            player1Score += 6 #For win


        if line[-2] == ("Y"): #Draw

            player2Score += 4 #1 plus 3 for draw
            player1Score += 3

        if line[-2] == ("Z"): #Win

            player2Score += 8 #2 plus 6 for win 

    if line.startswith("B"): #Paper

        player1Score += 2

        if line[-2] == ("X"): #Lose

            player2Score += 1
            player1Score += 6 #For winning


        if line[-2] == ("Y"): #Draw

            player2Score += 5 #2 plus 3 for draw
            player1Score += 3 #For draw

        if line[-2] == ("Z"): #Win

            player2Score += 9 #3 plus 6 for win

    if line.startswith("C"): #Scissors

        player1Score += 3

        if line[-2] == ("X"): #Lose

            player2Score += 2
            player1Score += 6

        if line[-2] == ("Y"): #Draw

            player2Score += 6
            player1Score += 3 #For draw

        if line[-2] == ("Z"): #Win

            player2Score += 7 #1 plus 6 for win

print(player1Score)
print(player2Score)