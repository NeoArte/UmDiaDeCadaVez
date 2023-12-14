label day_x():
    scene black
    "Dia X - ([score])"
    scene bg room with fade
    $ version = randint(1,2)
    $ day_color = week_colors[WeekDay.ONE]

    if version == 1:
        jump .version_1
    elif version == 2:
        jump .version_2
    elif version == 3:
        jump .version_3

label .version_1:
    menu .v1_m1:
        set menuset_dx
        "[dx_v1_a[0]]":
            label .v1_m1_path_a:
                $ menuset_dx.discard("[dx_v1_a[1]]")
            pass
        "[dx_v1_a[1]]":
            $ menuset_dx.discard("[dx_v1_a[1]]")
            jump .v1_m1_path_a
        "[dx_v1_b[0]]":
            label .v1_m1_path_b:
                $ menuset_dx.discard("[dx_v1_b[1]]")
                pass
        "[dx_v1_b[1]]":
            $ menuset_dx.discard("[dx_v1_b[1]]")
            jump .v1_m1_path_b
        "[dx_v1_c[0]]":
            label .v1_m1_path_c:
                $ menuset_dx.discard("[dx_v1_c[1]]")
                pass
        "[dx_v1_c[1]]":
            $ menuset_dx.discard("[dx_v1_c[1]]")
            jump .v1_m1_path_c
    return

label .version_2:
    return

label .version_3:
    return
