from logicpuzzles import *
from time import perf_counter

length1 = (6, var(), var(), var())
length2 = (8, var(), var(), var())
length3 = (10, var(), var(), var())
length4 = (12, var(), var(), var())
length5 = (14, var(), var(), var())
length6 = (16, var(), var(), var())
length7 = (18, var(), var(), var())
lengths = (length1, length2, length3, length4, length5, length6, length7)
# (lengths, names, prime ministers, grades)


def lengthsproblem(lengths):
    return lall(

        # 1. The presenter who got the A- talked about P.M. Chamberlain.
        membero((var(), var(), 'Chamberlain', 'A-'), lengths),

        # 13. Blake talked about P.M. Atlee.
        membero((var(), 'Blake', 'Atlee', var()), lengths),

        # 3. The presenter who spoke for 16 minutes was either Virgil or the student who got the B+.
        lany(eq((16, 'Virgil', var(), var()), length6),
             eq((16, var(), var(), 'B+'), length6)),

        # 5. Of the presenter who got the A and the student who gave the presentation on P.M. Grey, one was Iris and the other was Anita.
        conde((membero((var(), 'Anita', var(), 'A'), lengths), membero((var(), 'Iris', 'Grey', var()), lengths)),
              (membero((var(), 'Iris', var(), 'A'), lengths), membero((var(), 'Anita', 'Grey', var()), lengths))),

        # 7. Krista spoke 2 minutes less than the presenter who got the B-.
        left_of(lengths, (var(), 'Krista', var(), var()),
                (var(), var(), var(), 'B-')),
        
        # 15. Nichole spoke 4 minutes less than the student who gave the presentation on P.M. Thatcher.
        left_of(lengths, (var(), 'Nichole', var(), var()),
                (var(), var(), 'Thatcher', var()), 2),

        # 9. Iris spoke 8 minutes more than the presenter who gave the presentation on P.M. Eden.
        right_of(lengths, (var(), 'Iris', var(), var()),
                 (var(), var(), 'Eden', var()), 4),

        # 10. The presenter who got the B+ spoke 4 minutes more than the student who gave the presentation on P.M. Atlee.
        right_of(lengths, (var(), var(), var(), 'B+'),
                 (var(), var(), 'Atlee', var()), 2),

        # 2. Virgil spoke for a somewhat longer time than the student who got the B-.
        somewhat_right_of(lengths, (var(), 'Virgil', var(), var()),
                          (var(), var(), var(), 'B-')),

        # 14. Yvonne spoke for a somewhat shorter time than the presenter who got the C+.
        somewhat_left_of(lengths, (var(), 'Yvonne', var(), var()),
                          (var(), var(), var(), 'C+')),

        # 4. Neither Anita nor Yvonne was the presenter who spoke for 12 minutes.
        neq((12, 'Anita'), (length4[0], length4[1])),
        neq((12, 'Yvonne'), (length4[0], length4[1])),

        # 6. The student who spoke for 12 minutes didn't get the C+.
        neq((12, 'C+'), (length4[0], length4[3])),

        # 12. Neither the student who gave the presentation on P.M. Churchill nor the student who spoke for 16 minutes was Yvonne.
        neq((16, 'Yvonne'), (length6[0], length6[1])),
        neq((16, 'Churchill'), (length6[0], length6[2])),

        # Not mentioned
        membero((var(), var(), 'Churchill', var()), lengths),
        membero((var(), var(), 'Disraeli', var()), lengths),
        membero((var(), var(), var(), 'C-'), lengths),
        membero((var(), var(), var(), 'D'), lengths),
    )


start = perf_counter()
solutions = run(0, lengths, lengthsproblem(lengths),

                # 8. The student who got the D didn't talk about P.M. Thatcher.
                nmembero(lengths, ('Thatcher', 'D'), (2, 3)),

                # 11. The seven students were the student who got the A, Anita, the student who gave the presentation on P.M. Thatcher,
                # the student who spoke for 6 minutes, the presenter who spoke for 10 minutes, the student who spoke for 16 minutes and Nichole.
                differents(lengths, ((6, 10, 16,), ('Anita', 'Nichole',), ('Thatcher',), ('A',))),

                # 12. Neither the student who gave the presentation on P.M. Churchill nor the student who spoke for 16 minutes was Yvonne.
                nmembero(lengths, ('Yvonne', 'Churchill'), (1, 2)),
                )

end = perf_counter()
for lengths in solutions:
    print("Solutions:",)
    for length in lengths:
        print(length)

execution_time = (end - start)
print("Solutions: ", len(solutions))
print("Tiempo de ejecucion: ", execution_time)