label day_5:
    scene bg room with fade
    if score >= 3:
        jump day_5_win
    else:
        jump day_5_restart

label day_5_win:
    "Vitória com [score] pontos"
    return

label day_5_restart:
    "Derrota com [score] pontos"
    rat_think "A semana acabou... ele sempre fica fora o final de semana todo"
    rat_think "E volta com aquele cheiro quente... me sinto tonto"
    rat_think "Bem, eu posso tentar de novo, semana que vem"
    $ score = 0
    jump day_1
