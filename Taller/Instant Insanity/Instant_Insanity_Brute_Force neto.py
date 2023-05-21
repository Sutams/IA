from itertools import product
from time import perf_counter
import numpy as np

# representación de los n cubos
# (arriba, frente, derecha, atrás, izquierda, abajo)
cubes_pos = ((2, 3, 1, 1, 1, 4),
             (1, 2, 4, 3, 1, 2),
             (4, 3, 4, 3, 1, 2),
             (2, 1, 4, 3, 2, 3),
             #(6, 1, 2, 3, 4, 5),
             #(6, 1, 2, 3, 4, 5),
             )

# rota un cubo n veces a la izquierda
def rotateLeft(cube, n):
    for _ in range(n):
        top, front, right, back, left, bottom = cube
        cube = (top, right, back, left, front, bottom)
    return cube

# rota un cubo n veces hacia arriba
def rotateUp(cube, n):
    for _ in range(n):
        top, front, right, back, left, bottom = cube
        cube = (front, bottom, right, top, left, back)
    return cube

def create_24_moves(cube):
    for i in range(4):
        for j in range(4):
            yield rotateLeft(rotateUp(cube, j), i)
        for k in (1, 3):
            yield rotateLeft(rotateUp(rotateLeft(cube, k), 1), i)

# revisa que las caras centrales del cubo sean diferentes
def checkColors(cubes):
    tcubes = np.array(cubes).transpose()
    for faces in tcubes[1:(len(tcubes)-1)]:
        myset = set(faces)
        if len(myset) != len(faces):
            return False
    print(cubes)

start = perf_counter()
# para agregar un enésimo cubo se agrega al product `create_24_moves(cubes[n]),`
for newCubes in product(create_24_moves(cubes_pos[0]),
                        create_24_moves(cubes_pos[1]),
                        create_24_moves(cubes_pos[2]),
                        create_24_moves(cubes_pos[3])):
    checkColors(newCubes)
end = perf_counter()

execution_time = (end - start)
print("Tiempo de ejecución: ", execution_time)
