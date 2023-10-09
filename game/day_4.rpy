label day_4():
    $ day_color = week_colors[WeekDay.FOUR]
    scene bg room
    "Dia 4 ([score])"
    # TODO - Gerar valores aleatórios
    $ version = 1
    if version == 1:
        jump .version_1
    elif version == 2:
        jump .version_2
    elif version == 3:
        jump .version_3

label .version_1:
    rat_think "Ele... não parece bem..."
    rat_think "É quase como se o coração estivesse mais... vazio"
    rat_think "Ele ta encolhido.. o que eu faço?"

    menu .choice_1:
        "Chamar dono":
            rat_think "Ele ta me ignorando.."
            rat_think "Talvez eu possa tentar outra coisa?"
            jump .choice_1
        "Ficar quieto":
            rat_think "Acabei não fazendo nada e o dia passou..."
            jump day_5
        "Tentar sair":
            # TODO - Permitir ações repetidas
            rat_think "Eu tive que ficar insistindo, mas consegui que ele me tirasse"
            rat_think "Ele voltou para cama... não parece bem ainda."
            rat_think "E agora?"
    menu .choice_2:
        "Ir até o dono":
            rat_speak "Squeak"
            show diego
            diego "Ah!!"
            diego "Deuses, você me deu um susto.."
            diego "Quer dormir um pouco comigo? Eu to exausto..."
            rat_think "Ele é quentinho"
            rat_think "Nós acabamos dormindo, mas acho que ele tava precisando"
            $ score += 1
            jump day_5
        "Se esconder":
            rat_think "Ele ta distraido..."
            rat_think "O dia ta acabando já"
            rat_think "Ah ele ta me botando comida hehe ele não ta me achando"
            rat_think "O que será que eu faço?"
        "Ir para a cozinha":
            rat_think "Explorando! Explorandooo!"
            rat_think "Ah! Acho que fiz muito barulho..."
            rat_think "Ele ficou bravo e me botou na jaula de volta"
            $ score -= 1
            jump day_5
    menu .choice_3:
        "Voltar para ele":
            rat_think "To com saudade! Melhor eu sair"
            rat_think "Ele ficou feliz e me deixou livre, brincamos bastante!"
            $ score += 1
            jump day_5
        "Continuar escondido":
            rat_think "Ainda não fui pego!!! Vou ficar aqui..."
            rat_think "Ah... mas a comida parece tão boa..."
            rat_think "Não!!!!!"
            rat_think "Me deixei tentar e ele me prendeu na jaula... ele parece bravo"
            rat_think "E triste..."
            $ score -= 1
            jump day_5
        "Sair para fora":
            rat_think "Mundo exterior, lá vou eu!"
            rat_think "Oia! É o moço que veio aqui em casa já"
            rat_think "Meu dono me achou aqui fora, agora ele e o moço tão conversando"
            rat_think "Acho que foi bom pra ele"
            $ score += 1
            jump day_5

label .version_2:
    return

label .version_3:
    return
