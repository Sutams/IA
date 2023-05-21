from ortools.sat.python import cp_model as cp

# Desarrollo
model = cp.CpModel()



# Solver
solver = cp.CpSolver()
status = solver.Solve(model)
# Print
if status == cp.OPTIMAL:
    print()
else:
    print('No hay solucion optima')
