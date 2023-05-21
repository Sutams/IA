
from logicpuzzles import *
from time import perf_counter

# time slots (10.15,10.30,10.45,11.00,11.15,11.30,11.45)
# hosts (Jack Jensen, Ken Kirby, Lina Lopez, Maddy Meyer, Nate Nichol, Oda Osborn, Penny Pugh)
# titles (Green Tonight, Late Night, Red Eye Party, Tonight Again, Up Till Two, Variety X, Witching Hour)
# channels (2, 4, 5, 7, 9, 11, 13)

# Hay 6 horarios
time1 = ('10.15', var(), var(), var())
time2 = ('10.30', var(), var(), var())
time3 = ('10.45', var(), var(), var())
time4 = ('11.00', var(), var(), var())
time5 = ('11.15', var(), var(), var())
time6 = ('11.30', var(), var(), var())
time7 = ('11.45', var(), var(), var())

times = (time1, time2, time3, time4, time5, time6, time7)

# time (times, hosts, titles, channels)

def timesproblem(times):
    return lall(

        # 5. El espectáculo que comienza a las 10:15 pm es Tonight Again.
        eq(('10.15', var(), 'Tonight Again', var()), time1),

        # 4. El programa del canal 5 comienza 15 minutos después del programa del canal 4.
        right_of(times, (var(), var(), var(), 5), (var(), var(), var(), 4)),

        # 6. El programa del canal 2 comienza en algún momento antes que el programa del canal 13.
        somewhat_left_of(times, (var(), var(), var(), 2),
                         (var(), var(), var(), 13)),

        # 11. El programa del canal 4 comienza 75 minutos antes del programa del canal 9.
        left_of(times, (var(), var(), var(), 4), (var(), var(), var(), 9), 5),

        # 7. Up Till Two es el programa de Ken Kirby o el programa que comienza a las 10:45 p. m.
        lany(membero((var(), 'Ken Kirby', 'Up Till Two', var()), times),
             eq(('10.45', var(), 'Up Till Two', var()), time3)),

        # 10. El programa de Nate Nichol es Up Till Two o Variety X.
        lany(membero((var(), 'Nate Nichol', 'Up Till Two', var()), times),
             membero((var(), 'Nate Nichol', 'Variety X', var()), times)),

        # 12. El programa que comienza a las 11:30 pm es el programa de Penny Pugh o Green Tonight.
        lany(eq(('11.30', 'Penny Pugh', var(), var()), time6),
             eq(('11.30', var(), 'Green Tonight', var()), time6)),

        # 3. Del programa del canal 4 y el programa que comienza a las 11:15 p. m., 
        # uno es Tonight Again y el otro lo conduce Jack Jensen.
        conde((membero((var(), var(), 'Tonight Again', 4), times), eq(('11.15', 'Jack Jensen', var(), var()), time5)),
              (membero((var(), 'Jack Jensen', var(), 4), times), eq(('11.15', var(), 'Tonight Again', var()), time5))),

        # 8. Del programa que inicia a las 11:00 pm y el programa de Lina Lopez, 
        # uno es Late Night y el otro se transmite por canal 5.
        conde((membero((var(), 'Lina Lopez', 'Late Night', var()), times), eq(('11.00', var(), var(), 5), time4)),
              (membero((var(), 'Lina Lopez', var(), 5), times), eq(('11.00', var(), 'Late Night', var()), time4))),

        # 13. Del programa que comienza a las 11:45 pm y Tonight Again, 
        # uno se transmite por el canal 11 y el otro lo presenta Maddy Meyer.
        conde((membero((var(), 'Maddy Meyer', 'Tonight Again', var()), times), eq(('11.45', var(), var(), 11), time7)),
              (membero((var(), var(), 'Tonight Again', 11), times), eq(('11.45', 'Maddy Meyer', var(), var()), time7))),

        # Otras variables del dominio
        membero((var(), 'Ken Kirby', var(), var()), times),
        membero((var(), 'Oda Osborn', var(), var()), times),
        membero((var(), 'Penny Pugh', var(), var()), times),
        membero((var(), var(), 'Green Tonight', var()), times),
        membero((var(), var(), 'Red Eye Party', var()), times),
        membero((var(), var(), 'Witching Hour', var()), times),
        membero((var(), var(), var(), 7), times),
    )

start = perf_counter()
solutions = run(0, times, timesproblem(times),

                # 1. Green Tonight, el programa del canal 9, el programa de Jack Jensen, 
                # el programa de Nate Nichol y el programa del canal 13 son programas diferentes.
                differents(times, ((var(),), ('Jack Jensen','Nate Nichol',), ('Green Tonight',), (9, 13,))),

                # 2. El programa del canal 2 no es Up Till Two.
                nmembero(times, ('Up Till Two', 2), (2, 3)),

                # 9. El programa de Jack Jensen no es Witching Hour.
                nmembero(times, ('Jack Jensen', 'Witching Hour'), (1, 2)),                
)

print(solutions)

end = perf_counter()
for domain in solutions:
    print("Solutions:",)
    for year in domain:
        print(year)

execution_time = (end - start)
print("Solutions: ", len(solutions))
print("Tiempo de ejecucion: ", execution_time)