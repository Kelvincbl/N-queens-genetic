import random
import matplotlib.pyplot as plt
import time

# Parâmetros configuráveis
N = 8
POPULATION_SIZE = 200
MUTATION_RATE = 0.10
MAX_GENERATIONS = 1000
VISUALIZE_EVERY = 50

# Avaliação da aptidão: número de pares de rainhas que não se atacam
def avaliar_aptidao(genes):
    nao_atacando = 0
    for i in range(N):
        for j in range(i + 1, N):
            if genes[i] != genes[j] and abs(genes[i] - genes[j]) != abs(i - j):
                nao_atacando += 1
    return nao_atacando

# Criação de um indivíduo
def criar_individuo():
    genes = list(range(N))
    random.shuffle(genes)
    aptidao = avaliar_aptidao(genes)
    return {'genes': genes, 'aptidao': aptidao}

# Criação da população inicial
def criar_populacao():
    return sorted([criar_individuo() for _ in range(POPULATION_SIZE)], key=lambda x: x['aptidao'], reverse=True)

# Seleção por torneio
def selecionar_pai(populacao):
    candidatos = random.sample(populacao, 5)
    return max(candidatos, key=lambda x: x['aptidao'])

# Cruzamento (crossover)
def cruzamento(pai1, pai2):
    ponto = random.randint(0, N - 1)
    genes = pai1['genes'][:ponto] + [g for g in pai2['genes'] if g not in pai1['genes'][:ponto]]
    return {'genes': genes, 'aptidao': avaliar_aptidao(genes)}

# Mutação (swap entre duas posições)
def mutacao(individuo):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(N), 2)
        individuo['genes'][i], individuo['genes'][j] = individuo['genes'][j], individuo['genes'][i]
        individuo['aptidao'] = avaliar_aptidao(individuo['genes'])

# Evolução da população
def evoluir_populacao(populacao):
    nova_geracao = populacao[:10]  # elitismo
    while len(nova_geracao) < POPULATION_SIZE:
        pai1 = selecionar_pai(populacao)
        pai2 = selecionar_pai(populacao)
        filho = cruzamento(pai1, pai2)
        mutacao(filho)
        nova_geracao.append(filho)
    return sorted(nova_geracao, key=lambda x: x['aptidao'], reverse=True)

# Visualização do tabuleiro
def plotar_tabuleiro(genes, geracao, aptidao):
    plt.clf()
    tabuleiro = [[0]*N for _ in range(N)]
    for col, row in enumerate(genes):
        tabuleiro[row][col] = 1
    plt.imshow(tabuleiro, cmap="binary")
    plt.title(f"Geração {geracao} | Aptidão: {aptidao}")
    plt.pause(0.1)

# Execução do algoritmo genético
def executar_algoritmo_genetico():
    inicio = time.time()
    populacao = criar_populacao()
    for geracao in range(1, MAX_GENERATIONS + 1):
        melhor = populacao[0]
        if melhor['aptidao'] == (N * (N - 1)) // 2:
            fim = time.time()
            print(f"Solução encontrada na geração {geracao}: {melhor['genes']} | Tempo: {fim - inicio:.2f}s")
            plotar_tabuleiro(melhor['genes'], geracao, melhor['aptidao'])
            return
        if geracao % VISUALIZE_EVERY == 0:
            print(f"Geração {geracao} | Melhor aptidão: {melhor['aptidao']}")
            plotar_tabuleiro(melhor['genes'], geracao, melhor['aptidao'])
        populacao = evoluir_populacao(populacao)

    fim = time.time()
    print(f"Nenhuma solução perfeita encontrada após {MAX_GENERATIONS} gerações. Tempo: {fim - inicio:.2f}s")
    plotar_tabuleiro(populacao[0]['genes'], MAX_GENERATIONS, populacao[0]['aptidao'])

# Executa com visualização
plt.ion()
executar_algoritmo_genetico()
plt.ioff()
plt.show()
