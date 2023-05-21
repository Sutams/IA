
from logicpuzzles import *
from time import perf_counter

var1 = (50, var(), var(), var())
var2 = (75, var(), var(), var())
var3 = (100, var(), var(), var())
var4 = (125, var(), var(), var())
var5 = (150, var(), var(), var())
var6 = (175, var(), var(), var())
var7 = (200, var(), var(), var())
domain = (var1, var2, var3, var4, var5, var6, var7)
# (riders, employees, section, rides)


def problem(domain):
    return lall(

        # Brett served 50 riders.
        membero((50, 'Brett', var(), var()), domain),

        # Neither the employee who served 125 riders nor the worker who served 175 riders is Ronald.
        neq((125, 'Ronald'), (var4[0], var4[1])),
        neq((175, 'Ronald'), (var6[0], var6[1])),

        # The employee who manages Demon Drop served 25 more riders than the employee who manages The Screamer.
        right_of(domain, (var(), var(), var(), 'Demon Drop'),
                 (var(), var(), var(), 'The Screamer')),

        # The person who manages Demon Drop served 75 fewer riders than the person who works in the blue section.
        left_of(domain, (var(), var(), var(), 'Demon Drop'),
                (var(), var(), 'blue', var()), 3),

        # The worker who served 75 riders doesn't manage Zinjo.
        neq((75, 'Zinjo'), (var2[0], var2[3])),

        # Of Ronald and the employee who served 200 riders, one manages Speed Devil and the other works in the pink section.
        conde((membero((var(), 'Ronald', var(), 'Speed Devil'), domain), eq((200, var(), 'pink', var()), var7)),
              (membero((var(), 'Ronald', 'pink', var()), domain), eq((200, var(), var(), 'Speed Devil'), var7))),
        neq((200,'Ronald','pink','Speed Devil'),var7),

        # Lyle served fewer riders than the person who works in the green section.
        somewhat_left_of(domain, (var(), 'Lyle', var(), var()),
                         (var(), var(), 'green', var())),

        # Nathan served 75 more riders than the person who works in the yellow section.
        right_of(domain, (var(), 'Nathan', var(), var()),
                 (var(), var(), 'yellow', var()), 3),

        # The person who works in the orange section is either the employee who served 75 riders or Fredrick.
        lany(eq((75, var(), 'orange', var()), var2), membero(
            (var(), 'Fredrick', 'orange', var()), domain)),

        # The worker who works in the yellow section served 25 fewer riders than the worker who works in the purple section.
        left_of(domain, (var(), var(), 'yellow', var()),
                (var(), var(), 'purple', var())),

        # Andy served 25 more riders than the employee who manages Agony Alley.
        right_of(domain, (var(), 'Andy', var(), var()),
                 (var(), var(), var(), 'Agony Alley')),

        # The worker who works in the pink section served 50 more riders than the person who works in the yellow section.
        right_of(domain, (var(), var(), 'pink', var()),
                 (var(), var(), 'yellow', var()),2),

        # The person who served 75 riders doesn't manage Loop-D-Loop.
        neq((75, 'Loop-D-Loop'), (var2[0], var2[3])),

        # Datos no mencionados
        membero((var(), 'Fredrick', var(), var()), domain),
        membero((var(), 'Jeremy', var(), var()), domain),
        membero((var(), var(), 'red', var()), domain),
        membero((var(), var(), var(), 'Loop-D-Loop'), domain),
        membero((var(), var(), var(), 'The Breaker'), domain),
        membero((var(), var(), var(), 'Zinjo'), domain),
    )


start = perf_counter()
solutions = run(0, domain, problem(domain),
                # The worker who manages Speed Devil, the person who works in the green section,
                # the employee who served 125 riders and the person who served 175 riders are all different employees.
                differents(domain, ((125, 175,), (var(),),
                                    ('green',), ('Speed Devil',),)),

                # Lyle doesn't manage The Screamer.
                nmembero(domain, ('Lyle', 'The Screamer'), (1, 3)),

                # Jeremy doesn't manage Loop-D-Loop.
                nmembero(domain, ('Jeremy', 'Loop-D-Loop'), (1, 3)),
                )

end = perf_counter()
for domain in solutions:
    print("Solutions:",)
    for year in domain:
        print(year)

execution_time = (end - start)
print("Solutions: ", len(solutions))
print("Tiempo de ejecucion: ", execution_time)
