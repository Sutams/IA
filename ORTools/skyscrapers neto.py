from ortools.sat.python import cp_model as cp
import numpy as np

values = [(2, 3, 2, 1),  # left
          (4, 1, 3, 2),  # up
          (2, 1, 2, 3),  # right
          (1, 2, 2, 2)   # down
          ]


def solve_skyscrapers(puzzle, n):
    model = cp.CpModel()

    # variables
    skyscrapers = [[model.NewIntVar(1, n, 'x{}{}'.format(i, j)) for j in range(n)] for i in range(n)]

    # constraints
    for value in puzzle[0:2]:
        for row in skyscrapers:
            model.AddAllDifferent(row)
            # for i in range(len(row)-1):
                # if row[i] < row[i+1]:
                #     print("hola")
                # 1<2<3<4
                # 0<1<2<3
                #       i+1
        skyscrapers = np.transpose(skyscrapers)
    skyscrapers = np.transpose(skyscrapers)


    # solver
    solver = cp.CpSolver()
    status = solver.Solve(model)

    # print solution
    if status == cp.OPTIMAL:
        i=0
        print("   ", puzzle[1])
        for row in skyscrapers:
            print("({})".format(puzzle[0][i]),
                  [solver.Value(x) for x in row], 
                  "({})".format(puzzle[2][i])
                  )
            i=i+1
        print("   ", puzzle[3])
    else:
        print('No hay solucion optima')


solve_skyscrapers(values, len(values[0]))
