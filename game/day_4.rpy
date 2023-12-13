label day_4():
    scene black with fade
    "Dia 4 - ([score])"
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
    "Ao fundo é possível ouvir sons de choro."
    diego sad "Gulp… sniff.. Uhuhh.."
    rat_think "Uh?"
    rat_think "Ele ta chorando..."
    menu .v1_m1:
        set menuset_d4
        "[d4_v1_a[0]]":
            label .path_a:
                $ d4_v1_a_repetitions += 1
                if d4_v1_a_repetitions < 3:
                    $ menuset_d4.discard("[d4_v1_a[0]]")
                    if d4_v1_a_repetitions <= 2:
                        rat_think "EI! Ei vem cá! O que foi?!"
                        diego sad "Gulp… sniff.. Uhuhh.."
                        rat_think "Uh ele não me ouviu"
                    jump .v1_m1
                else:
                    $ menuset_d4.discard("[d4_v1_a[1]]\nRepetições: [d4_v1_a_repetitions]")
                    rat_think "Humano! Sério! Tudo certo?"
                    hide diego
                    diego "Hmmm"
                    rat_think "Droga ele enterrou a cabeça onde ele tá deitado, acho que não está pra conversa…"
                    jump day_4
        "[d4_v1_a[1]]]\nRepetições: [d4_v1_a_repetitions]":
            $ menuset_d4.pop()
            jump .path_a
        "[d4_v1_b[0]]":
            label .path_b:
                $ menuset_d4.discard("[d4_v1_b[1]]")
                rat_think "Hm, e eu com isso, desculpa mas não tô pra drama hoje."
                diego sad "Gulp… sniff.. Uhuhh.."
                hide diego
                diego "..."
                diego "*ronco*"
                rat_think "Boa noite."
                jump day_4
        "[d4_v1_b[1]]":
            $ menuset_d4.discard("[d4_v1_b[1]]")
            jump .path_b
        "[d4_v1_c[0]]":
            $ menuset_d4.discard("[d4_v1_c[1]]")
            label .path_c:
                rat_think "Huh, ele nem me trancou."
                rat_think "Bem okay, agora pra onde?"
                menu .v1_m2:
                    set menuset_d4
                    "[d4_v1_ca[0]]":
                        $ menuset_d4.discard("[d4_v1_ca[1]]")
                        label .path_ca:
                            diego confused @ surprised "AH!"
                            diego "Ah... ah oi pequeno..."
                            diego "desculpa eu..."
                            "Ambos se abraçam"
                            diego happy @ sad "ah..."
                            diego "bem... podemos dormir juntos sim..."
                            jump day_4
                    "[d4_v1_ca[1]]":
                        $ menuset_d4.discard("[d4_v1_ca[1]]")
                        jump .path_ca
                    "[d4_v1_cb[0]]":
                        $ menuset_d4.discard("[d4_v1_cb[1]]")
                        label .path_cb:
                            diego -sad "Hm? Ah é…"
                            diego "tá *Sigh* eu ainda não dei comida pro guri né?"
                            diego "Ookay pequeno… pequeno?"
                            diego surprised "Ah não"
                            diego "Ah droga cadê ele?!"
                            menu .v1_m3:
                                set menuset_d4
                                "[d4_v1_cba[0]]":
                                    label .path_cba:
                                        $ menuset_d4.discard("[d4_v1_cba[1]]")
                                        rat_speak "Squeak! Squeak! Squeak?"
                                        rat_think "Ei! To aqui! Algum problema?"
                                        diego surprised "AH! Ai está você!"
                                        diego "Ah que susto menino!"
                                        diego happy @ laughing "Ahahaha okay, ufa."
                                        diego "Tá quer ficar fora essa noite?"
                                        diego "Pode ser até só se comporta."
                                        jump day_4
                                "[d4_v1_cba[1]]":
                                    $ menuset_d4.discard("[d4_v1_cba[1]]")
                                    jump .path_cba
                                "[d4_v1_cbb[0]]":
                                    label .path_cbb:
                                        $ menuset_d4.discard("[d4_v1_cbb[1]]")
                                        diego sad "Ah droga…"
                                        diego "Bem ele deve estar por aí…"
                                        diego @ happy"Ei pequeno! Se você tiver por aí, ta com comida aqui de novo…"
                                        diego "só…. Não some também…"
                                        diego "Sigh…"
                                        hide diego
                                        rat_think "Ah, comida né! Não tem nada aqui disso"
                                        rat_think "só sujeira..."
                                        rat_think "Bem vou voltar lá."
                                        jump day_4
                                "[d4_v1_cbb[1]]":
                                    $ menuset_d4.discard("[d4_v1_cbb[1]]")
                                    jump .path_cbb
                                "[d4_v1_cbc[0]]":
                                    label .path_cbc:
                                        $ menuset_d4.discard("[d4_v1_cbc[1]]")
                                        rat_think "Ah! Pera! Ta claro lá fora!"
                                        rat_think "Huh acho que passo por aqui"
                                        rat_speak "Squeak! Squish... Squeak!"
                                        rat_think "é só... eu... uh..!"
                                        diego surprised "huh? EITA"
                                        diego "AH nanana volta aqui!"
                                        "A porta se abre."
                                        diego -surprised "UH! Ah ok!"
                                        diego angry "Seu louco! Não vai fugir assim na.."
                                        diego @ surprised "Huh? Ah!"
                                        diego "Boa noite!"
                                        diego "Ou uh… tarde né hahaha"
                                        diego @ laughing "Desculpa ele normalmente é mais comportado"
                                        diego "Sim! Ele é de estimação, mais limpo que eu hahahaha"
                                        diego "Não me lembro de você, novo por aqui né?"
                                        diego "Ah que bom, bem vindo então! Boa noite!"
                                        diego surprised @ confused "..."
                                        diego " TARDE! hahahahaha"
                                        rat_think "Uh, faz tempo que não vejo outra pessoa, nem ele conversando."
                                        rat_think "Hah parece que ele também gostou"
                                        jump day_4
                                "[d4_v1_cbc[1]]":
                                    $ menuset_d4.discard("[d4_v1_cbc[1]]")
                                    jump .path_cbc
                    "[d4_v1_cb[1]]":
                        $ menuset_d4.discard("[d4_v1_cb[1]]")
                        jump .path_cb
                    "[d4_v1_cc[0]]":
                        $ menuset_d4.discard("[d4_v1_cc[1]]")
                        label .path_cc:
                            rat_think "Hm que fome!"
                            rat_think "Tá muito sujo aqui."
                            show rat standing with rat_stand_right
                            rat_think "Deixa ver se algo lá em cima tá bom."
                            "Sons de troço."
                            diego angry @ surprised "Huh? EI!"
                            diego "EI seu peste!"
                            "Você é colocado de volta na gaiola."
                            diego @ -angry "Safado!"
                            diego "Tu não come o suficiente não?!"
                            diego "Toma aqui sua comida e BOA NOITE!"
                            diego -angry "Onde já se viu…"
                            jump day_4
                    "[d4_v1_cc[1]]":
                        $ menuset_d4.discard("[d4_v1_cc[1]]")
                        jump .path_cc
        "[d4_v1_c[1]]":
            $ menuset_d4.discard("[d4_v1_c[1]]")
            jump .path_c
    return

label .version_2:
    return

label .version_3:
    return
