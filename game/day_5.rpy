label day_5:
    scene black with fade
    "Dia 5..."
    if score >= 3:
        scene bg desk happy with fade
        jump day_5_win
    else:
        scene bg room with fade
        jump day_5_restart

label day_5_win:
    rat_think "*Sigh*... hm?"
    rat_think "Nossa que claro"
    rat_think "Eita e que cheiro é esse?"
    diego happy "Booom dia pequeno!"
    diego "Vem cá vem."
    "Ele abre a gaiola."
    diego "To mais livre hoje, que tal um mimo pra nós?"
    rat_think "Que?"
    rat_think "Ah nossa vamos comer juntos!"
    rat_think "Acho que nunca fiz isso com ele"
    diego -happy @ happy "Sabe pequeno, eu…"
    diego "Eu não tava bem esses dias…"
    diego @ laughing "Quer dizer, vamos ser honestos né, ainda não estou hahaha."
    diego "Mas… é sobre isso não?"
    diego "Se manter andando, não se deixar cair"
    diego "Quer dizer, conseguir se levantar"
    diego happy "Mas estou me sentindo melhor!"
    diego -happy @ happy "Nossa muito melhor"
    diego "Ainda sinto falta, mas o tempo me ajudou afinal de contas."
    diego @ happy "E você também! Muito na verdade"
    diego "me pergunto como estaria hoje se estivesse realmente sozinho…"
    diego "Uuh chega! Já fiquei pra baixo o suficiente!"
    diego @ happy "Vamos comer!"
    menu win_endings:
        "Bebida do Humano":
            diego surprised "Eei isso é minha água!"
            rat_speak "Opa, desculpa!"
            diego laughing "Hahaha e pois é né?"
            diego laughing @ -laughing "Nem to no café hoje."
            diego "Tava querendo me sentir eu mesmo… e o pó acabou hahaha."
        "Comida do Humano":
            diego @ surprised "Ah mas que!"
            diego "Hm se bem que… ovo é bom pra vocês né?"
            diego "Aqui, tó um tanto."
            diego happy "Ha ha Bon Appetit pequeno"
        "Ficar parado":
            diego "Hm?"
            diego @ laughing "Ah nossa você se manteve educado, ein?"
            diego "Tá aqui seus petiscos"
            diego @ laughing "E eu achava que você já tinha me inspirado o suficiente nesses últimos dias hahaha"
            diego happy "Obrigado viu pequeno? Você me ajuda muito"
    scene bg diegorat with fade
    "Vitória com [score] pontos"
    return

label day_5_restart:
    rat_think "A semana acabou... ele sempre fica fora o final de semana todo"
    rat_think "E volta com aquele cheiro quente... me sinto tonto"
    rat_think "Bem, eu posso tentar de novo, semana que vem"
    "Derrota com [score] pontos"
    $ score = 0
    jump day_1
