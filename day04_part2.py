import copy

f = open('day04_input.txt', 'r')
a = f.readlines()

for i in range(0, len(a)):
    a[i] = a[i].replace("\n", "")
guesses = a[0].split(",")


boards = []
i = 2
while i < (len(a)-4):
    temp = []
    for j in range(0,5):
        temp2 =  a[i+j].replace("  ", " ").split(" ")
        if "" in temp2:
            temp2.remove("")
        temp = temp + temp2
    i = i + 6
    boards.append(temp)

num = len(boards)
comp = []

for guess in guesses:
    for x in range(0, len(boards)):
        board = boards[x]
        if guess in board:
            # tick new guess off on board
            for i in range(0, len(board)):
                if board[i] == guess:
                    board[i] = "!"
            # check if board meets condition
            # check columns
            for yc in range(0, 5):
                done = True
                for xc in range(0,5):
                    if board[yc + (5*xc)] != "!":
                        done = False
                if done == True:
                    if len(comp) == num - 1:
                        if x not in comp:
                            s = 0
                            for i in board:
                                if i != "!":
                                    s = s + int(i)
                            print(s*int(guess))
                            comp.append(x)
                    else:
                        if x not in comp:
                            comp.append(x)

            # check rows
            for xc in range(0, 5):
                done = True
                for yc in range(0,5):
                    if board[yc + (5*xc)] != "!":
                        done = False
                if done == True:
                    if len(comp) == num - 1:
                        if x not in comp:
                            s = 0
                            for i in board:
                                if i != "!":
                                    s = s + int(i)
                            print(s*int(guess))
                            comp.append(x)
                    else:
                        if x not in comp:
                            comp.append(x)
