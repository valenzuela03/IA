from Nodo import Nodo
class Arbol:
    def __init__(self):
        self.start = None

    def search_node(self, name):
        return self._search_node_current(self.start, name)

    def _search_node_current(self, current, name):
        if current is None:
            return None
        if name == current.name:
            return current
        if name < current.name:
            return self._search_node_current(current.left, name)
        else:
            return self._search_node_current(current.right, name)

    def insert_node(self, name):
        self.start = self._insert_node_recursive(self.start, name)

    def _insert_node_recursive(self, current, name):
        if current is None:
            return Nodo(name)
        if name < current.name:
            current.left = self._insert_node_recursive(current.left, name)
        elif name > current.name:
            current.right = self._insert_node_recursive(current.right, name)
        return current

    def print_recursive(self):
        self._print_recursive(self.start)

    def _print_recursive(self, current):
        if current is None:
            return
        self._print_recursive(current.left)
        print(current.name)
        self._print_recursive(current.right)

def main():
    arbol = Arbol()
    arbol.insert_node(1)
    arbol.insert_node(2)
    arbol.insert_node(9)
    arbol.insert_node(4)
    arbol.insert_node(7)
    arbol.insert_node(2)
    arbol.insert_node(78)
    arbol.insert_node(34)
    arbol.print_recursive()

if __name__ == '__main__': 
    main()