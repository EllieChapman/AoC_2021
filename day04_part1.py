f = open('day04_input.txt', 'r')
a = f.readlines()

for i in range(0, len(a)):
    a[i] = a[i].replace("\n", "")
guesses = a[0].split(",")
boards = []
for i in range(2, len(a)-4, 6):
    temp = []
    for j in range(0,5):
        temp +=  a[i+j].replace("  ", " ").lstrip().split(" ")
    boards.append(temp)


def board_check(board):
    for yc in range(0, 5):
        done_x = True
        done_y = True
        for xc in range(0,5):
            if board[yc + (5*xc)] != "!":
                done_x = False
            if board[xc + (5*yc)] != "!":
                done_y = False
        if (done_x or done_y):
            return True
    return False

def sum_board(board, guess):
    s = 0
    for i in board:
        if i != "!":
            s = s + int(i)
    return s*int(guess)

def run_game(guesses, boards):
    for guess in guesses:
        for x in range(0, len(boards)):
            board = boards[x]
            if guess in board:
                # tick new guess off on board
                for i in range(0, len(board)):
                    if board[i] == guess:
                        board[i] = "!"
                # check if board now meets condition
                if board_check(board):
                    return sum_board(board, guess)


# Run game and print value of the winning board
print(run_game(guesses, boards))
