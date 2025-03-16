# Iniciando com a classe Grafo
class Grafo:
    def __init__(self, orientado=False):
        self._lista_de_adjacencias = dict()
        self.orientado = orientado

    def vertices(self):  # retorna os nomes dos vértices
        return set(self._lista_de_adjacencias.keys())

    def arestas(self, v_origem=None):
        # retorna as arestas do vértices v_origem ou do grafo inteiro
        if v_origem:
            # obter as arestas do vértices
            return self.v_arestas(v_origem)
        # retorna as arestas do grafo inteiro
        arestas_do_grafo = []
        for v_origem in self.vertices():
            # acumulará as arestas de todos os vértices
            arestas_do_grafo += self.v_arestas(v_origem)
            return arestas_do_grafo

    def v_arestas(self, v_origem):
        # retorna as arestas do vértices v_origem
        # retorna as arestas de um vértices
        arestas = []
        for v_destino, custo in self._lista_de_adjacencias[v_origem]:
            arestas.append((v_origem, v_destino, custo))
        return arestas

    def inserir_arestas(self, u, v, custo):
        # cria uma aresta entre os vértices u e v
        # cria uma chave u com valor lista vazia no dicionário
        # se a chave u não existir
        self._lista_de_adjacencias.setdefault(u, [])

        # cria uma chave v com o valor lista vazia no dicionário
        # se a chave v não existir
        # se a chave v não existir
        self._lista_de_adjacencias.setdefault(v, [])

        # adiciona a aresta ao vértices u
        self._lista_de_adjacencias[u].append((v, custo))

        if not self.orientado:
            # se é um grafo orientado
            # adiciona a aresta ao vértices v
            self._lista_de_adjacencias[v].append((u, custo))

    def inserir_aresta(self, arestas):
        # insere todas as arestas no grafo
        for aresta in arestas:
            self.inserir_arestas(*aresta)

    def imprimir(self):
        total = 0
        for u, v, custo in self.arestas():
            print("({}, {}, {})".format(u, v, custo), end="")
            total += custo
        if not self.orientado:
            # divide por 2 para desconar a duplicidade
            total = total / 2
        print("")
        print("Custo: {}".format(total))


def dijkstra(grafo, fonte):
    VAZIO = None
    INFINITO = sum([aresta[-1] for aresta in grafo.arestas()])
    antecessor_e_distancia = {}
    fila = []

    """
    inicia os antecessor_e_custo de todas as vértices com o valor: VAZIO,
    INFINITO
    """
    for u in grafo.vertices():
        antecessor_e_distancia[u] = VAZIO, INFINITO
        fila.append(u)

    # início
    antecessor_e_distancia[fonte] = VAZIO, 0

    while fila:
        # pega as distâncias de vértices que estão na fila
        selecao_dist_vertice = [
            (ant_dist[-1], u)
            for u, ant_dist, in antecessor_e_distancia.items()
            if u in fila
        ]

        # pega a menor distância
        menor_dist, vertice_menor_dist = sorted(selecao_dist_vertice)[0]

        # remove o vértice u da fila
        fila.remove(vertice_menor_dist)

        # para cada vizinho de vertice_menor_dist
        for v, dist_v in grafo._lista_de_adjacencias[vertice_menor_dist]:
            if v in fila:
                dist = menor_dist + dist_v
                if dist < antecessor_e_distancia[v][-1]:
                    antecessor_e_distancia[v] = vertice_menor_dist, dist
    return antecessor_e_distancia


def caminho(antecessor_distancia, fonte, destino):
    rota = [destino]
    distancia = antecessor_distancia[destino][1]
    while True:
        antecessor = antecessor_distancia[destino][0]
        if antecessor is None:
            break
        rota.insert(0, antecessor)
        destino = antecessor
    return " -> ".join(rota) + " distância: {}".format(distancia)

# Testando o algoritmo de Dijkstra


print("""
 O programa apresenta o custo mínimo de ir de um ponto A a todos os demais,
 usando o algoritmo de Dijkstra.
""")

arestas = [
    ('A', 'B', 3),
    ('A', 'X', 2),
    ('A', 'H', 5),
    ('B', 'C', 4),
    ('B', 'X', 3),
    ('B', 'E', 3),
    ('C', 'H', 3),
    ('C', 'E', 3),
    ('C', 'D', 2),
    ('D', 'G', 3),
    ('D', 'F', 4),
    ('E', 'F', 5),
    ('G', 'H', 5)
]

# Criando o objeto grafo
grafo = Grafo()

# inserindo as arestas do grafo
grafo.inserir_aresta(arestas)

# executa o algoritmo de Dijkstra
antecessor_distancia = dijkstra(grafo, 'E')


for u, ant_dist in antecessor_distancia.items():
    print('De A para {}, distância = {}'.format(u, ant_dist[1]))
    print("Caminho: {}".format(caminho(antecessor_distancia, u, "A")))
