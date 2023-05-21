from kanren import *
from kanren.constraints import neq
from itertools import combinations
from time import perf_counter
import numpy as np

# representación de los n cubos
# (arriba, frente, derecha, atrás, izquierda, abajo)
cubes_pos = ((2, 3, 1, 1, 1, 4),
             (1, 2, 4, 3, 1, 2),
             (3, 2, 4, 4, 1, 3),
             (2, 1, 4, 3, 2, 3),
             #(6, 1, 2, 3, 4, 5),
             #(6, 1, 2, 3, 4, 5),
             )

# crea los n cubos con variables var() de kanren
def create_cubes(n):
    return tuple(tuple(var() for _ in range(6)) for _ in range(n))

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

def create_24_moves(newCube, baseCube):
    return lany(
        lany(eq(rotateLeft(rotateUp(baseCube, i), j), newCube) for i in range(4) for j in range(4)),
        lany(eq(rotateLeft(rotateUp(rotateLeft(baseCube, i), 1), j), newCube) for i in (1, 3) for j in range(4)),
    )

def create_all_moves(newCubes, baseCubes):
    return lall(
        create_24_moves(newCubes[i], baseCubes[i]) for i in range(len(baseCubes))
    )

# restringe las caras centrales del cubo para que sean diferentes
def differents(cubes):
    tcubes = np.array(cubes).transpose()
    return lall(neq(r1, r2) for faces in tcubes[1:(len(tcubes)-1)] for r1, r2 in combinations(faces, 2))

def solve(newCubes, baseCubes):
    return lall(
        differents(newCubes),
        create_all_moves(newCubes, baseCubes),
    )

cubes = create_cubes(len(cubes_pos))

start = perf_counter()
solutions = run(0, cubes, solve(cubes, cubes_pos))
end = perf_counter()

for i in solutions:
    print(i)

execution_time = (end - start)
print("Soluciones encontradas: ", len(solutions))
print("Tiempo de ejecución: ", execution_time)
