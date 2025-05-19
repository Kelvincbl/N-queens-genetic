import random
import matplotlib.pyplot as plt

# Parâmetros
N = 8
TAMANHO_POPULACAO = 100
MAX_GERACOES = 1000
TAXA_MUTACAO = 0.05
VISUALIZAR_A_CADA = 50

# Avaliar aptidão: número de pares de rainhas que não se atacam
def avaliar_aptidao(genes):
    nao_atacando = 0
    for i in range(N):
        for j in range(i + 1, N):
            if genes[i] != genes[j] and abs(genes[i] - genes[j]) != abs(i - j):
                nao_atacando += 1
    return nao_atacando

# Criar indivíduo (solução)
def criar_individuo():
    genes = list(range(N))
    random.shuffle(genes)
    aptidao = avaliar_aptidao(genes)
    return {'genes': genes, 'aptidao': aptidao}

# Criar população inicial
def criar_populacao():
    populacao = [criar_individuo() for _ in range(TAMANHO_POPULACAO)]
    return sorted(populacao, key=lambda x: x['aptidao'], reverse=True)

# Seleção por torneio
def selecionar_pai(populacao):
    candidatos = random.sample(populacao, 5)
    return max(candidatos, key=lambda x: x['aptidao'])

# Cruzamento
def cruzamento(pai1, pai2):
    ponto = random.randint(0, N - 1)
    genes = pai1['genes'][:ponto] + [g for g in pai2['genes'] if g not in pai1['genes'][:ponto]]
    return {'genes': genes, 'aptidao': avaliar_aptidao(genes)}

# Mutação
def mutacao(individuo):
    if random.random() < TAXA_MUTACAO:
        i = random.randint(0, N - 1)
        j = random.randint(0, N - 1)
        individuo['genes'][i], individuo['genes'][j] = individuo['genes'][j], individuo['genes'][i]
        individuo['aptidao'] = avaliar_aptidao(individuo['genes'])

# Evoluir população
def evoluir_populacao(populacao):
    nova_geracao = populacao[:10]  # Elitismo
    while len(nova_geracao) < TAMANHO_POPULACAO:
        pai1 = selecionar_pai(populacao)
        pai2 = selecionar_pai(populacao)
        filho = cruzamento(pai1, pai2)
        mutacao(filho)
        nova_geracao.append(filho)
    return sorted(nova_geracao, key=lambda x: x['aptidao'], reverse=True)

# Visualizar tabuleiro
def plotar_tabuleiro(genes, geracao, aptidao):
    plt.clf()
    tabuleiro = [["." for _ in range(N)] for _ in range(N)]
    for col, row in enumerate(genes):
        tabuleiro[row][col] = "Q"
    plt.imshow([[1 if c == "Q" else 0 for c in row] for row in tabuleiro], cmap="binary")
    plt.title(f"Geração {geracao} | Aptidão: {aptidao}")
    plt.pause(0.1)

# Executar algoritmo genético
def executar_algoritmo_genetico():
    populacao = criar_populacao()
    for geracao in range(1, MAX_GERACOES + 1):
        melhor = populacao[0]
        if melhor['aptidao'] == (N * (N - 1)) // 2:
            print(f"Solução encontrada na geração {geracao}: {melhor['genes']}")
            plotar_tabuleiro(melhor['genes'], geracao, melhor['aptidao'])
            return
        if geracao % VISUALIZAR_A_CADA == 0:
            print(f"Geração {geracao} | Melhor aptidão: {melhor['aptidao']}")
            plotar_tabuleiro(melhor['genes'], geracao, melhor['aptidao'])
        populacao = evoluir_populacao(populacao)

    print("Nenhuma solução perfeita encontrada.")
    plotar_tabuleiro(populacao[0]['genes'], MAX_GERACOES, populacao[0]['aptidao'])

# Rodar
plt.ion()  # Ativa modo interativo do matplotlib
executar_algoritmo_genetico()
plt.ioff()
plt.show()
