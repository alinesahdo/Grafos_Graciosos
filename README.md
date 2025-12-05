# Verificador de Grafos Graciosos

Este repositório contém uma implementação, em Python, para verificar se um grafo admite um **rotulamento gracioso (graceful labeling)**.

## Objetivos

- Implementar um verificador utilizando:
  - **Força bruta** (enumerando todas as permutações), adequado para grafos pequenos.
  - **Backtracking com poda heurística**, permitindo explorar grafos um pouco maiores.
- Ilustrar como funciona o espaço de busca do problema.
- Fornecer código simples, didático e sem dependências externas.

---

## Estrutura

src/

├── brute_force.py # Algoritmo simples por força bruta

├── backtracking.py # Versão com backtracking e podas heurísticas

└── examples.py # Exemplos de execução

examples/

├── P4.txt # Grafo caminho de 4 vértices

├── star5.txt # Estrela com 5 vértices

└── tree1.txt # Outro exemplo de árvore

