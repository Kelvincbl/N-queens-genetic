# N-queens-genetic

# Algoritmo Genético para o Problema das N-Rainhas

Este projeto implementa uma solução para o clássico problema das N-Rainhas utilizando Algoritmos Genéticos com visualização do progresso.

## Objetivo

Colocar N rainhas em um tabuleiro NxN de forma que nenhuma se ataque, ou seja, sem rainhas na mesma linha, coluna ou diagonal.

## Como funciona

O algoritmo segue os seguintes passos:

1. **Inicialização**: cria uma população de indivíduos (possíveis soluções).
2. **Avaliação**: calcula a aptidão de cada indivíduo (quantas rainhas não se atacam).
3. **Seleção**: escolhe os melhores indivíduos para reprodução.
4. **Cruzamento**: combina dois indivíduos para formar um novo.
5. **Mutação**: altera aleatoriamente o novo indivíduo.
6. **Substituição**: cria uma nova geração com os melhores indivíduos.

## Parâmetros

- `N`: número de rainhas (default = 8)
- `TAMANHO_POPULACAO`: tamanho da população inicial
- `TAXA_MUTACAO`: chance de um gene ser alterado
- `MAX_GERACOES`: número máximo de gerações
- `VISUALIZAR_A_CADA`: gerações para atualizar o gráfico

## Resultados dos Testes

| POPULATION_SIZE | MUTATION_RATE | Tempo médio (segundos) | Geração com solução |
|------------------|----------------|--------------------------|----------------------|
| 100              | 0.05           | 4.2                      | 86                   |
| 50               | 0.05           | 7.8                      | 134                  |
| 200              | 0.05           | 3.9                      | 72                   |
| 100              | 0.01           | 6.5                      | 110                  |
| 100              | 0.10           | 3.6                      | 58                   |
| 200              | 0.10           | 3.3                      | 52                   |

> Os testes mostraram que o melhor desempenho foi obtido com `POPULATION_SIZE = 200` e `MUTATION_RATE = 0.10`.

## Conclusão

O desempenho melhora com populações maiores e taxas de mutação moderadas a altas, pois aumentam a diversidade genética e evitam estagnação em mínimos locais.

---
