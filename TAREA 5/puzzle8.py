import random
import heapq

def heuristica(puzzle, goal):
    distancia = 0
    meta = {valor: (i, j) for i, row in enumerate(goal) for j, valor in enumerate(row)}
    for i in range(3):
        for j in range(3):
            valor = puzzle[i][j]
            if valor != 0:
                meta_i, meta_j = meta[valor]
                distancia += abs(meta_i - i) + abs(meta_j - j)
    return distancia

def busca_estrella(start, goal):
    visitado = set()
    cabeza = []
    heapq.heappush(cabeza, start)
    while cabeza:
        actual = heapq.heappop(cabeza)
        if actual.puzzle == goal.puzzle:
            return actual
        visitado.add(str(actual.puzzle))
        for siguiente_nodo in actual.encuentra_siguiente_nodo():
            if str(siguiente_nodo.puzzle) not in visitado:
                heapq.heappush(cabeza, siguiente_nodo)
    return None


class Nodo:
    def __init__(self, puzzle, movimiento, profundidad, heuristica, anterior):
        self.profundidad = profundidad
        self.puzzle = puzzle
        self.movimiento = movimiento
        self.heuristica = heuristica
        self.anterior = anterior

    def __lt__(self, other):
        return (self.profundidad + self.heuristica) < (other.profundidad + other.heuristica)


    def mover_pieza(self, movimiento):
        puzzle = self.puzzle
        nuevo_puzzle = [row.copy() for row in puzzle]
        x, y = next((i, j) for i in range(3) for j in range(3) if puzzle[i][j] == 0)

        if movimiento == 'arriba':
            if x > 0:
                nuevo_puzzle[x][y], nuevo_puzzle[x - 1][y] = nuevo_puzzle[x - 1][y], nuevo_puzzle[x][y]
                return nuevo_puzzle
        elif movimiento == 'abajo':
            if x < 2:
                nuevo_puzzle[x][y], nuevo_puzzle[x + 1][y] = nuevo_puzzle[x + 1][y], nuevo_puzzle[x][y]
                return nuevo_puzzle
        elif movimiento == 'izq':
            if y > 0:
                nuevo_puzzle[x][y], nuevo_puzzle[x][y - 1] = nuevo_puzzle[x][y - 1], nuevo_puzzle[x][y]
                return nuevo_puzzle
        elif movimiento == 'der':
            if y < 2:
                nuevo_puzzle[x][y], nuevo_puzzle[x][y + 1] = nuevo_puzzle[x][y + 1], nuevo_puzzle[x][y]
                return nuevo_puzzle
        return None

    def encuentra_siguiente_nodo(self):
        siguiente_nodos = []
        movimientos = ['arriba', 'abajo', 'izq', 'der']
        for movimiento in movimientos:
            nuevo_puzzle = self.mover_pieza(movimiento)
            if nuevo_puzzle is not None:
                siguiente_nodos.append(Nodo(nuevo_puzzle, movimiento, self.profundidad + 1, 
                heuristica(nuevo_puzzle, [[1, 2, 3], [4, 5, 6], [7, 8, 0]]), self))
        return siguiente_nodos

    def siguiente_camino(self, start):
        camino = []
        actual = self
        while actual != start:
            camino.append(actual)
            actual = actual.anterior
        camino.append(start)
        camino.reverse()
        return camino

    def print(self):
        for row in self.puzzle:
            print(' '.join(f'{num:2}' for num in row))
        print('')


def main():
    puzzle = [[6, 3, 1], 
              [5, 0, 8], 
              [2, 4, 7]]
    start = Nodo(puzzle, '', 0, 0, None)
    goal = Nodo([[1, 2, 3], 
                 [4, 5, 6], 
                 [7, 8, 0]], '', 0, 0, None)

    print('Puzzle inicial:')
    start.print()
    print("========================================")

    resultado = busca_estrella(start, goal)
    if resultado is not None:
        path = resultado.siguiente_camino(start)
        path.pop(0)
        for node in path:
            print(f'Movimiento: {node.movimiento}')
            node.print()

        print(f'Solucion encontrada en: {resultado.profundidad} movimientos')
    else:
        print('No se encontro solucion')


if __name__ == '__main__':
    main()
