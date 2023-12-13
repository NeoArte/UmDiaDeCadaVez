label day_2():
    scene black with fade
    "Dia 2 - ([score])"
    scene bg desk happy with fade
    $ version = 1
    $ day_color = week_colors[WeekDay.TWO]

    if version == 1:
        jump .version_1
    elif version == 2:
        jump .version_2
    elif version == 3:
        jump .version_3

label .version_1:
    $ d2_v1_a_repetitions = 0
    "*Sons de Teclado*"
    show diego angry
    diego "Hmmmm… aff outro? Ugh mas que saco…."
    diego -angry "Uuuhh okay chefia…. Tá aqui então…."
    diego -angry @ angry "DROGA! Ah ok vamos de novo então…."
    rat_think "Dono parece estar com dor, com esses sons… ele está preso?"
    menu .v1_m1:
        set menuset_d2
        "[d2_v1_a[0]]":
            label .path_a:
                $ d2_v1_a_repetitions += 1
                if d2_v1_a_repetitions < 5:
                    $ menuset_d2.discard("[d2_v1_a[0]]")
                    if d2_v1_a_repetitions <= 2:
                        "A gaoila balança, *Clack Clack*"
                        rat_speak "Squeak! Squeaaaaaaak!"
                        rat_think "Ei! Tu tá me ignorando?"
                        # rat_think "Hm... talvez eu possa tentar de novo?"
                    elif d2_v1_a_repetitions <= 4:
                        "A gaoila balança ainda mais, *Clack Clack Clack*"
                        rat_speak "Squeak Squeak Squeak!"
                        diego -bravo "Uhh agora não, fica quieto!"
                        rat_think "você tá me ouvindo! Vem cá!"
                    jump .v1_m1
                else:
                    $ menuset_d2.discard("[d2_v1_a[1]]\nRepetições: [d2_v1_a_repetitions]")
                    "A gaoila balança muito mais, *Clack Clack Clack Clack*"
                    rat_think "VEM LOGO"
                    diego angry "AH MEU DEUS OKAY"
                    show rat  at rat_right
                    rat_think "Ufa finalmente!"
                    show rat confused at rat_right
                    rat_think "Vem cá humano o que está-"
                    diego angry "PRONTO TÁ AQUI SUA COMIDA!"
                    show rat sad at rat_right
                    rat_think "Pera que? Não-"
                    diego "E FICA QUIETO!"
                    diego "Pela mor de deus bicho chato!"
                    rat_think "Ah… ele não tá pra conversa… que droga"
                    jump day_3
        "[d2_v1_a[1]]\nRepetições: [d2_v1_a_repetitions]":
            $ menuset_d2.discard("[d2_v1_a[1]]\nRepetições: [d2_v1_a_repetitions]")
            jump .path_a
        "[d2_v1_b[0]]":
            label .path_b:
                $ menuset_d2.discard("[d2_v1_b[1]]")
                rat_think "Meh, ele é esperto, deve se virar, essa luz tá chata vou dormir mais pra dentro"
                diego angry "GAH, chega! Não aguento mais!"
                diego "Ugh, vou pegar algo pra comer"
                diego -angry "E você pequeno como.."
                diego sad "Ah, ele foi dormir… okay"
                jump day_3
        "[d2_v1_b[1]]":
            $ menuset_d2.discard("[d2_v1_b[1]]")
            jump .path_b
        "[d2_v1_c[0]]":
            label .path_c:
                $ menuset_d2.discard("[d2_v1_c[1]]")
                "Clack Clack"
                diego -angry "OPA pera aí!"
                diego laughing "Po menino se você ficar nessa tu cai ein"
                menu .v1_m2:
                    set menuset_d2
                    "[d2_v1_ca[0]]":
                        label .path_ca:
                            $ menuset_d2.discard("[d2_v1_ca[1]]")
                            rat_speak "Squeaaaaaak"
                            diego happy "Ah qual foi? Quer colo?"
                            scene bg diegorat with fade
                            diego "Assim tá melhor?"
                            diego "Ah ok, então pequeno, só rapidinho pra eu terminar aqui"
                            scene bg desk happy with fade
                            diego "Hmm ok onde eu estava mesmo?"
                            jump day_3
                    "[d2_v1_ca[1]]":
                        $ menuset_d2.discard("[d2_v1_ca[1]]")
                        jump .path_ca
                    "[d2_v1_cb[0]]":
                        label .path_cb:
                            diego surprised "AH, mas que!"
                            diego angry "Ei!"
                            diego "Huh bem fica ai então, só não cai denovo!"
                            diego "Bicho louco"
                            show diego laughing
                            jump .v1_m2
                    "[d2_v1_cc[0]]":
                        label .path_cc:
                            $ menuset_d2.discard("[d2_v1_cc[1]]")
                            diego surprised "Ei?!"
                            diego -surprised @ surprised "Huh okay, tá bom então"
                            diego "Huh só vou terminar isso aqui então, vai entender"
                            jump day_3
                    "[d2_v1_cc[1]]":
                        $ menuset_d2.discard("[d2_v1_cc[1]]")
                        jump .path_cc
        "[d2_v1_c[1]]":
            $ menuset_d2.discard("[d2_v1_c[1]]")
            jump .path_c
    return

label .version_2:
    return

label .version_3:
    return
