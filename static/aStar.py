class Node:
    neighbours: [] = []

    def __init__(self, name, g: object, h: object, f: object, p: object) -> object:
        self.g = g
        self.h = h
        self.f = f
        self.p = p
        self.name = name

    def get_neighbours(self):
        return self.neighbours


class AStar:
    # Crear lista abierta para nodos (cada nodo tiene atributos g, h, f, p)
    list_open = []
    # Crear lista cerrada para nodos (cada nodo tiene atributos g, h, f, p)
    list_close = []
    # Crear lista vecinos para nodos (cada nodo tiene atributos g, h, f, p)
    list_neighbour: [Node] = []
    # Crear nodo actual
    node_actual: Node = None

    def a_start_search(self, node_ini: Node, node_end: Node):
        if node_ini == node_end:
            return node_ini
        else:
            return self.sub_search(node_ini, node_end, [])

    def sub_search(self, node_ini: Node, node_end: Node, grap):
        short_list = []
        # nodo actual es igual al nodo inicial
        self.node_actual = node_ini
        # Insertar nodo inicial en lista cerrada con g=0 (costo de nodo)
        self.node_actual.g = 0
        self.list_close.append(self.node_actual)
        # Mientras nodo final no se encuentre en la lista cerrada
        while self.list_close[-1].name != node_end.name:
            # Nodo actual = último elemento agregado a la lista cerrada
            node_actual = self.list_close[-1]
            # Agregar los nodos vecinos del nodo actual en la lista vecinos excepto nodos que
            # estén en la lista cerrada
            self.list_neighbour = self.add_neighbour(node_actual)
            self.calc_data()
            short_list = self.process_list()
        return short_list


    #saca los vecinos de un nodo
    def add_neighbour(self, node_ini: Node):
        neighbours = []
        # sacar los vecinos del nodo
        aux_neighbours = node_ini.get_neighbours()
        # sacar nodos que no se encuentren
        for i in aux_neighbours:
            if not i in self.list_close:
                neighbours.append(i)
        return neighbours

    # Para todo nodo de la lista vecinos calcular los atributos:
    # g = g del nodo actual + costo del nodo vecino al nodo actual
    # h = costo (directo) aproximado desde el nodo vecino al nodo final
    # f = g + h
    # p = nodo actual
    # fin para
    def calc_data(self):
        for no in self.list_neighbour:
            no.g = no.g + self.node_actual.g  # distncia del nodo alcual al nodo vecino
            no.h = no.h
            no.f = no.f + no.g
            no.p = self.node_actual

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
            if not self.search_node_for_name(self.list_open, i) and not self.search_node_for_name(self.list_close, i):
                self.list_open.append(i)
            else:
                if self.search_node_for_name(self.list_open, i):
                    node_list = self.get_node_for_name(self.list_open, i)
                    if i.g < node_list.g:
                        node_list.g = i.g
                        node_list.h = i.h
                        node_list.p = i.p
                        node_list.f = i.f
        self.list_neighbour = []
        self.list_close.append(self.select_min_node())
        return self.make_list_short(self.list_close)

    def search_node_for_name(self, list: [Node], node: Node):
        res = False
        for i in list:
            if i.name == node.name:
                res = True
                return res
        return res

    def get_node_for_name(self, list: [Node], node: Node) -> Node:
        for i in list:
            if i.name == node.name:
                return i

    def select_min_node(self) -> Node:
        min = None
        for i in self.list_open:
            if min is None:
                min = i
            if i.f <= min.f:
                min = i
        return min

    def make_list_short(self, list_res: []):
        return list_res.reverse()

    def funtion_test(self):
        return "te conectaste al servicio"
