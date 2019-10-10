from static.Node import Node
from collections import OrderedDict


class AStar:
    # Crear lista abierta para nodos (cada nodo tiene atributos g, h, f, p)
    list_open = dict()
    # Crear lista cerrada para nodos (cada nodo tiene atributos g, h, f, p)
    list_close = OrderedDict()
    # Crear lista vecinos para nodos (cada nodo tiene atributos g, h, f, p)
    list_neighbour = dict()
    # Crear nodo actual
    node_actual = None

    list = []
    node_ini = None

    def __init__(self, data: dict, origin, dest):
        self.graph = data
        self.nodes = data.keys()
        self.ini = origin
        self.end = dest
        self.node_ini = Node(origin, 0, self.graph[origin].get('heuristic'), 0, None)
        print(self.graph)
        # self.node_end = Node(self.end.get('label'), 0, self.end.get('heuristic'), 0, None)

    # def a_start_search(self, node_ini: Node, node_end: Node, ):

    def a_start_search(self):
        if self.node_ini.name == self.end:
            return self.node_ini
        else:
            res = self.sub_search(self.node_ini, self.end);
            self.list = []
            return res

    def sub_search(self, node_ini: Node, node_end):
        short_list = []
        # nodo actual es igual al nodo inicial
        self.node_actual = node_ini
        # Insertar nodo inicial en lista cerrada con g=0 (costo de nodo)
        self.node_actual.g = 0
        self.list_close[self.node_actual.name] = self.node_actual
        # Mientras nodo final no se encuentre en la lista cerrada
        last = list(self.list_close)[-1]
        while last != node_end:
            # Nodo actual = último elemento agregado a la lista cerrada
            self.node_actual = self.list_close[last]
            # Agregar los nodos vecinos del nodo actual en la lista vecinos excepto nodos que
            # estén en la lista cerrada
            self.list_neighbour = self.add_neighbour_of_node(self.node_actual.name)
            self.calc_data()
            self.process_list()
            last = list(self.list_close)[-1]
        return self.make_list_short()

    # saca los vecinos de un nodo

    def add_neighbour_of_node(self, key):
        alNey = dict()
        # sacar los vecinos del nodo
        neighbours: dict = self.graph[key].get('childs')
        for a in neighbours:
            # label = n.
            # value = i.get('value')
            if a not in self.list_close:
                alNey[a] = Node(a, neighbours[a], self.graph[a].get('heuristic'), 0, self.node_actual)

        # sacar nodos que no se encuentren
        # for i in aux_neighbours:
        #     if not i in self.list_close:
        #         neighbours.append(i)
        return alNey

    def get_node_on_label(self, label):
        for i in self.nodes:
            if label == i.get('label'):
                return i.get('heuristic')

    # para todo nodo de la lista vecinos calcular los atributos
    # g = g del nodo actual + costo del nodo vecino al nodo actual
    # h = costo (directo) aproximado desde el nodo vecino al nodo final
    # f = g + h
    # p = nodo actual
    # fin para
    def calc_data(self):
        for no in self.list_neighbour:
            self.list_neighbour[no].g = self.list_neighbour[
                                            no].g + self.node_actual.g  # distncia del nodo alcual al nodo vecino
            self.list_neighbour[no].h = self.list_neighbour[no].h
            self.list_neighbour[no].f = self.list_neighbour[no].h + self.list_neighbour[no].g
            self.list_neighbour[no].p = self.node_actual

    # Para cada nodo de la lista vecinos
    #   Si el nodo vecino no se encuentra en la lista abierta ni en la lista cerrada
    #       Copiar nodo vecino en la lista abierta
    #   Fin si
    #   Si no
    #       Si nodo vecino ya se encuentra en la lista abierta
    #           Si g del nodo vecino < al g del mismo nodo de la lista abierta
    #               Actualizar atributos del nodo de la lista abierta con atributos del mismo nodo de la lista vecinos
    #           Fin si
    #       Fin si
    #   Fin si no
    # Fin para
    def process_list(self):
        for i in self.list_neighbour:
            if i not in self.list_open and i not in self.list_close:
                self.list_open[i] = self.list_neighbour[i]
            else:
                if i in self.list_open:
                    if self.list_neighbour[i].g < self.list_open[i].g:
                        self.list_open[i].g = self.list_neighbour[i].g
                        self.list_open[i].h = self.list_neighbour[i].h
                        self.list_open[i].p = self.list_neighbour[i].p
                        self.list_open[i].f = self.list_neighbour[i].f

        self.list_neighbour = dict()
        self.append_min_node()
        # return self.make_list_short()

    def search_node_for_name(self, list: [Node], name):
        res = False
        for i in list:
            if i.name == name:
                res = True
                return res
        return res

    def get_node_for_name(self, list: [Node], node: Node) -> Node:
        for i in list:
            if i.name == node.name:
                return i

    def append_min_node(self):
        min = None
        for i in self.list_open:
            if min is None:
                min = self.list_open[i]
            if self.list_open[i].f <= min.f:
                min = self.list_open[i]
        self.list_open.pop(min.name)
        self.list_close[min.name] = min

    def make_list_short(self):
        res = []
        for i in self.list_close:
            if self.list_close[i].p != None:
                res.append([i, self.list_close[i].p.name])
            else:
                res.append([i])
        res.reverse()
        self.list = []
        return self.get_ress(res, self.end, self.ini)

    def get_ress(self, res, end1, ini1):

        for i in res:
            if end1 == i[0]:
                self.list.append(i)
                if i[0] != ini1:
                    self.list + self.get_ress(res, i[1], ini1)
        return self.list

    def funtion_test(self):
        return "te conectaste al servicio"


nodes = {
    "aristas": [
        {"pointA": {"x": 365, "y": 455, "heuristic": 362, "label": "a"},
         "pointB": {"x": 522, "y": 287, "label": "b"},
         "value": 230},
        {"pointA": {"x": 522, "y": 287, "heuristic": 228, "label": "b"},
         "pointB": {"x": 722, "y": 396, "label": "c"},
         "value": 228}
    ],
    "nodos": [
        {"x": 365, "y": 455, "heuristic": 362, "label": "a"},
        {"x": 522, "y": 287, "heuristic": 228, "label": "b"},
        {"x": 722, "y": 396, "heuristic": 0, "label": "c"}
    ],
    "origin": {"x": 522, "y": 287, "heuristic": 228, "label": "b"},
    "destin": {"x": 722, "y": 396, "heuristic": 0, "label": "c"}
}
