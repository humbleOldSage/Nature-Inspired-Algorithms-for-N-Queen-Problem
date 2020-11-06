import argparse,textwrap
from printBoard import printBoard
from localSearch import localSearch
from hill_climbing import hill_climbing
from hill_climbing import hc_rand_restart
from simulated_annealing import simulated_annealing
from NQueens import NQueensSearch

###### algorithm numbers#####
# 1  ->  simulated annealing 
# 2  ->  hill climbing with random restart
# 3  ->  hill climbing
# 4  ->  
# 5  ->
#############################

if __name__ == "__main__":

    des= "N-queens using Nature Inspired Algorithms " 
    algos = """1 ->  simualted annealing   |  
      2  ->  hill climbing with random restart |        
       3  ->  hill climbing        """
         
    parser = argparse.ArgumentParser(description =des)
    parser.add_argument("-n", type=int, default=4, help="Size of the board")
    parser.add_argument("-i", type=int, default=10, help="Number of iterations")
    parser.add_argument("-a", type=int, default=10, help=algos,nargs='+',required =True)
    parser.add_argument("--all", type=int, dest='all', action='store',
                        choices=range(0, 2), default=0,
                        help="0 = show one solution | 1 = show all solutions")
   

    args = parser.parse_args()
    test = localSearch()
   
    algorithms = [simulated_annealing ]#, hc_rand_restart, hill_climbing]
    names = ["simulated_annealing","hill_climbing", "hc_random_restart"]

    for i in range(len(algorithms)):
        problem = NQueensSearch(args.n)
        print (names[i])
        result_board = test.localSearch(problem, algorithms[i], args.i)
        del problem
        printBoard(result_board, args.all)
