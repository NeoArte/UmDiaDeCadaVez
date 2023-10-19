label day_1():
    scene bg room with fade
    "Dia 1 ([score])"
    # TODO - Gerar valores aleatórios
    $ version = 1
    $ day_color = week_colors[WeekDay.ONE]
    
    if version == 1:
        jump .version_1
    elif version == 2:
        jump .version_2
    elif version == 3:
        jump .version_3

label .version_1:
    "Dia 1"
    rat_think "Dono está com bastante sede hoje!"
    rat_think "Mas... esse não parece o cheiro de algo bom"
    show diego triste
    diego "*Múrmurios e Suspiros*"
    hide diego
    menu .choice_1:
        "Chamar Dono":
            rat_think "Ele está vindo até aqui!"
            rat_think "Mas ele parece... tonto"
            rat_think "Será que está machucado?"
            show diego bebado
            diego "Qual foi *hic* pequenino?"
            diego "Quer um pouco? hehe"
            hide diego
        "Ficar quieto":
            rat_think "Ele continua ali..."
            rat_think "Ah! Ele ta roncando"
            rat_think "Espero que ele fique melhor amanhã..."
            jump day_2
        "Tentar sair":
            rat_think "Ele parece irritado... e tonto"
            rat_think "Dono deu uma olhada na minha gaiola e foi pegar mais dessa coisa"
            rat_think "Talvez eu devesse tentar de novo"
            $ score -= 1
            jump .choice_1
    menu .choice_2:
        "Pede para experimentar":
            show diego triste
            rat_speak "Cof! Cof Cof"
            diego rindo @ triste "Ai ai, o que eu estava pensando, espera ai vou pegar água pra gente"
            rat_think "Ele parece preocupado, mas sinto que pudemos rir com isso"
            rat_think "Ehhh pena que o gosto era bem ruim. Eca! Hihihi"
            $ score += 1
            jump day_2
        "Se esconder do cheiro":
            show diego bravo
            diego "Humf! Mais pra mim"
            rat_think "Ele foi pegar mais... espero que ele melhore amanhã"
            $ score -= 1
            jump day_2
        "Pede carinho":
            show diego feliz
            rat_think "Nós brincamos até ele cair no sono..."
            rat_think "O que foi bem rápido, mas melhor que nada."
            jump day_2
    return

label .version_2:
    return

label .version_3:
    return
