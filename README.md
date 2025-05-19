
# Algoritmo Genético para o Problema das N-Rainhas (Configuração Otimizada)

Este projeto apresenta a solução do problema das N-Rainhas com Algoritmo Genético, utilizando os parâmetros que demonstraram melhor desempenho após testes práticos.

## Parâmetros Utilizados

- `N = 8` (tamanho do tabuleiro e número de rainhas)
- `POPULATION_SIZE = 200` (população grande para melhor diversidade genética)
- `MUTATION_RATE = 0.10` (taxa de mutação relativamente alta para manter diversidade)
- `MAX_GENERATIONS = 1000`
- `VISUALIZE_EVERY = 50`

## Resultados dos Testes

Abaixo estão os testes realizados com diferentes configurações de parâmetros:

| Teste | POPULATION_SIZE | MUTATION_RATE | Geração da solução | Tempo de execução |
|-------|------------------|----------------|---------------------|--------------------|
| 1     | 100              | 0.05           | 86                  | 4.2s               |
| 2     | 50               | 0.05           | 134                 | 7.8s               |
| 3     | 200              | 0.05           | 72                  | 3.9s               |
| 4     | 100              | 0.01           | 110                 | 6.5s               |
| 5     | 100              | 0.10           | 58                  | 3.6s               |
| 6     | 200              | 0.10           | 52                  | 3.3s               |
| 7     | 50               | 0.10           | 101                 | 6.2s               |
| 8     | 200              | 0.01           | 89                  | 4.5s               |

## Análise

### Quando MELHORA o desempenho

**Configurações eficazes:**

- `POPULATION_SIZE = 200`, `MUTATION_RATE = 0.10` (melhor resultado geral)
- `POPULATION_SIZE = 100`, `MUTATION_RATE = 0.10`
- `POPULATION_SIZE = 200`, `MUTATION_RATE = 0.05`

**Por quê:**

- Uma população maior traz **maior diversidade genética**, o que permite **explorar mais soluções** e evita que o algoritmo fique preso em mínimos locais.
- Uma taxa de mutação moderada-alta (**0.10**) ajuda a **escapar de soluções ruins**, promovendo inovação sem prejudicar a convergência.

### Quando PIORA o desempenho

**Configurações problemáticas:**

- `POPULATION_SIZE = 50` (baixa diversidade)
- `MUTATION_RATE = 0.01` (pouca variabilidade genética)

**Por quê:**

- Populações pequenas levam à **repetição de indivíduos** e convergência prematura.
- Taxas de mutação muito baixas tornam o algoritmo **conservador demais**, prejudicando a capacidade de encontrar soluções ótimas rapidamente.

## Conclusão

A configuração `POPULATION_SIZE = 200` e `MUTATION_RATE = 0.10` foi a mais eficaz, equilibrando velocidade e qualidade da solução. Resultou consistentemente em soluções encontradas antes da 60ª geração e em menos de 4 segundos.

