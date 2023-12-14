label day_2():
    scene black with fade
    "Dia 2 - ([score])"
    scene bg desk open with fade
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
                    $ score -= 3
                    jump day_3
        "[d2_v1_a[1]]\nRepetições: [d2_v1_a_repetitions]":
            $ menuset_d2.discard("[d2_v1_a[1]]\nRepetições: [d2_v1_a_repetitions]")
            jump .v1_m1_path_a
        "[d2_v1_b[0]]":
            label .v1_m1_path_b:
                $ menuset_d2.discard("[d2_v1_b[1]]")
                rat_think "Meh, ele é esperto, deve se virar, essa luz tá chata vou dormir mais pra dentro"
                diego angry "GAH, chega! Não aguento mais!"
                diego "Ugh, vou pegar algo pra comer"
                diego -angry "E você pequeno como.."
                diego sad "Ah, ele foi dormir… okay"
                jump day_3
        "[d2_v1_b[1]]":
            $ menuset_d2.discard("[d2_v1_b[1]]")
            jump .v1_m1_path_b
        "[d2_v1_c[0]]":
            label .v1_m1_path_c:
                $ menuset_d2.discard("[d2_v1_c[1]]")
                "Clack Clack"
                diego -angry "OPA pera aí!"
                diego laughing "Po menino se você ficar nessa tu cai ein"
                menu .v1_m2:
                    set menuset_d2
                    "[d2_v1_ca[0]]":
                        label .v1_m1_path_ca:
                            $ menuset_d2.discard("[d2_v1_ca[1]]")
                            rat_speak "Squeaaaaaak"
                            diego happy "Ah qual foi? Quer colo?"
                            scene bg diegorat with fade
                            diego "Assim tá melhor?"
                            diego "Ah ok, então pequeno, só rapidinho pra eu terminar aqui"
                            scene bg desk happy with fade
                            diego "Hmm ok onde eu estava mesmo?"
                            $ score += 1
                            jump day_3
                    "[d2_v1_ca[1]]":
                        $ menuset_d2.discard("[d2_v1_ca[1]]")
                        jump .v1_m1_path_ca
                    "[d2_v1_cb[0]]":
                        label .v1_m1_path_cb:
                            diego surprised "AH, mas que!"
                            diego angry "Ei!"
                            diego "Huh bem fica ai então, só não cai denovo!"
                            diego "Bicho louco"
                            show diego laughing
                            $ score -= 1
                            jump .v1_m2
                    "[d2_v1_cc[0]]":
                        label .v1_m1_path_cc:
                            $ menuset_d2.discard("[d2_v1_cc[1]]")
                            diego surprised "Ei?!"
                            diego -surprised @ surprised "Huh okay, tá bom então"
                            diego "Huh só vou terminar isso aqui então, vai entender"
                            jump day_3
                    "[d2_v1_cc[1]]":
                        $ menuset_d2.discard("[d2_v1_cc[1]]")
                        jump .v1_m1_path_cc
        "[d2_v1_c[1]]":
            $ menuset_d2.discard("[d2_v1_c[1]]")
            jump .v1_m1_path_c
    return

label .version_2:
    "*CLACK CLACK CLACK CLACK CLACK CLACK CLACK CLACK CLACK CLACK CLACK CLACK CLACK CLACK CLACK CLACK CLACK CLACK CLACK CLACK CLACK *"
    show diego angry
    show rat confused at rat_right
    diego "POR QUE SÓ NÃO FUNCIONA?!?” “GAAAH EU JÁ FIZ ISSO!!"
    rat_think "AH!!!"
    rat_think "O que tá acontecendo?!?"
    show rat standing at rat_stand_right
    rat_think "O que ele fica fazendo ali?"
    rat_think "Ele tá brigando, ou estressado com algo."
    menu .v2_m1:
        set menuset_d1
        "[d1_v2_a[0]]":
            label .v2_m1_path_a:
                $ menuset_d1.discard("[d1_v2_a[1]]")
                show rat standing at rat_stand_right
                rat_think "Ei! Humano olha pra mim, aqui!"
                rat_speak "Squeee! Squeak! Squee!"
                diego sad @ surprised "Hã?"
                diego "*Glup* *Sniff*"
                diego "O que você quer garoto?"
                diego @ -sad "Volta a dormir, eu quero ficar sozinho."
                rat_think "Ei! Qual foi?"
                diego angry "Eu não estou com cabeça para isso! Cadê o pano da gaiola?"
                scene black
                diego "Vai dormir!"
                $ score -= 1
            jump day_2
        "[d1_v2_a[1]]":
            $ menuset_d1.discard("[d1_v2_a[1]]")
            jump .v2_m1_path_a
        "[d1_v2_b[0]]":
            label .v2_m1_path_b:
                $ menuset_d1.discard("[d1_v2_b[1]]")
                rat_think "Hm, não vou conseguir ajudar ele, não tem porque ficar acordado…"
                scene black with fade
                "Algum tempo depois..."
                diego "*Sniff*"
                diego "Eu não aguento mais sentir tanta falta."
                scene bg desk closed with fade
                rat_think "Hm? Ai ai, ele ainda não parou…"
                show diego sad
            jump .v2_m1
        "[d1_v2_c[0]]":
            label .v2_m1_path_c:
                $ menuset_d1.discard("[d1_v2_c[1]]")
                "Você sai da gaiola sem problemas."
                rat_think "Meu Humano está muito distraído."
                rat_think "Não me viu ainda..."
                menu .v2_m2:
                    set menuset_d1
                    "[d1_v2_ca[0]]":
                        label .v1_m1_path_ca:
                            $ menuset_d1.discard("[d1_v2_ca[1]]")
                            show rat standing at rat_stand_right
                            diego surprised "Gulp Hã?"
                            diego "Garoto?"
                            diego "*Sniff* Mas como?"
                            diego "..."
                            rat_think "..."
                            diego happy "Ah…"
                            diego sad @ happy "Esses seus  olhinhos me lembram…"
                            diego "Sigh… sinto saudades sabe?"
                            diego "Como eu queria que nada tivesse acontecido…"
                            diego "*Sniff Sniff*"
                            rat_speak "Squeak!!!"
                            diego -sad @ sad "*Glup*"
                            diego "Eu sei."
                            diego "Desculpa..."
                            diego "Obrigado garoto, obrigado."
                            "A noite termina, o humano fazendo carinho em seu animalzinho."
                            $ score += 1
                        jump day_2
                    "[d1_v2_ca[1]]":
                        $ menuset_d1.discard("[d1_v2_ca[1]]")
                        jump .v1_m1_path_ca
                    "[d1_v2_cb[0]]":
                        label .v1_m1_path_cb:
                            $ menuset_d1.discard("[d1_v2_cb[1]]")
                            diego surprised "AI!!!"
                            diego angry "mas que... QUE MERDA GAROTO!!!"
                            diego "Como que você saiu?!?!"
                            rat_speak "squea..-"
                            diego "Não quero saber!!!"
                            diego "Você vai voltar pra gaiola."
                            diego "E FICA AI! peste.."
                            $ score -= 2
                        jump day_2
                    "[d1_v2_cb[1]]":
                        $ menuset_d1.discard("[d1_v2_cb[1]]")
                        jump .v1_m1_path_cb
                    "[d1_v2_cc[0]]":
                        label .v1_m1_path_cc:
                            $ menuset_d1.discard("[d1_v2_cc[1]]")
                            diego surprised "O que?!?!"
                            diego -surprised @ surprised "Mas como foi que você saiu da gaiola?"
                            show rat standing at rat_stand_right
                            rat_speak "Squeak! Squeak!"
                            diego @ sad "*Glup*"
                            diego "Ai ai."
                            diego "O que faço com você?"
                            diego @ sad "Você me trás tantas lembranças…"
                            "E então... ambos se abraçam"
                            diego "*Sniff*... ok.."
                            diego "Pronto garoto."
                            diego "Tá mais confortável né?"
                            diego "Obrigado por isso."
                            diego "Não deve ser fácil pra você também."
                        jump day_2
                    "[d1_v2_cc[1]]":
                        $ menuset_d1.discard("[d1_v2_cc[1]]")
                        jump .v1_m1_path_cc
        "[d1_v2_c[1]]":
            $ menuset_d1.discard("[d1_v2_c[1]]")
            jump .v2_m1_path_c
    return

label .version_3:
    return
