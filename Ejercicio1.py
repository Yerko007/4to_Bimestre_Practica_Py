class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.apuntador = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
            return

        actual = self.cabeza

        while actual.apuntador is not None:
            actual = actual.apuntador

        actual.apuntador = nuevo

    def imprimir(self):
        actual = self.cabeza

        while actual is not None:
            print(actual.dato)
            actual = actual.apuntador

        print("Fin de la lista")


# Programa principal
mi_lista = ListaEnlazada()

# Insertar elementos
mi_lista.insertar(10)
mi_lista.insertar(20)
mi_lista.insertar(30)

# Imprimir lista
mi_lista.imprimir()