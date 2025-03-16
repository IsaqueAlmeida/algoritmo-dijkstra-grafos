# Algoritmo de Dijkstra

## Introdução

O **Algoritmo de Dijkstra** é um dos algoritmos mais utilizados para encontrar o caminho mais curto em um grafo. Ele foi desenvolvido por Edsger W. Dijkstra em 1956 e é amplamente utilizado em redes de computadores, sistemas de navegação, engenharia de transporte e muito mais.

Este repositório contém uma implementação do algoritmo de Dijkstra em Python.

## Aplicações do Algoritmo de Dijkstra

- **Redes de Computadores**: Encontrar a rota mais curta entre servidores ou roteadores.
- **Sistemas de Navegação**: Aplicativos de mapas utilizam Dijkstra para determinar a melhor rota entre dois pontos.
- **Planejamento de Transporte**: Encontrar a rota mais curta entre cidades ou pontos de interesse.
- **Jogos e IA**: Usado em pathfinding para movimentação de personagens e NPCs.

## Como Funciona o Algoritmo

O algoritmo de Dijkstra segue os seguintes passos:

1. Inicializa todos os vértices com uma distância infinita, exceto o vértice inicial (fonte), que recebe distância 0.
2. Cria uma fila de prioridade para processar os vértices.
3. Iterativamente, seleciona o vértice com a menor distância, relaxa suas arestas e atualiza as distâncias dos vizinhos.
4. Repete o processo até que todos os vértices tenham sido processados.

---

## Explicação do Código

### Classe `Grafo`

```python
class Grafo:
    def __init__(self, orientado=False):
        self._lista_de_adjacencias = dict()
        self.orientado = orientado
```
A classe `Grafo` representa um grafo usando listas de adjacências. O parâmetro `orientado` define se o grafo é direcionado ou não.

#### Métodos principais:

- `vertices()`: Retorna todos os vértices do grafo.
- `arestas()`: Retorna todas as arestas do grafo.
- `inserir_arestas(u, v, custo)`: Adiciona uma aresta entre dois vértices com um custo associado.
- `imprimir()`: Exibe as arestas do grafo e o custo total.

### Implementação do Algoritmo de Dijkstra

```python
def dijkstra(grafo, fonte):
    VAZIO = None
    INFINITO = sum([aresta[-1] for aresta in grafo.arestas()])
    antecessor_e_distancia = {}
    fila = []
```
O algoritmo começa definindo:
- `VAZIO` como `None` para indicar vértices ainda não processados.
- `INFINITO` como um valor alto, representando distâncias ainda não calculadas.
- `antecessor_e_distancia` armazena os antecessores e distâncias mínimas.
- `fila` é usada para processar os vértices.

#### Inicialização
```python
for u in grafo.vertices():
    antecessor_e_distancia[u] = VAZIO, INFINITO
    fila.append(u)

antecessor_e_distancia[fonte] = VAZIO, 0
```
Todos os vértices começam com distância infinita, exceto o vértice fonte, que recebe `0`.

#### Processamento dos Vértices
```python
while fila:
    selecao_dist_vertice = [
        (ant_dist[-1], u)
        for u, ant_dist, in antecessor_e_distancia.items()
        if u in fila
    ]

    menor_dist, vertice_menor_dist = sorted(selecao_dist_vertice)[0]
    fila.remove(vertice_menor_dist)
```
O algoritmo seleciona o vértice com a menor distância atual e o remove da fila.

#### Relaxamento das Arestas
```python
for v, dist_v in grafo._lista_de_adjacencias[vertice_menor_dist]:
    if v in fila:
        dist = menor_dist + dist_v
        if dist < antecessor_e_distancia[v][-1]:
            antecessor_e_distancia[v] = vertice_menor_dist, dist
```
Se a nova distância encontrada for menor que a distância armazenada, ela é atualizada.

### Função para Determinar o Caminho
```python
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
```
Essa função reconstrói o caminho percorrido com base nos antecessores armazenados.

---

## Exemplo de Uso

```python
arestas = [
    ('A', 'B', 3), ('A', 'X', 2), ('A', 'H', 5),
    ('B', 'C', 4), ('B', 'X', 3), ('B', 'E', 3),
    ('C', 'H', 3), ('C', 'E', 3), ('C', 'D', 2),
    ('D', 'G', 3), ('D', 'F', 4), ('E', 'F', 5),
    ('G', 'H', 5)
]

grafo = Grafo()
grafo.inserir_aresta(arestas)
antecessor_distancia = dijkstra(grafo, 'E')
```
Esse trecho cria um grafo com as arestas definidas e executa o algoritmo de Dijkstra a partir do vértice `E`.

## Exemplo de Saída

```bash
De A para G, distância = 8
Caminho: E -> B -> A distância: 6
De A para H, distância = 6
Caminho: E -> B -> A distância: 6
De A para D, distância = 5
Caminho: E -> B -> A distância: 6
De A para A, distância = 6
Caminho: E -> B -> A distância: 6
De A para E, distância = 0
Caminho: E -> B -> A distância: 6
De A para B, distância = 3
Caminho: E -> B -> A distância: 6
De A para F, distância = 5
Caminho: E -> B -> A distância: 6
De A para C, distância = 3
Caminho: E -> B -> A distância: 6
De A para X, distância = 6
Caminho: E -> B -> A distância: 6
```

---

## Contato

- **GitHub:** [Isaque Almeida](https://github.com/IsaqueAlmeida)
- **LinkedIn:** [Isaque Almeida](https://www.linkedin.com/in/isaque-f-s-almeida/)

