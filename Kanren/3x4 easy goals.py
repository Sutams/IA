# https://logic.puzzlebaron.com/play.php?u2=efc5545e2eea1b2574451394f14a64e1
# 3x4
# Easy

from logicpuzzles import *
from time import perf_counter

# Hay cuatro goles

goal1 = (6, var(), var())
goal2 = (7, var(), var())
goal3 = (8, var(), var())
goal4 = (9, var(), var())
gols = (goal1, goal2, goal3, goal4)

#(goals, players, team)


def goalsproblem(gols):
    return lall(

        # 1.Duran is either the player from the Monsters or the person from the Wolverines.
        lany(membero((var(), 'Duran', 'Monsters'), gols),
             membero((var(), 'Duran', 'Wolverines'), gols)),

        # 2.The player from the Wolverines scored 2 goals more than Nicholson.
        right_of(gols, (var(), var(), 'Wolverines'),
                 (var(), 'Nicholson', var()), 2),

        # 3.Guerra is from the Comets.
        membero((var(), 'Guerra', 'Comets'), gols),

        # 4.Guerra is either the player with 9 goals or the person from the Monsters.
        lany(eq((9, 'Guerra', var()), goal4),
             membero((var(), 'Guerra', 'Monsters'), gols),),

        # 5.Vazquez is from the Wolverines.
        membero((var(), 'Vazquez', 'Wolverines'), gols),

        # Datos no mencionados
        membero((var(), var(), 'Checkers'), gols),
        membero((var(), var(), 'Monsters'), gols)
    )


start = perf_counter()

solutions = run(0, gols, goalsproblem(gols))
end = perf_counter()

for i in solutions:
    print("Solution")
    for j in i:
        print(j)

print(f"Soluciones:{len(solutions)}")
execution_time = (end - start)
print("Tiempo de ejecucion: ", execution_time)
