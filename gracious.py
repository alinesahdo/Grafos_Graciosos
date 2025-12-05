from itertools import permutations

def grafo_gracioso(vertices, arestas):
    m = len(arestas)                     # quantidade de arestas
    rotulos_possiveis = list(range(m+1)) # rotulos 0..m

    esperado = set(range(1, m+1))        # conjunto {1,...,m}

    # tenta todas as rotulacoes possiveis
    for perm in permutations(rotulos_possiveis, len(vertices)):
        f = {vertices[i]: perm[i] for i in range(len(vertices))}

        rotulos_arestas = set()
        valido = True

        for (u, v) in arestas:
            diferenca = abs(f[u] - f[v])

            if diferenca == 0 or diferenca > m or diferenca in rotulos_arestas:
                valido = False
                break

            rotulos_arestas.add(diferenca)

        # agora checa se é exatamente {1,...,m}
        if valido and rotulos_arestas == esperado:
            return True, f

    return False, None


vertices = [1,2,3] 
arestas = [(1,2),(2,3)]

resultado, rotulamento = grafo_gracioso(vertices, arestas)

if resultado:
    print("O grafo e gracioso!")
    print("Rotulamento encontrado:", rotulamento)
else:
    print("O grafo NAO e gracioso.")
