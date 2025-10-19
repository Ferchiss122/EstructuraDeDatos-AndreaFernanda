#Actividad1
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def print_tree(self, level=0):
        print(" " * level + self.data)
        for child in self.children:
            child.print_tree(level + 1)

root = Node("Root")
b = Node("Documentos")
c = Node("Escuela")
d = Node("Trabajo")
e = Node("Imágenes")
f = Node("Vacaciones")
g = Node("Familia")

root.add_child(b)
root.add_child(e)
b.add_child(c)
b.add_child(d)
e.add_child(f)
e.add_child(g)

root.print_tree()

#Actividad2
class NodoBinario:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end=' ')
        if self.right:
            self.right.inorder()

    def preorden(self):
        print(self.data, end=' ')
        if self.left:
            self.left.preorden()
        if self.right:
            self.right.preorden()

    def postorden(self):
        if self.left:
            self.left.postorden()
        if self.right:
            self.right.postorden()
        print(self.data, end=' ')


raiz = NodoBinario("A")
raiz.left = NodoBinario("B")
raiz.right = NodoBinario("C")
raiz.left.left = NodoBinario("D")
raiz.left.right = NodoBinario("E")
raiz.right.left = NodoBinario("F")

# Recorridos
print("Recorrido Inorden:")
raiz.inorder()

print("\nRecorrido Preorden:")
raiz.preorden()

print("\nRecorrido Postorden:")
raiz.postorden()

#Actividad 3
def altura(NodoBinario):
    if NodoBinario is None:
        return 0
    return 1 + max(altura(NodoBinario.left), altura(NodoBinario.right))

print("\nAltura del árbol:", altura(raiz))