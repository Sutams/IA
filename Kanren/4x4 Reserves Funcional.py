# https://logic.puzzlebaron.com
# 4x4
# Challenging

# Solución:
# (2004, 'Riverside Glen', 'frilled stork', 'Bibb')
# (2006, 'Howard Park', 'box python', 'Chilton')
# (2008, 'Elm Park', 'fig turtle', 'Pickens')
# (2010, 'Wanda Park', 'sandy hare', 'Lamar')
# Tiempo de ejecucion:  0.11071789999914472

from logicpuzzles import *
from time import perf_counter

# Hay cuatro años
year1 = (2004, var(), var(), var())
year2 = (2006, var(), var(), var())
year3 = (2008, var(), var(), var())
year4 = (2010, var(), var(), var())
years = (year1, year2, year3, year4)

# años(years, reserves, animals, counties)
def yearsproblem(years):
    return lall(

        # 1. The reserve in Pickens County was established sometime after the box python's reserve.
        somewhat_right_of(years, (var(), var(), var(), 'Pickens'),
                          (var(), var(), 'box python', var())),

        # # 2. The reserve in Chilton County was established sometime before the sandy hare's reserve.
        somewhat_left_of(years, (var(), var(), var(), 'Chilton'),
                         (var(), var(), 'sandy hare', var())),
        
        # 3. The park in Lamar County is home to the sandy hare.
        membero((var(), var(), 'sandy hare', 'Lamar'), years),

        # 4. The park in Chilton County was established 2 years after Riverside Glen.
        right_of(years, (var(), var(), var(), 'Chilton'),
                 (var(), 'Riverside Glen', var(), var())),

        # 5. The fig turtle's reserve was established 4 years after the frilled stork's reserve.
        right_of(years, (var(), var(), 'fig turtle', var()),
                 (var(), var(), 'frilled stork', var()), 2),

        # 6. Of the box python's reserve and the park established in 2008, one is in Chilton County and the other is Elm Park.
        conde((membero((var(), var(), 'box python', 'Chilton'), years), eq((2008, 'Elm Park', var(), var()), year3)),
              (membero((var(), 'Elm Park', 'box python', var()), years), eq((2008, var(), var(), 'Chilton'), year3))),

        # 7. Datos no mencionados
        membero((var(), 'Howard Park', var(), var()), years),
        membero((var(), 'Wanda Park', var(), var()), years),
        membero((var(), var(), var(), 'Bibb'), years)
    )

start = perf_counter()
solutions = run(0, years, yearsproblem(years),
                # 7. Wanda Park isn't home to the endangered box python
                nmembero(years, ('Wanda Park', 'box python'), (1,2)),
                )

end = perf_counter()
for years in solutions:
    print("Solutions:",)
    for year in years:
        print(year)

execution_time = (end - start)
print("Solutions: ", len(solutions))
print("Tiempo de ejecucion: ", execution_time)
