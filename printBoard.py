from random import choice


def printer(r):
    board = []
    for col in r:
        line = ['.'] * len(r)
        line[col] = 'Q'
        board.append(str().join(line))
    charlist = list(map(list, board))      

def printBoard(result, param):

    if not result:
        print("No Board Found for given the algorithm and alloted parameters")
    
    
    if param == 0 :
        r = choice(result)
        printer(r)

        
        for line in charlist:
            print (" ".join(line))

    else:
        for r in result:
            printer(r)

        for i in range(0, len(charlist)):
            if i % len(charlist[i]) == 0:
                print ("\n")

            print(" ".join(charlist[i]))

    print ("\n")
