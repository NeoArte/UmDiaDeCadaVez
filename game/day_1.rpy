label day_1():
    "Dia 1 - ([score])"
    # $ version = randint(1,2)
    $ version = 2
    $ day_color = week_colors[WeekDay.ONE]
    
    if version == 1:
        scene bg room with fade
        jump .version_1
    elif version == 2:
        scene bg desk closed with fade
        jump .version_2
    elif version == 3:
        jump .version_3

label .version_1:
    show diego drunk
    rat_think "Ugh esse cheiro não tá bom, ele tá com isso na boca?"
    menu .v1_m1:
        set menuset_d1
        "[d1_v1_a[0]]":
            label .v1_m1_path_a:
                $ menuset_d1.discard("[d1_v1_a[1]]")
                rat_speak "Squeak! Squeak! Squeak Squeak!"
                rat_think "Ei! Tira isso! Tá estragado ou algo assim!"
                diego "OoOpa garotinho? Qual… hic* qual fooi?"
                menu .v1_m2:
                    set menuset_d1
                    "[d1_v1_aa[0]]":
                        label .v1_m1_path_aa:
                            $ menuset_d1.discard("[d1_v1_aa[1]]")
                            show rat standing at rat_stand_right
                            diego "eita, quer... *HIC*"
                            diego "quer um pouco, pequeno?"
                            rat_think "Huh, deixa eu ver qual é a dessa..."
                            rat_speak "Sque-BLEGH! BLEGH!"
                            rat_think "NOSSA! QUE GOSTO HORROROSO!"
                            diego @ surprised "Eita! Pera ai, pequeno!"
                            diego @ sad "Po, mas isso mal tem..."
                            diego @ surprised "Meu Deus! Já passou da metade..."
                            diego -drunk "..."
                            rat_speak "..."
                            diego "Ta."
                            diego "Vou pegar água pra gente."
                            $ score += 1
                            jump day_2
                    "[d1_v1_aa[1]]":
                        $ menuset_d1.discard("[d1_v1_aa[1]]")
                        jump .v1_m1_path_aa
                    "[d1_v1_ab[0]]":
                        label .v1_m1_path_ab:
                            $ menuset_d1.discard("[d1_v1_ab[1]]")
                            rat_think "Uh, esse cheiro não é pra mim não."
                            diego angry @ sad "Ih! Qual foi, pequeno?!"
                            diego "*HIC* Ah! Então vai dormir!"
                            diego "Uhh... bem, já que tô aqui… *hic*."
                            diego "Deixa eu encher o tanque.."
                            rat_think "Ah, sério outra? Ah, mas vou dormir mesmo."
                            $ score -= 1
                            jump day_2
                    "[d1_v1_ab[1]]":
                        $ menuset_d1.discard("[d1_v1_ab[1]]")
                        jump .v1_m1_path_ab
                    "[d1_v1_ac[0]]":
                        label .v1_m1_path_ac:
                            $ menuset_d1.discard("[d1_v1_ac[1]]")
                            rat_speak "Squeakikiki!"
                            rat_think "Oh me deixa aí! Isso não tá legal."
                            diego happy "hahah quer brincar seu fofo? Ahh! Vem cá então."
                            scene bg diegorat with fade
                            diego "heheheh mas olha só que fofo né? Ah mas você é"
                            scene bg room dark with fade
                            diego @ drunk "*HIC* fofinho né? Eu uh…"
                            diego -happy "é uh… que tal um…"
                            hide diego
                            diego "*Ronco*"
                            rat_think "Ih, já dormiu?"
                            rat_think "Uh é ele não parece tá bem, deve acordar melhor."
                            rat_think "Vou voltar pro meu canto, o cheiro tá menos pior"
                            jump day_2
                    "[d1_v1_ac[1]]":
                        $ menuset_d1.discard("[d1_v1_ac[1]]")
                        jump .v1_m1_path_ac
        "[d1_v1_a[1]]":
            $ menuset_d1.discard("[d1_v1_a[1]]")
            jump .v1_m1_path_a
        "[d1_v1_b[0]]":
            label .v1_m1_path_b:
                $ menuset_d1.discard("[d1_v1_b[1]]")
                rat_think "Ugh vou é ficar tonto com isso, vou me enfiar nesse pano e vai que diminui."
                jump day_2
        "[d1_v1_b[1]]":
            $ menuset_d1.discard("[d1_v1_b[1]]")
            jump .v1_m1_path_b
        "[d1_v1_c[0]]":
            label .v1_m1_path_c:
                $ menuset_d1.discard("[d1_v1_c[1]]")
                "*TUM* *TUM"
                diego "EI ei ei ei!"
                diego "*HIC*"
                diego "Calma lá amigo, não vai fugir ein? Hahaha."
                diego "OOoookAY! *Hic” “agora isso vai…"
                diego "Hic vai ficar AI! Heh."
                show rat sad at rat_right
                rat_think "Ah droga ele fechou de vez isso, nem balança."
                diego laughing "HAH! Voce está prRESO! *HIC*"
                diego "hehe e já que to aqui, essa acabou..."
                diego "ME VE MAIS UMA CHEFIA hahahahah."
                rat_think "Ugh.. esse cheiro de novo, é hoje ele vai ficar nessa."
                $ score -= 1
                jump day_2
        "[d1_v1_c[1]]":
            $ menuset_d1.discard("[d1_v1_c[1]]")
            jump .v1_m1_path_c
    return

label .version_2:
    "Ao fundo é possível uma música tocando."
    show diego sad
    diego "*Sniff sniff*"
    diego "*Glup*"
    show rat confused at rat_right
    rat_think "Hum?"
    show rat standing at rat_stand_right
    rat_think "Ah!"
    rat_think "É meu humano!"
    show rat confused at rat_right
    rat_think "Mas ele ta fazendo um som estranho..."
    rat_think "O que está acontecendo?"
    hide rat
    diego "*Sniff*"
    diego "Eu não sei se consigo suportar tudo isso"
    diego "*Sniff*"
    diego "Eu não aguento mais o mesmo pesadelo"
    diego @ "Vai tudo voltar ao normal"
    diego "Precisa voltar..."
    diego "*Gulp*"
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
