label day_3():
    scene black with fade
    "Dia 3 - ([score])"
    scene bg room with fade
    $ version = 1
    $ day_color = week_colors[WeekDay.ONE]

    if version == 1:
        jump .version_1
    elif version == 2:
        jump .version_2
    elif version == 3:
        jump .version_3

label .version_1:
    rat_speak "Sigh"
    rat_think "... hm?"
    rat_think "Ué, essa não é minha gaiola.."
    rat_think "Huh, to numa caixa?"
    diego @ happy "Opa bom dia pequeno."
    diego "Só um minuto tô terminando aqui."
    diego @ happy "Tó um biscoitinho."
    menu .v1_m1:
        set menuset_d3
        "[d3_v1_a[0]]":
            label .path_a:
                $ menuset_d3.discard("[d3_v1_a[1]]")
                diego "Huh? Calma pequeno, tenho que te deixar certinho."
                diego sad @ laughing "Pelo menos alguém nessa casa tem que tá arrumado hahaha."
                diego "..."
                diego "Mas bem fica aí então, assim já fica no jeitinho"
                jump day_3
        "[d3_v1_a[1]]":
            $ menuset_d3.discard("[d3_v1_a[1]]")
            jump .path_a
        "[d3_v1_b[0]]":
            label .path_b:
                $ menuset_d3.discard("[d3_v1_b[1]]")
                rat_think "Ah, que bom então!"
                rat_think "Ele tá bem hoje ein? Tá até arrumando minhas coisas"
                rat_think "bem, vou aproveitar aqui então."
                rat_think "Hmm essa serragem nova tem cheiro bom."
                jump day_3
        "[d3_v1_b[1]]":
            $ menuset_d3.discard("[d3_v1_b[1]]")
            jump .path_b
        "[d3_v1_c[0]]":
            label .path_c:
                $ menuset_d3.discard("[d3_v1_c[1]]")
                diego "Opa opa opa, que isso pequeno?"
                diego "É te peguei, e agora?"
                diego "Para onde você tava querendo ir ao menos?"
                diego "Pra minha… Deus aqui tá sujo…"
                diego "Mas bem você merece melhor né?"
                diego "Eu… eu sinto que… você é quem precisa mais…."
                diego "Quem merece mais…"
                diego "Pera eu estou me colocando abaixo de um rato?”"
                diego sad "..."
                diego "Você não é só um rato né"
                diego "Não pra mim."
                diego "Você… é o que me sobrou…"
                diego "Você merece um lugar limpo pequeno"
                diego "eu uh… ainda to vendo se eu mereço um também"
                jump day_3
        "[d3_v1_c[1]]":
            $ menuset_d3.discard("[d3_v1_c[1]]")
            jump .path_c
    return

label .version_2:
    return

label .version_3:
    return
