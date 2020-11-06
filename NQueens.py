from random import choice
from collections import Counter
from random import randrange


class SearchProblem:

    def __init__(self, initial=None):
        pass


    def initial(self):
        pass

    def goal_test(self, state):
        pass

    def heuristic(self, state):
        pass

    def nearStates(self, state):
        pass

    def randomNearState(self, state):
        return choice(self.nearStates(state))

class NQueensSearch(SearchProblem):


    def __init__(self, N):
        self.N = N

    def compute_chessboard(self,queens, n):

        chessboard = [[1 for _ in range(n)] for _ in range(n)]
        for a in range(n):

            chessboard[queens[a][0]][queens[a][1]] = 0

        return chessboard

    def initial(self):
        return list(randrange(self.N) for i in range(self.N))

    def goal_test(self, state):
        a, b, c = (set() for i in range(3))
        for row, col in enumerate(state):
            if col in a or row - col in b or row + col in c:
                return False
            a.add(col)
            b.add(row - col)
            c.add(row + col)
        return True
    def heuristic(self,state):
        flag=0
        for i in state:
            if state[i]!=i:
                flag=1
                break

        if flag==0:
            return 100
        queens=[]
        for i in state:
            queens.append([i,state[i]])


        n=self.N
                # put the queens on the chessboard
        chessboard = self.compute_chessboard(queens, n)



        for (x, y) in queens:

            for i in range(n):
                chessboard[i][y] = 0

            for j in range(n):
                chessboard[x][j] = 0

            for k in range(min(x, n - y)):
                chessboard[x - k][y + k] = 0

            for k in range(min(n - x, y)):
                chessboard[x + k][y - k] = 0

            for k in range(min(n - x, n - y)):
                chessboard[x + k][y + k] = 0

            for k in range(min(n + x, n + y)):
                chessboard[x - k][y - k] = 0

        return sum(map(sum, chessboard))



    def nearStates(self, state):
        near_states = []

        for row in range(self.N):
            for col in range(self.N):
                if col != state[row]:
                    aux = list(state)
                    aux[row] = col
                    near_states.append(list(aux))
        return near_states
