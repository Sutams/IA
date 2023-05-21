from ortools.sat.python import cp_model as cp
import numpy as np

# values range from 1 to Σn-1
values = [(7,3,9,1), # X
          (4,3,6,4)] # Y
# values = [(14,23,27,14,27,24,21), # X
#           (16,27,24,18,25,24,20)] # Y

def solve_kakurasu(puzzle, n):
    model = cp.CpModel()
    
    # variables
    kakurasu = [[model.NewBoolVar('x({},{})'.format(i, j)) for j in range(n)] for i in range(n)]
    
    # constraints
    for values in puzzle:
        for i in range(n):
            rowsum = 0
            for j in range(n):
                rowsum = rowsum + (kakurasu[i][j] * (j+1))
            model.Add( rowsum == values[i] )
        kakurasu = np.transpose(kakurasu)
    kakurasu = np.transpose(kakurasu)

    # solver
    solver = cp.CpSolver()
    status = solver.Solve(model)
    
    # print solution
    if status == cp.OPTIMAL:
        i=0
        for row in kakurasu:
            print([solver.Value(x) for x in row], "({})".format(puzzle[1][i]))
            i=i+1
        print(puzzle[0])
    else:
        print('No hay solucion optima')

solve_kakurasu(values, len(values[0]))