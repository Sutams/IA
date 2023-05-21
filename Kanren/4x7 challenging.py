# https://logic.puzzlebaron.com/play.php?u2=b14f017c8f27e69c5278181ae5adb1fe
# 4x7
# Challenging

from logicpuzzles import *
from time import perf_counter

#Hay siete fechas

date1 = ('may 10th', var(), var(),var())
date2 = ('may 11th', var(), var(),var())
date3 = ('may 12th', var(), var(),var())
date4 = ('may 13th', var(), var(),var())
date5 = ('may 14th', var(), var(),var())
date6 = ('may 15th', var(), var(),var())
date7 = ('may 16th', var(), var(),var())
dates = (date1,date2,date3,date4,date5,date6,date7)

#(date, presenters, topics, institutions)

def datesproblem(dates):
    return lall(

        # 1. Of the sulfur oxide expert and Yolanda, one is from Duke and the other is from Cornell.
        conde((membero((var(),var(),'Sulfur oxide','Duke'),dates),membero((var(),'Yolanda',var(),'Cornell'),dates)),
              (membero((var(),var(),'Sulfur oxide','Cornell'),dates),membero((var(),'Yolanda',var(),'Duke'),dates))),
        
        # 2. Phillip will be either the person from Cornell or the person who will speak on May 15th.
        lany(eq(('may 15th',var(),'Phillip',var()),date6),membero((var(),'Phillip',var(),'Cornell'),dates)),
        # 3. Felipe is from Stanford.
        membero((var(),'Felipe',var(),'Stanford'),dates),
        # 4. The solar energy expert is scheduled sometime after the acid rain expert.
        somewhat_right_of(dates,(var(),var(),'Solar energy',var()),(var(),var(),'Acid rain',var())),
        # 5. The person from Stanford will be either the person who will speak on May 10th or Phillip.
        lany(eq(('may 10th',var(),var(),'Stanford'),date1),membero((var(),'Phillip',var(),'Stanford'),dates)),
        # 6. Carla is scheduled 3 days after Felipe.
        right_of(dates,(var(),'Carla',var(),var()),(var(),'Felipe',var(),var()),3),
        # 7. The wind power expert is scheduled 5 days after Sheri.
        right_of(dates,(var(),var(),'Wind power',var()),(var(),'Sheri',var(),var()),5),
        # 8. Yolanda is scheduled 1 day before Wendy.
        left_of(dates,(var(),'Yolanda',var(),var()),(var(),'Wendy',var(),var())),
        # 9. Phillip is scheduled 1 day after the presenter from Brown.
        right_of(dates,(var(),'Phillip',var(),var()),(var(),var(),var(),'Brown')),
        # 10. The presenter from Ohio State is scheduled 4 days after the nitrogen usage expert.
        right_of(dates,(var(),var(),var(),'Ohio state'),(var(),var(),'Nitrogen usage',var()),4),

        #Datos no mencionados
        membero((var(),'Alexander',var(),var()),dates),
        membero((var(),var(),'Fossil fuels',var()),dates),
        membero((var(),var(),'Global warming',var()),dates),
        membero((var(),var(),var(),'Harvard'),dates),
        membero((var(),var(),var(),'Yale'),dates)
        # membero(var(),var(),var()),

    )

start = perf_counter()

solutions = run(0, dates, datesproblem(dates),
                    # 12. The seven presenters will be Sheri, the person from Cornell, the person from Stanford, the presenter from Yale, the fossil fuels expert, the presenter who will speak on May 13th and the person who will speak on May 16th.
                    differents(dates, (('may 13th','may 16th',),('Sheri',),('Fossil fuels',),('Cornell','Stanford','Yale',))),
                    # 11. The person from Brown won't talk about solar energy.
                    nmembero(dates,('Solar energy', 'Brown'), (2,3))
                )
end = perf_counter()

for i in solutions:
    print("Solution")
    for j in i:
        print(j)

print(f"Soluciones:{len(solutions)}")
execution_time = (end - start)
print("Tiempo de ejecucion: ", execution_time)