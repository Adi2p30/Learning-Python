Sudokuboard = [[4,0,0,0,0,7,0,0,0],
               [0,5,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,8,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,6,7,9,0,0,0,0,0],
               [0,0,0,0,0,0,8,1,0],
               [0,9,1,4,6,3,0,0,0]]

group1 = Sudokuboard[0][0:3],Sudokuboard[1][0:3],Sudokuboard[2][0:3]
group2 = Sudokuboard[0][3:6],Sudokuboard[1][3:6],Sudokuboard[2][3:6]
group3 = Sudokuboard[0][6:9],Sudokuboard[1][6:9],Sudokuboard[2][6:9]
group4 = Sudokuboard[3][0:3],Sudokuboard[4][0:3],Sudokuboard[5][0:3]
group5 = Sudokuboard[3][3:6],Sudokuboard[4][3:6],Sudokuboard[5][3:6]
group6 = Sudokuboard[3][6:9],Sudokuboard[4][6:9],Sudokuboard[5][6:9]
group7 = Sudokuboard[6][0:3],Sudokuboard[7][0:3],Sudokuboard[8][0:3]
group8 = Sudokuboard[6][3:6],Sudokuboard[7][3:6],Sudokuboard[8][3:6]
group9 = Sudokuboard[6][6:9],Sudokuboard[7][6:9],Sudokuboard[8][6:9]

#======================================================================================
for i in range(0,9):
    for j in range(0,9):
        if 0 == Sudokuboard[i][j]:
            Startingpoint = Sudokuboard[i][j]
            break
for i in range(0,9):
    Sudokuboard[i][j] = i
    if