init 2 python:
    menuset_d1 = set()
    menuset_d2 = set()
    menuset_d3 = set()
    menuset_d4 = set()

    # DAY 1 -----------------------------------------------------------------------------------
    d1_v1_a = ["Chamar seu Humano."]
    d1_v1_a.append(d1_v1_a[0] + "\n{size=-10}Leva às escolhas \"Cheira o que tem\", \"Se esconde\", \"Pede pra sair\".")
    d1_v1_b = ["Ficar quieto."]
    d1_v1_b.append(d1_v1_b[0] + "\n{size=-10}Caminho Neutro (0), leva para o próximo dia.")
    d1_v1_c = ["Pede pra sair."]
    d1_v1_c.append(d1_v1_c[0] + "\n{size=-10}Caminho Negativo (-1), o dono te prende de volta, bebe mais e segue para o próximo dia.")

    d1_v1_aa = ["Cheira o que tem."]
    d1_v1_aa.append(d1_v1_aa[0] + "\n{size=-10}Caminho Positivo (+1), seu incomôdo com o álcool acorda seu dono para o quanto ele está bebendo. Segue para o próximo dia.")
    d1_v1_ab = ["Se esconde."]
    d1_v1_ab.append(d1_v1_ab[0] + "\n{size=-10}Caminho Negativo (-1), seu dono se incomoda com tê-lo chamado para nada e bebê mais. Segue para o próximo dia.")
    d1_v1_ac = ["Pede pra sair."]
    d1_v1_ac.append(d1_v1_ac[0] + "\n{size=-10}Caminho Neutro (0), vocês brincam até seu dono dormir, segue para o próximo dia.")


    d1_v2_a = ["Chamar seu Humano."]
    d1_v2_a.append(d1_v2_a[0] + "\n{size=-10}Caminho Negativo (-1), seu humano está cansado demais para te dar atenção e vai dormir irritado, segue para o próximo dia.")
    d1_v2_b = ["Ficar quieto."]
    # d1_v2_b.append(d1_v2_b[0] + "\n{size=-10}Caminho Neutro (0), leva para o próximo dia.")
    d1_v2_c = ["Tentar sair da gaiola."]
    d1_v2_c.append(d1_v2_c[0] + "\n{size=-10}Leva às escolhas \"Subir no seu humano\", \"Mordeu seu humano\", \"Fazer barulhinhos\".")

    d1_v2_ca = ["Subir no seu humano."]
    d1_v2_ca.append(d1_v2_ca[0] + "\n{size=-10}Caminho Positivo (+1), seu incomôdo com o álcool acorda seu dono para o quanto ele está bebendo. Segue para o próximo dia.")
    d1_v2_cb = ["Morder seu humano."]
    d1_v2_cb.append(d1_v2_cb[0] + "\n{size=-10}Caminho Negativo (-2), seu dono se incomoda com tê-lo chamado para nada e bebê mais. Segue para o próximo dia.")
    d1_v2_cc = ["Fazer barulhinhos."]
    d1_v2_cc.append(d1_v2_cc[0] + "\n{size=-10}Caminho Neutro (0), vocês brincam até seu dono dormir, segue para o próximo dia.")


    # DAY 2 -----------------------------------------------------------------------------------
    d2_v1_a_repetitions = 0
    d2_v1_a = ["Chamar seu Humano."]
    d2_v1_a.append(d2_v1_a[0] + "\n{size=-10}Caminho Neutro (0) e volta para a tela atual. Caso selecionada um total de 5 vezes leva ao seu dono ficar irritada e seguir para o próximo dia, MUITO negativo. (-3)")
    d2_v1_b = ["Ficar quieto."]
    d2_v1_b.append(d2_v1_b[0] + "\n{size=-10}Caminho Neutro (0), você dorme e não interage. Leva para o próximo dia.")
    d2_v1_c = ["Tentar sair da gaiola."]
    d2_v1_c.append(d2_v1_c[0] + "\n{size=-10}Leva às escolhas \"Pedir Colo\", \"Morder Dono\", \"Se esconder\".")

    d2_v1_ca = ["Pedir Colo"]
    d2_v1_ca.append(d2_v1_ca[0] + "\n{size=-10}Caminho Positivo (+1), o momento afetuoso com o dono o acalma um pouco. Segue para o próximo dia.")
    d2_v1_cb = ["Morder Dono"]
    # d2_v1_cb.append(d2_v1_cb[0] + "\n{size=-10}Caminho Negativo (-1), seu dono se incomoda com tê-lo chamado para nada e bebê mais. Segue para o próximo dia.")
    d2_v1_cc = ["Se esconder"]
    d2_v1_cc.append(d2_v1_cc[0] + "\n{size=-10}Caminho Neutro (0), vocês brincam até seu dono dormir, segue para o próximo dia.")

    # DAY3 -----------------------------------------------------------------------------------
    d3_v1_a = ["Ir até seu Humano."]
    d3_v1_a.append(d3_v1_a[0] + "\n{size=-10}Caminho Negativo (-1), ele te ajuda, mas se afunda mais em uma espiral autodepreciativa. Segue para o próximo dia.")
    d3_v1_b = ["Ficar quieto."]
    d3_v1_b.append(d3_v1_b[0] + "\n{size=-10}Caminho Neutro (0), seu dono parece bem então você aproveita para descansar. Leva para o próximo dia.")
    d3_v1_c = ["Tentar sair da mesa."]
    d3_v1_c.append(d3_v1_c[0] + "\n{size=-10}Caminho Positivo (+1), seu dono busca melhorar por você, mas também reflete que ele próprio também vale o esforço. Leva para o próximo dia.")

    # DAY 4 -----------------------------------------------------------------------------------
    d4_v1_a_repetitions = 0
    d4_v1_a = ["Chamar seu Humano."]
    d4_v1_a.append(d4_v1_a[0] + "\n{size=-10}Caminho Neutro (0) e volta para a tela atual. Caso selecionada um total de 2 vezes, seu dono, chateado em não poder te ajudar, chora mais. Negativo (-1), segue para o próximo dia.")
    d4_v1_b = ["Ficar quieto."]
    d4_v1_b.append(d4_v1_b[0] + "\n{size=-10}Caminho Neutro (0), você ignora a crise dele e volta a dormir, vai para o próximo dia.")
    d4_v1_c = ["Tentar sair da gaiola."]
    d4_v1_c.append(d4_v1_c[0] + "\n{size=-10}Leva às escolhas \"Ir até o dono\", \"Se esconder\", \"Comer algo na cozinha\".")

    d4_v1_ca = ["Ir até o dono"]
    d4_v1_ca.append(d4_v1_ca[0] + "\n{size=-10}Caminho Positivo (+1), vocês dormem juntos se acolhendo até o próximo dia.")
    d4_v1_cb = ["Se esconder"]
    d4_v1_cb.append(d4_v1_cb[0] + "\n{size=-10}Leva às escolhas \"Voltar pro dono\", \"Manter esconder\", \"Tentar sair do apartamento\".")
    d4_v1_cc = ["Comer algo na cozinha"]
    d4_v1_cc.append(d4_v1_cc[0] + "\n{size=-10}Caminho Negativo(-1), sua bagunça em procura de comida irrita seu dono, ele te prende até amanhã.")

    d4_v1_cba = ["Voltar pro dono"]
    d4_v1_cba.append(d4_v1_ca[0] + "\n{size=-10}Caminho Positivo (+1), vocês aproveitam a noite juntos até o próximo dia.")
    d4_v1_cbb = ["Manter escondido"]
    d4_v1_cbb.append(d4_v1_cb[0] + "\n{size=-10}Caminho Negativo (-1), seu breve desaparecimento traz memórias ruins à seu dono, você volta e segue até o dia seguinte.")
    d4_v1_cbc = ["Tentar sair do apartamento"]
    d4_v1_cbc.append(d4_v1_cc[0] + "\n{size=-10}Caminho Positivo(+1), ao sair da casa, seu dono, enquanto te procura, tem uma conversa agrádavel com outra pessoa (algo que ele não faz a muito tempo) e ambos voltam felizes até amanhã.")

    menuset_d1.update({
            "[d1_v1_a[1]]",
            "[d1_v1_b[1]]",
            "[d1_v1_c[1]]",
            "[d1_v1_aa[1]]",
            "[d1_v1_ab[1]]",
            "[d1_v1_ac[1]]",
            "[d1_v2_a[1]]",
            # "[d1_v2_b[1]]",
            "[d1_v2_c[1]]",
            "[d1_v2_ca[1]]",
            "[d1_v2_cb[1]]",
            "[d1_v2_cc[1]]"
            })
    menuset_d2.update({
            "[d2_v1_a[1]]\nRepetições: [d2_v1_a_repetitions]",
            "[d2_v1_b[1]]",
            "[d2_v1_c[1]]",
            "[d2_v1_ca[1]]",
            "[d2_v1_cb[1]]",
            "[d2_v1_cc[1]]"
            })
    menuset_d3.update({
            "[d3_v1_a[1]]",
            "[d3_v1_b[1]]",
            "[d3_v1_c[1]]",
            })
    menuset_d4.update({
            "[d4_v1_a[1]]]\nRepetições: [d4_v1_a_repetitions]",
            "[d4_v1_b[1]]",
            "[d4_v1_c[1]]",
            "[d4_v1_ca[1]]",
            "[d4_v1_cb[1]]",
            "[d4_v1_cc[1]]",
            "[d4_v1_cba[1]]",
            "[d4_v1_cbb[1]]",
            "[d4_v1_cbc[1]]"
            })

    print(menuset_d1)
    print(menuset_d2)
    print(menuset_d3)
    print(menuset_d4)
