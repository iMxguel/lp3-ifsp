def simulador_eleicoes():
    candidatos = {
        1: {'nome': 'Candidato 1', 'votos': 0},
        2: {'nome': 'Candidato 2', 'votos': 0},
        3: {'nome': 'Candidato 3', 'votos': 0}
    }

    while True:
        print("Candidatos disponíveis:")
        for numero, candidato in candidatos.items():
            print(f"{numero}: {candidato['nome']}")

        voto = input("Digite o número do candidato em quem você deseja votar (ou '0' para encerrar a votação): ")
        
        if voto == '0':
            break
        elif voto.isdigit() and int(voto) in candidatos:
            candidatos[int(voto)]['votos'] += 1
            print("Voto computado com sucesso!")
        else:
            print("Candidato inválido. Por favor, escolha um número correspondente a um candidato da lista.")

    print("\nResultado da votação:")
    total_votos = sum(candidato['votos'] for candidato in candidatos.values())
    for numero, candidato in candidatos.items():
        percentual_votos = (candidato['votos'] / total_votos) * 100
        print(f"{candidato['nome']}: {candidato['votos']} votos ({percentual_votos:.2f}% dos votos)")

    vencedor = max(candidatos, key=lambda x: candidatos[x]['votos'])
    print(f"\nO vencedor é: {candidatos[vencedor]['nome']}!")

simulador_eleicoes()
