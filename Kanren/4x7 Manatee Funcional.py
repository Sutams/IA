# https://logic.puzzlebaron.com/play.php?u2=c906b2d6569db8b4ddd6b2c8b595d0d8
# 4x7
# Challenging

# Solución:
# (3, 'Foxy Roxy', 'Preston', 'Arnos Spit')
# (4, 'Samantha', 'Romero', 'Hollow Hole')
# (5, 'Sea Cow', 'Quinn', 'Yellow Bend')
# (6, 'Watery Pete', 'Armstrong', 'Betty Beach')
# (7, 'Daily Ray', 'Jacobson', 'Silver springs')
# (8, 'Benny II', 'Espinoza', 'Rainbow Reef')
# (9, 'Mellow Mel', 'Lloyd', 'Treys Tunnel')
# Tiempo de ejecucion:  242.61165150000124
# Tiempo de ejecucion:  229.8732276999981

from logicpuzzles import *
from time import perf_counter

# Hay seis manaties
manatee3 = (3, var(), var(), var())
manatee4 = (4, var(), var(), var())
manatee5 = (5, var(), var(), var())
manatee6 = (6, var(), var(), var())
manatee7 = (7, var(), var(), var())
manatee8 = (8, var(), var(), var())
manatee9 = (9, var(), var(), var())
manatees = (manatee3, manatee4, manatee5,
            manatee6, manatee7, manatee8, manatee9)

# avistamientos(manatees, boats, captains, locations)
def manateesproblem(manatees):
    return lall(

        # 13. The boat that saw 5 manatees is either the Watery Pete or Captain Quinn's vessel.
        lany(eq((5, 'Watery Pete', var(), var()), manatee5),
             eq((5, var(), 'Quinn', var()), manatee5)),
        neq((5, 'Watery Pete', 'Quinn', var()), manatee5),

        # 3. The vessel that went to Hollow Hole is either Captain Romero's vessel or Captain Quinn's boat.
        lany(membero((var(), var(), 'Romero', 'Hollow Hole'), manatees),
             membero((var(), var(), 'Quinn', 'Hollow Hole'), manatees)),

        # 5. Of the vessel that went to Rainbow Reef and the vessel that went to Trey's Tunnel,
        # one was the Mellow Mel and the other was led by Captain Espinoza.
        conde((membero((var(), 'Mellow Mel', var(), 'Rainbow Reef'), manatees), membero((var(), var(), 'Espinoza', 'Treys Tunnel'), manatees)),
              (membero((var(), var(), 'Espinoza', 'Rainbow Reef'), manatees), membero((var(), 'Mellow Mel', var(), 'Treys Tunnel'), manatees))),

        # 11. Of the boat that went to Rainbow Reef and the boat that went to Yellow Bend,
        # one saw 5 manatees and the other was the Benny II.
        conde((eq((5, var(), var(), 'Rainbow Reef'), manatee5), membero((var(), 'Benny II', var(), 'Yellow Bend'), manatees)),
              (membero((var(), 'Benny II', var(), 'Rainbow Reef'), manatees), eq((5, var(), var(), 'Yellow Bend'), manatee5))),

        # 14. Captain Preston's boat saw 4 fewer manatees than the vessel that went to Silver springs.
        left_of(manatees, (var(), var(), 'Preston', var()),
                (var(), var(), var(), 'Silver springs'), 4),

        # 2. The Watery Pete saw 3 fewer manatees than the vessel that went to Trey's Tunnel.
        left_of(manatees, (var(), 'Watery Pete', var(), var()),
                (var(), var(), var(), 'Treys Tunnel'), 3),

        # 4. The Benny II saw 5 more manatees than Captain Preston's vessel.
        right_of(manatees, (var(), 'Benny II', var(), var()),
                 (var(), var(), 'Preston', var()), 5),

        # 6. The vessel that went to Yellow Bend saw 3 fewer manatees than Captain Espinoza's vessel.
        left_of(manatees, (var(), var(), var(), 'Yellow Bend'),
                (var(), var(), 'Espinoza', var()), 3),

        # 9. The vessel that went to Hollow Hole saw 2 fewer manatees than Captain Armstrong's boat.
        left_of(manatees, (var(), var(), var(), 'Hollow Hole'),
                (var(), var(), 'Armstrong', var()), 2),

        # 7. The Samantha saw fewer manatees than Captain Quinn's boat.
        somewhat_left_of(manatees, (var(), 'Samantha', var(), var()),
                         (var(), var(), 'Quinn', var())),

        # 8. Captain Romero's boat saw more manatees than the Foxy Roxy.
        somewhat_right_of(manatees, (var(), var(), 'Romero', var()),
                          (var(), 'Foxy Roxy', var(), var())),

        # 10. The Samantha saw more manatees than the vessel that went to Arno's Spit.
        somewhat_right_of(manatees, (var(), 'Samantha', var(), var()),
                          (var(), var(), var(), 'Arnos Spit')),

        # 16. datos no mencionados
        membero((var(), 'Daily Ray', var(), var()), manatees),
        membero((var(), var(), 'Lloyd', var()), manatees),
        membero((var(), 'Sea Cow', var(), var()), manatees),
        membero((var(), var(), 'Jacobson', var()), manatees),
        membero((var(), var(), var(), 'Betty Beach'), manatees)
    )

start = perf_counter()
solutions = run(0, manatees, manateesproblem(manatees),
                # 1. The Daily Ray wasn't led by Captain Lloyd.
                nmembero(manatees, ('Daily Ray', 'Lloyd'), (1, 2)),

                # 12. The Daily Ray wasn't led by Captain Quinn.
                nmembero(manatees, ('Daily Ray', 'Quinn'), (1, 2)),
                )

end = perf_counter()
for manatees in solutions:
    print("Solutions:",)
    for manatee in manatees:
        print(manatee)

execution_time = (end - start)
print("Solutions: ", len(solutions))
print("Tiempo de ejecucion: ", execution_time)
