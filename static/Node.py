class Node:
    neighbours: [] = []

    def __init__(self, name, g: object, h: object, f: object, p: object) -> object:
        self.g = g  # valor del camino de un nodo a otro
        self.h = h  # valor de la heuristica
        self.f = f  # costo total
        self.p = p  # nodo padre
        self.name = name

    def get_neighbours(self):
        return self.neighbours

    def set_neighbours(self, n):
        self.neighbours = n


class Utils:
    def __init__(self, data):
        self.nodos = data.get('nodos')
        self.aristas = data.get('aristas')
        self.origin = data.get('origin')
        self.destin = data.get('destin')

    def create_graph(self):
        graph = []
        graph.append(Node(self.origin.get('label'), 0, self.origin.get('heuristic'), 0, None))
        # for i in self.nodos:x
        #     if not i.get('label') == self.origin.get('label')
        #     graph.append(Node(i.get('label'), 0, 3, 4, 0))



# util = Utils(nodes)
# util.create_graph()