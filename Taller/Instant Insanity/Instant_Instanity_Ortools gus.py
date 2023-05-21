from ortools.sat.python import cp_model as cp
import numpy as np

# Rota un cubo n veces a la izquierda
def rotateLeft(cube):
    top, front, right, back, left, bottom = cube
    cube = (top, right, back, left, front, bottom)
    return cube

# Rota un cubo n veces hacia arriba
def rotateUp(cube):
    top, front, right, back, left, bottom = cube
    cube = (front, bottom, right, top, left, back)
    return cube

# Genera todas las posiciones posibles de un cubo
def moves(cube):
    for _ in range(4):
        for _ in range(4):
            yield cube
            cube = rotateLeft(cube)
        cube = rotateUp(cube)

    # The two sides remaining
    cube = rotateLeft(cube)
    for _ in range(2):
        cube = rotateUp(cube)
        for _ in range(4):
            yield cube
            cube = rotateLeft(cube)
        cube = rotateUp(cube)

# Representacion de n cubos
# [back,bottom,front,top,left,right]
cube_nets = [(2, 3, 1, 1, 1, 4),
             (1, 2, 4, 3, 1, 2),
             (4, 3, 4, 3, 1, 2),
             (2, 1, 4, 3, 2, 3),
             #  (6, 1, 2, 3, 4, 5),
             #  (6, 1, 2, 3, 4, 5)
             ]

# Se inicializa la lista de posiciones posibles para cada cubo
cubes_pos = []
for i in range(len(cube_nets)):
    cube = []
    for cube_net in moves(cube_nets[i]):
        cube.append(cube_net)
    cubes_pos.append(cube)

# Resolución puzzle
model = cp.CpModel()
raw_vars = [[model.NewIntVar(1, len(cube_nets), 'color({})'.format(
    i)) for i in cube_nets[j]] for j in range(len(cube_nets))]
for i in range(len(raw_vars)):
    model.AddAllowedAssignments(raw_vars[i], cubes_pos[i])
raw_vars = np.transpose(raw_vars)
for row in raw_vars[1:len(raw_vars)-1]:
    model.AddAllDifferent(row)
raw_vars = np.transpose(raw_vars)
solver = cp.CpSolver()
status = solver.Solve(model)

# Se imprime la solucion
print("Solucion:", solver.StatusName(status))
if status == cp.OPTIMAL:
    print('#--------------------#')
    for cube in raw_vars:
        print("|", [solver.Value(x) for x in cube], "|")
    print('#--------------------#')
