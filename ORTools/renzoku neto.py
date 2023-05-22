from ortools.sat.python import cp_model as cp
import numpy as np

# standard solution printer modified to print a matrix
class VarArraySolutionPrinter(cp.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables):
        cp.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for row in self.__variables:
            for v in row:
                print('%i' % (self.Value(v)), end=' ')
            print()
        print()
            
    def solution_count(self):
        return self.__solution_count

# dots that symbol two cells are consecutive, x for rows, y for cols
dotsX = [(0, 0, 0),
         (0, 0, 1),
         (1, 0, 0),
         (0, 1, 0)]

dotsY = [(0, 0, 0, 1),
         (1, 1, 1, 1),
         (0, 1, 0, 0)]

grid = [(0, 4, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0)]

def solve_renzoku(n, dX, dY, grid=None):
    model = cp.CpModel()
    
    tmp = model.NewIntVar(1, 1, '')
    
    if grid is None: grid = np.zeros([n, n])
    
    # keeps grid values and else makes NewIntVars
    mtrx = [[model.NewIntVar(grid[i][j], grid[i][j], 'x({},{})'.format(i, j))
             if grid[i][j] else model.NewIntVar(1, n, 'x({},{})'.format(i, j))
             for j in range(n)] for i in range(n)]

    # row constraints
    for i, row in enumerate(mtrx):
        model.AddAllDifferent(row)
        for j, x in enumerate(row[0:len(row)-1]):
            if dX[i][j] == 1:
                tmpbool = model.NewBoolVar('')
                model.Add(x == row[j+1] + tmp).OnlyEnforceIf(tmpbool)
                model.Add(x == row[j+1] - tmp).OnlyEnforceIf(tmpbool.Not())
            else:
                tmpbool = model.NewBoolVar('')
                model.Add(x != row[j+1] + tmp).OnlyEnforceIf(tmpbool)
                model.Add(x != row[j+1] - tmp).OnlyEnforceIf(tmpbool.Not())
    
    # col constraints
    mtrx = np.transpose(mtrx)
    for i, row in enumerate(mtrx):
        model.AddAllDifferent(row)
        for j, x in enumerate(row[0:len(row)-1]):
            if dY[i][j] == 1:
                tmpbool = model.NewBoolVar('')
                model.Add(x == row[j+1] + tmp).OnlyEnforceIf(tmpbool)
                model.Add(x == row[j+1] - tmp).OnlyEnforceIf(tmpbool.Not())
            else:
                tmpbool = model.NewBoolVar('')
                model.Add(x != row[j+1] + tmp).OnlyEnforceIf(tmpbool)
                model.Add(x != row[j+1] - tmp).OnlyEnforceIf(tmpbool.Not())
    
    # transpose back to normal
    mtrx = np.transpose(mtrx)
    
    # solve and print
    solver = cp.CpSolver()
    solution_printer = VarArraySolutionPrinter(mtrx)
    solver.parameters.enumerate_all_solutions = True
    status = solver.Solve(model, solution_printer)
    print('Status = %s' % solver.StatusName(status))
    print('Number of solutions found: %i' % solution_printer.solution_count())

solve_renzoku(len(dotsX), dotsX, np.transpose(dotsY), grid)

#idx 0 1 2 3
                  # dX
# 0  2 4 1 3     (0, 0, 0)
# 1  4 1 3 2     (0, 0, 1)
# 2  3 2 4 1     (1, 0, 0)
# 3  1 3 2 4     (0, 1, 0)
                            # dY
# 0  2 4 1 3     0 1 0     (0, 0, 0, 1)
# 1  4 1 3 2     0 1 1     (1, 1, 1, 1)
# 2  3 2 4 1     0 1 0     (0, 1, 0, 0)
# 3  1 3 2 4     1 1 0
