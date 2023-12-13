label day_1():
    scene bg room with fade
    "Dia 1 - ([score])"
    $ version = 1
    $ day_color = week_colors[WeekDay.ONE]
    
    if version == 1:
        jump .version_1
    elif version == 2:
        jump .version_2
    elif version == 3:
        jump .version_3

label .version_1:
    show diego drunk
    rat_think "Ugh esse cheiro não tá bom, ele tá com isso na boca?"
    menu .v1_m1:
        set menuset_d1
        "[d1_v1_a[0]]":
            label .path_a:
                $ menuset_d1.discard("[d1_v1_a[1]]")
                rat_speak "Squeak! Squeak! Squeak Squeak!"
                rat_think "Ei! Tira isso! Tá estragado ou algo assim!"
                diego "OoOpa garotinho? Qual… hic* qual fooi?"
                menu .v1_m2:
                    set menuset_d1
                    "[d1_v1_aa[0]]":
                        label .path_aa:
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
                            jump day_2
                    "[d1_v1_aa[1]]":
                        $ menuset_d1.discard("[d1_v1_aa[1]]")
                        jump .path_aa
                    "[d1_v1_ab[0]]":
                        label .path_ab:
                            $ menuset_d1.discard("[d1_v1_ab[1]]")
                            rat_think "Uh, esse cheiro não é pra mim não."
                            diego angry @ sad "Ih! Qual foi, pequeno?!"
                            diego "*HIC* Ah! Então vai dormir!"
                            diego "Uhh... bem, já que tô aqui… *hic*."
                            diego "Deixa eu encher o tanque.."
                            rat_think "Ah, sério outra? Ah, mas vou dormir mesmo."
                            jump day_2
                    "[d1_v1_ab[1]]":
                        $ menuset_d1.discard("[d1_v1_ab[1]]")
                        jump .path_ab
                    "[d1_v1_ac[0]]":
                        label .path_ac:
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
                        jump .path_ac
        "[d1_v1_a[1]]":
            $ menuset_d1.discard("[d1_v1_a[1]]")
            jump .path_a
        "[d1_v1_b[0]]":
            label .path_b:
                $ menuset_d1.discard("[d1_v1_b[1]]")
                rat_think "Ugh vou é ficar tonto com isso, vou me enfiar nesse pano e vai que diminui."
                jump day_2
        "[d1_v1_b[1]]":
            $ menuset_d1.discard("[d1_v1_b[1]]")
            jump .path_b
        "[d1_v1_c[0]]":
            label .path_c:
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
                jump day_2
        "[d1_v1_c[1]]":
            $ menuset_d1.discard("[d1_v1_c[1]]")
            jump .path_c
    return

label .version_2:
    return

label .version_3:
    return
