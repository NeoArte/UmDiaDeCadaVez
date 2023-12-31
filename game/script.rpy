﻿label start:
    stop music fadeout 2.5
    jump day_1
    scene bg room with Pixellate(1.0, 5)
    call setup from start_setup
    $ day_color = week_colors[WeekDay.ZERO]
    "Dia 0"
    rat_think "O humano está de volta!"
    rat_think "Mas a outra pessoa não está com ele de novo"
    rat_think "Hm..."
    rat_think "Esse é o cheiro dela, eles se encontraram, mas ele não parece feliz como ele ficava antes, com os outros dois."
    show diego
    diego "Bem, está feito, papelada resolvida…"
    diego "Pelo menos não vai ter pensão."

    hide diego
    menu tutorial_1:
        "Chamar o dono":
            show diego
            rat_speak "Squeak"
            diego feliz "Ah, oi pequeno!"
            diego triste "Sim, você vai ficar comigo... pelo menos..."
            hide diego
            jump tutorial_2
        "Ficar quieto":
            show diego triste
            diego "Ah..."
            diego "Está feito... Deuses está mesmo feito"
            rat_think "Ele está chorando..."
            rat_think "Espero que ele fique melhor amanhã..."
            $ score -= 1
            jump day_1
        "Tentar sair":
            show diego
            diego "Opa, opa, opa, calma lá."
            diego rindo "Não vai tentar fugir de mim também ein..."
            diego @ triste "Hah..."
            hide diego
            jump tutorial_2
    menu tutorial_2:
        "Cheirar dono":
            show diego
            diego feliz "Ah, tá sentindo o cheiro dela né..."
            diego triste "É, ela não vai voltar"
            rat_think "Ah..."
            rat_think "Quem sabe... Amanhã é um novo dia"
            $ score -= 1
            jump day_1
        "Se esconder":
            show diego triste
            diego "É, bem... eu nunca fui o favorito..."
            diego "...Aqui sua comida"
            rat_think "Espero que ele fique melhor amanhã..."            
            $ score -= 1
            jump day_1
        "Fazer barulhos":
            show diego
            diego "O que foi pequeno?"
            diego rindo "Hehe"
            diego "Você ta me lembrando como você era com..."
            diego triste "Hm..."
            rat_think "Espero que ele fique melhor amanhã..."
            $ score -= 1
            jump day_1
    return
