import sys
import pygame

# Función para encontrar el vértice con la distancia mínima
def encontrar_vertice_minimo(distancias, visitados):
    minimo = sys.maxsize
    minimo_indice = -1
    for v in range(len(distancias)):
        if distancias[v] < minimo and not visitados[v]:
            minimo = distancias[v]
            minimo_indice = v
    return minimo_indice

# Función para imprimir la solución actual
def imprimir_solucion_parcial(distancias):
    print("Vértice \t Distancia desde el origen")
    for nodo in range(len(distancias)):
        print(nodo, "\t", distancias[nodo])

# Función para implementar el algoritmo de Dijkstra paso a paso
def dijkstra_paso_a_paso(grafo, origen):
    num_vertices = len(grafo)
    distancias = [sys.maxsize] * num_vertices
    distancias[origen] = 0
    visitados = [False] * num_vertices

    for _ in range(num_vertices):
        imprimir_solucion_parcial(distancias)

        u = encontrar_vertice_minimo(distancias, visitados)
        visitados[u] = True

        for v in range(num_vertices):
            if (
                not visitados[v]
                and grafo[u][v] != 0
                and distancias[u] + grafo[u][v] < distancias[v]
            ):
                distancias[v] = distancias[u] + grafo[u][v]

    imprimir_solucion_parcial(distancias)
    return distancias

# Inicialización de pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulador de Dijkstra")

# Función para dibujar el grafo con las soluciones
def dibujar_grafo(grafo, solucion):
    screen.fill((255, 255, 255))
    num_vertices = len(grafo)
    for i in range(num_vertices):
        for j in range(num_vertices):
            if grafo[i][j] > 0:
                pygame.draw.line(
                    screen,
                    (0, 0, 0),
                    (50 + i * 100, 50),
                    (50 + j * 100, 50),
                    2,
                )

    for i in range(num_vertices):
        pygame.draw.circle(screen, (255, 0, 0), (50 + i * 100, 50), 20)
        pygame.font.init()
        font = pygame.font.Font(None, 36)
        text = font.render(str(solucion[i]), True, (0, 0, 0))
        screen.blit(text, (40 + i * 100, 20))

    pygame.display.update()

# Ejemplo de uso
grafo = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0],
]