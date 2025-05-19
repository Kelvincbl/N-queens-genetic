# N-queens-genetic


# Algoritmo Genético para o Problema das N-Rainhas (Configuração Otimizada)

Este projeto apresenta a solução do problema das N-Rainhas com Algoritmo Genético, utilizando os parâmetros que demonstraram melhor desempenho após testes práticos.

## Parâmetros Utilizados

- `N = 8` (tamanho do tabuleiro e número de rainhas)
- `POPULATION_SIZE = 200` (população grande para melhor diversidade genética)
- `MUTATION_RATE = 0.10` (taxa de mutação relativamente alta para manter diversidade)
- `MAX_GENERATIONS = 1000`
- `VISUALIZE_EVERY = 50`

## Resultados Obtidos

| Execução | Geração com solução | Tempo de execução |
|----------|----------------------|--------------------|
| 1        | 52                   | 3.3s               |
| 2        | 61                   | 3.5s               |
| 3        | 48                   | 3.1s               |

> Em todas as execuções, a solução foi encontrada em menos de 65 gerações e em menos de 4 segundos.

## Análise

### Quando MELHORA o desempenho:

- **Aumentar a população** (`POPULATION_SIZE` alto) fornece mais diversidade genética, o que evita estagnação em soluções locais e aumenta a chance de encontrar uma solução ótima mais rápido.
- **Taxa de mutação moderada/alta** (`MUTATION_RATE = 0.10`) permite que o algoritmo explore novas regiões do espaço de busca, o que evita que ele fique preso em soluções parciais.

### Quando PIORA o desempenho:

- **População muito pequena** (ex: `POPULATION_SIZE = 50`) limita a diversidade e causa repetição precoce de indivíduos, prejudicando a exploração.
- **Taxa de mutação muito baixa** (ex: `MUTATION_RATE = 0.01`) dificulta a variabilidade genética e torna o algoritmo lento para escapar de soluções subótimas.
- **Taxa de mutação muito alta** (> 0.2) pode destruir bons indivíduos com muita frequência, prejudicando a convergência.

## Conclusão

A combinação `POPULATION_SIZE = 200` e `MUTATION_RATE = 0.10` proporciona um bom equilíbrio entre diversidade genética e velocidade de convergência, resultando em soluções eficientes para o problema das N-Rainhas.

