from time import time


class localSearch(object):
    def localSearch(self, problem, search_type, i):
        n_iterations = i
        iter=0
        cnt = 0
        start = time()
        s = []
        result=[]
        for i in range(n_iterations):
            iter+=1
            #print("%%%%%")
            result = search_type(problem)
            #print("#####")
            a=problem.heuristic(result)
            #print(l,a,"----l ,aaa")
            #print(a)
            if a ==0:
                s.append(result)
                break


        print (" - No of Iterations %d \tRuntime: %f" % ( iter, time() - start))
        if len(s)==0:
            s.append(result)

        print(s)
        return s
