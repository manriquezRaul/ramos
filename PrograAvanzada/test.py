w = ('hola', 123, "mundo", 456)
print(w[2])

w = tuple("Hasta la vista".split())
print(w[0:2])

s = ["hola","kilo","frio","mola"]
w = s
s.append("chao")
print(w)

s = ["hola","kilo","frio","mola"]
w = s
s = ["milo", "remo"]
print(w)


class arbolBinario:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

    def __str__(self):
        # Representación en texto para ver la raíz y sus hijos
        return f"arbolBinario({self.valor}, izq={self.izq}, der={self.der})"


def insertaEnArbolBinario(arbol, valor):
    if arbol is None:
        return arbolBinario(valor)

    # Menores a la izquierda
    if valor < arbol.valor:
        if arbol.izq is None:
            arbol.izq = arbolBinario(valor)
        else:
            insertaEnArbolBinario(arbol.izq, valor)
    # Mayores a la derecha
    elif valor > arbol.valor:
        if arbol.der is None:
            arbol.der = arbolBinario(valor)
        else:
            insertaEnArbolBinario(arbol.der, valor)

    return arbol


# --- Tu código ---
w = arbolBinario(50)
insertaEnArbolBinario(w, 22)
insertaEnArbolBinario(w, 33)
print(w)