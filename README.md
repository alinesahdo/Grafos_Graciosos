# Grafos Graciosos em Python

Este repositório contém implementações em Python para verificar se um grafo é **gracioso**.  
Um grafo é dito gracioso se existe uma função de rotulamento dos vértices com valores distintos em `{0,1,...,|E|}`, tal que cada aresta `(u,v)` receba o rótulo `|f(u)-f(v)|`, e os rótulos das arestas formem exatamente o conjunto `{1,2,...,|E|}`.

## Estrutura do repositório
- `gracious.py` → Verificação por força bruta usando permutações.
- `backtracking_gracious.py` → Versão otimizada usando backtracking com poda.

## Como executar
Clone o repositório e rode os arquivos diretamente com Python 3:

```bash
git clone https://github.com/usuario/graceful-graphs.git
cd graceful-graphs
python3 forca_bruta.py
python3 backtracking.py
