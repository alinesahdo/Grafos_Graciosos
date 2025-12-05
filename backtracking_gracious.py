def backtracking_rotulamento(vertices, arestas):
    n = len(vertices)
    m = len(arestas)

    vertices_ordenados = sorted(vertices)
    rotulos_possiveis = list(range(m + 1))

    f = {}
    usados_vertice = set()
    usados_arestas = set()
    esperado = set(range(1, m+1))

    solucao = None

    def backtrack(i):
        nonlocal solucao
        if i == n:
            if usados_arestas == esperado:
                solucao = f.copy()
                return True
            return False

        v = vertices_ordenados[i]

        for r in rotulos_possiveis:
            if r in usados_vertice:
                continue

            f[v] = r
            usados_vertice.add(r)

            valido = True
            novos_rotulos = set()
            for (u, w) in arestas:
                if u in f and w in f:
                    d = abs(f[u] - f[w])
                    if d == 0 or d > m:
                        valido = False
                        break
                    novos_rotulos.add(d)

            if valido:
                for d in novos_rotulos:
                    usados_arestas.add(d)

                if backtrack(i + 1):
                    return True

                for d in novos_rotulos:
                    usados_arestas.discard(d)

            usados_vertice.remove(r)
            del f[v]

        return False

    sucesso = backtrack(0)
    return sucesso, solucao if sucesso else None


if __name__ == "__main__":
    vertices = [1,2,3] 
    arestas = [(1,2),(2,3)]

    resultado, rotulamento = backtracking_rotulamento(vertices, arestas)

    if resultado:
        print("O grafo e gracioso!")
        print("Rotulamento encontrado:", rotulamento)
    else:
        print("O grafo NAO e gracioso.")