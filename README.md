# Grafos_Graciosos

Repositório com implementações para verificar se um grafo admite um **rotulamento gracioso** (graceful labeling).

Este trabalho acompanha o relatório **"Grafos Rotulados e o Problema dos Grafos Graciosos"** (Aline Sahdo) — código em Python para testar instâncias pequenas e um verificador por backtracking com poda.

## Conteúdo
- `src/bruteforce.py` — implementação didática por força bruta (permutações).
- `src/backtrack.py` — verificador por backtracking com poda e ordenação por grau (recomendado).
- `examples/` — exemplos de grafos (formato JSON).
- `tests/` — testes `pytest`.
