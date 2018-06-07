def horizontal(size):
    return " ---" * size + " \n"

def vertical(size):
    return "|   " * size + "|\n"

def gameboard ( size ):
    board = """"""
    for i in range(size):
        board += horizontal(size)
        board += vertical(size)
    board += horizontal(size)
    return board

size = int(input("size game board?"))
print(gameboard(size))


