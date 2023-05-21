# https://logic.puzzlebaron.com
# 4x7
# Challenging

# Solución:
# ('January', 'Underwood', 'X-ray', 'Perunia')
# ('February', 'Joyce', 'Alpha', 'Heang')
# ('March', 'Ingram', 'Delta', 'Nyeos')
# ('April', 'Taylor', 'Mike', 'Rothoc')
# ('May', 'Lee', 'Quebec', 'Kimeche')
# ('June', 'Moody', 'Zulu', 'Biage')
# ('July', 'Vincent', 'Charlie', 'Ormmose')
# Tiempo de ejecucion:  118.34562790000018

from logicpuzzles import *
from time import perf_counter

# Hay 7 meses
month1 = ('January', var(), var(), var())
month2 = ('February', var(), var(), var())
month3 = ('March', var(), var(), var())
month4 = ('April', var(), var(), var())
month5 = ('May', var(), var(), var())
month6 = ('June', var(), var(), var())
month7 = ('July', var(), var(), var())
months = (month1, month2, month3, month4, month5, month6, month7)

# desplegamiento(months, commanders, battalions, locations)
def monthsproblem(months):
    return lall(

        # 1. The group deploying to Kimeche is either Quebec Battalion or the battalion led by Commander Ingram
        lany(membero((var(), 'Ingram', var(), 'Kimeche'), months),
             membero((var(), var(), 'Quebec', 'Kimeche'), months)),

        # 2. Of the group deploying to Heang and Quebec Battalion, one is led by Commander Lee and the other will deploy in February.
        conde((eq(('February', var(), var(), 'Heang'), month2), membero((var(), 'Lee', 'Quebec', var()), months)),
              (membero((var(), 'Lee', var(), 'Heang'), months), eq(('February', var(), 'Quebec', var()), month2))),

        # 3. Zulu Battalion is either the group deploying to Heang or the battalion deploying in June.
        lany(eq(('June', var(), 'Zulu', var()), month6),
             membero((var(), var(), 'Zulu', 'Heang'), months)),
        neq(('June', var(), 'Zulu', 'Heang'), month6),

        # 4. Zulu Battalion will deploy 5 months after the group deploying to Perunia.
        right_of(months, (var(), var(), 'Zulu', var()),
                 (var(), var(), var(), 'Perunia'), 5),

        # 7. Quebec Battalion will deploy sometime after the battalion led by Commander Joyce.
        somewhat_right_of(months, (var(), var(), 'Quebec', var()),
                          (var(), 'Joyce', var(), var())),

        # 8. X-ray Battalion will deploy 5 months before the battalion led by Commander Moody.
        left_of(months, (var(), var(), 'X-ray', var()),
                (var(), 'Moody', var(), var()), 5),

        # 10. The battalion deploying in July isn't Alpha Battalion.
        neq(('July', 'Alpha'), (month7[0], month7[2])),
        
        # 12. Mike Battalion will deploy 1 month after Delta Battalion.
        right_of(months, (var(), var(), 'Mike', var()),
                 (var(), var(), 'Delta', var())),

        # 14. The battalion led by Commander Ingram will deploy 2 months after the battalion led by Commander Underwood.
        right_of(months, (var(), 'Ingram', var(), var()),
                 (var(), 'Underwood', var(), var()), 2),

        # 15. The battalion deploying in April is either the battalion led by Commander Lee or the battalion led by Commander Taylor.
        lany(eq(('April', 'Lee', var(), var()), month4),
             eq(('April', 'Taylor', var(), var()), month4)),

        # 16. The group deploying Nyeos is either Charlie Battalion or the battalion deploying in March.
        lany(membero((var(), var(), 'Charlie', 'Nyeos'), months),
             eq(('March', var(), var(), 'Nyeos'), month3)),
        neq(('March', var(), 'Charlie', 'Nyeos'), month3),

        # 17. Datos no mencionados
        membero((var(), 'Vincent', var(), var()), months),
        membero((var(), 'Taylor', var(), var()), months),
        membero((var(), var(), 'Alpha', var()), months),
        membero((var(), var(), 'Charlie', var()), months),
        membero((var(), var(), var(), 'Biage'), months),
        membero((var(), var(), var(), 'Ormmose'), months),
        membero((var(), var(), var(), 'Rothoc'), months)
    )


start = perf_counter()
solutions = run(0, months, monthsproblem(months),

                # 11. The battalion led by Commander Lee, the battalion deploying April, Charlie Battalion,
                # Alpha Battalion, Zulu Battalion and the battalion deploying in March are all different battalions.
                differents(months, (('March', 'April',), ('Lee',),
                                    ('Alpha', 'Charlie', 'Zulu',), (var(),))),

                # 6. The battalion led by Commander Taylor won't deploy to Biage.
                nmembero(months, ('Taylor', 'Biage'), (1, 3)),

                # 9. The group deploying to Ormmose isn't Zulu Battalion.
                nmembero(months, ('Zulu', 'Ormmose'), (2, 3)),

                # 13. The battalion led by Commander Joyce isn't X-ray Battalion.
                nmembero(months, ('Joyce', 'X-ray'), (1, 2)),

                # 5. The battalion led by Commander Lee will deploy sometime before the group deploying to Ormmose.
               somewhat_left_of(months, (var(), 'Lee', var(), var()),
                                   (var(), var(), var(), 'Ormmose')),
                )

end = perf_counter()
for months in solutions:
    print("Solutions:",)
    for month in months:
        print(month)

execution_time = (end - start)
print("Solutions: ", len(solutions))
print("Tiempo de ejecucion: ", execution_time)
