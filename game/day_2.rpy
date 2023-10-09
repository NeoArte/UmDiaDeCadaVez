label day_2():
    $ day_color = week_colors[WeekDay.TWO]
    scene bg desk
    "Dia 2 ([score])"
    # TODO - Gerar valores aleatórios
    $ version = 1
    if version == 1:
        jump .version_1
    elif version == 2:
        jump .version_2
    elif version == 3:
        jump .version_3

label .version_1:
    rat_think "Meu dono... ele parece estar com dor e todo encurvado..."
    rat_think "E o que é esses sons? Tec tec tec, UGH"
    menu .choice_1:
        "Chamar Dono":
            show diego
            diego "*Humpf*"
            rat_think "Ele ta me ignorando... talvez eu possa tentar de novo"
            hide diego
            $ score -= 1
            jump .choice_1
        "Ficar quieto":
            hide diego
            rat_think "Ele ficou ali... fazendo esse tec tec"
            rat_think "E ele dormiu na mesa. Espero que ele melhore..."
            jump day_3
        "Sair da gaiola":
            show diego
            rat_think "Nyehe! Ele deixou a gaiola aberta"
            rat_think "Alto! Alto! Eu vou cair!!!"
            rat_speak "SQUEAK SQUEAK SQUEAK"
            rat_think "Ah... ele me segurou"
            show diego
            diego "Calma ai, pequenino"
            rat_think "Bem... e agora?"
            hide diego
    menu .choice_2:
        "Pedir carinho":
            hide diego
            rat_think "Carinho!!! Com toda minha fofura eu devo conseguir!"
            show diego
            diego "Quer ficar comigo enquanto trabalho? Vem aqui bobinho."
            rat_think "Ele parece mais calmo, isso me deixa feliz!"
            $ score += 1
            jump day_3
        "Morder ele":
            show diego
            diego "Qual foi?!"
            rat_think "Não parece que ele gostou muito.."
            $ score -= 1
            jump day_3
        "Se esconder":
            hide diego
            rat_think "E... eu não consegui. Ele me prendeu de novo"
            rat_think "Amanhã posso tentar de novo hehe"
            jump day_3
    return

label .version_2:
    return

label .version_3:
    return
