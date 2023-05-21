# https://logic.puzzlebaron.com/play.php?u2=4b9292a649a220be1b508422bb6c7317
# 4x6
# Challenging

# Solución:
# (22, 'Alton', 'lawyer', 'skating rink')
# (23, 'Eddie', 'firefighter', 'beach')
# (24, 'Leslie', 'boxer', 'restaurant')
# (25, 'Jesus', 'banker', 'concert')
# (26, 'Sean', 'musician', 'county fair')
# (27, 'Wayne', 'accountant', 'bowling alley')
# Tiempo de ejecucion:  36.77249819999997
# Tiempo de ejecucion:  35.50806340000054

from logicpuzzles import *
from time import perf_counter

# Hay seis personas
person1 = (22, var(), var(), var())
person2 = (23, var(), var(), var())
person3 = (24, var(), var(), var())
person4 = (25, var(), var(), var())
person5 = (26, var(), var(), var())
person6 = (27, var(), var(), var())
people = (person1, person2, person3, person4, person5, person6)

# citas(people, dates, professions, locations)
def peopleproblem(people):
    return lall(
        # 2. The accountant was either Jesus or the 27-year-old.
        lany(membero((var(), 'Jesus', 'accountant', var()), people),
             eq((27, var(), 'accountant', var()), person6)),
        neq((27, 'Jesus', 'accountant', var()), person6),

        # 3. Eddie was older than the lawyer.
        somewhat_right_of(people, (var(), 'Eddie', var(), var()),
                          (var(), var(), 'lawyer', var())),

        # 4. The date that took Kara to the county fair was 2 years older than the boxer.
        right_of(people, (var(), var(), var(), 'county fair'),
                 (var(), var(), 'boxer', var()), 2),

        # 7. Alton took Kara to the skating rink.
        membero((var(), 'Alton', var(), 'skating rink'), people),

        # 8. The man that took Kara to the beach was 2 years younger than Jesus.
        left_of(people, (var(), var(), var(), 'beach'),
                 (var(), 'Jesus', var(), var()), 2),

        # 9. Wayne was older than the gentleman that took Kara to the county fair.
        somewhat_right_of(people, (var(), 'Wayne', var(), var()),
                          (var(), var(), var(), 'county fair')),

        # 10. Eddie was the firefighter.
        membero((var(), 'Eddie', 'firefighter', var()), people),

        # 11. Of Sean and the man that took Kara to the bowling alley, one was the accountant and the other was 26 years old.
        conde((membero((var(), 'Sean', 'accountant', var()), people), eq((26, var(), var(), 'bowling alley'), person5)),
              (eq((26, 'Sean', var(), var()), person5), membero((var(), var(), 'accountant', 'bowling alley'), people))),
        
        # 12. Jesus took Kara to the concert.
        membero((var(), 'Jesus', var(), 'concert'), people),

        # 13 Datos no mencionados
        membero((var(), 'Leslie', var(), var()), people),
        membero((var(), var(), 'banker', var()), people),
        membero((var(), var(), 'musician', var()), people),
        membero((var(), var(), var(), 'restaurant'), people)
    )

start = perf_counter()
solutions = run(0, people, peopleproblem(people),
                # 1. The date that took Kara to the skating rink wasn't the boxer.
                nmembero(people, ('boxer', 'skating rink'), (2, 3)),

                # 5. The gentleman that took Kara to the concert wasn't the musician.
                nmembero(people, ('musician', 'concert'), (2, 3)),

                # 6. Leslie didn't take Kara to the beach.
                nmembero(people, ('Leslie', 'beach'), (1, 3)),
                )
end = perf_counter()

for i in solutions:
    print("Solution")
    for j in i:
        print(j)

execution_time = (end - start)
print("Solutions: ", len(solutions))
print("Tiempo de ejecucion: ", execution_time)
