class TreeNode:

  def __init__(self, val):
    self.val = val
    self.children = []

  def add_child(self, child_node):
    self.children.append(child_node)


# =====================================================================
# 1. CONSTRUCTOR: Convierte relaciones fáciles a Matriz y luego a Árbol
# =====================================================================
def construir_arbol_desde_relaciones(relaciones):
  """Recibe una lista de tuplas tipo: [("Padre", "Hijo"), ...]
  Genera la matriz de adyacencia y construye el árbol automáticamente.
  """
  # Obtener todos los nombres únicos preservando orden de aparición
  nodos_set = []
  for padre, hijo in relaciones:
    if padre not in nodos_set:
      nodos_set.append(padre)
    if hijo not in nodos_set:
      nodos_set.append(hijo)

  n = len(nodos_set)
  indices = {nombre: i for i, nombre in enumerate(nodos_set)}

  # Crear la matriz de adyacencia (n x n) con ceros
  matriz = [[0] * n for _ in range(n)]
  in_degree = [0] * n  # Conteo de quién tiene padres

  # Llenar la matriz con las conexiones dadas
  for padre, hijo in relaciones:
    i = indices[padre]
    j = indices[hijo]
    matriz[i][j] = 1
    in_degree[j] += 1

  # Instanciar los objetos TreeNode
  tree_nodes = [TreeNode(nombre) for nombre in nodos_set]

  # Enlazar los hijos usando la matriz creada
  for i in range(n):
    for j in range(n):
      if matriz[i][j] == 1:
        tree_nodes[i].add_child(tree_nodes[j])

  # La raíz es el nodo que nunca aparece como hijo (in_degree == 0)
  raices = [tree_nodes[i] for i in range(n) if in_degree[i] == 0]

  if not raices:
    raise ValueError(
        "Hay un ciclo en las relaciones (no hay una raíz clara)."
    )

  return raices[0], matriz, nodos_set


# =====================================================================
# 2. OBTENER NIVELES (Lista simple fácil de personalizar)
# =====================================================================
def obtener_niveles(raiz):
  """Retorna una lista simple por capas:

  [[Nivel 0], [Nivel 1], [Nivel 2], ...]
  """
  if not raiz:
    return []

  niveles = []
  capa_actual = [raiz]

  while capa_actual:
    valores_de_esta_capa = [nodo.val for nodo in capa_actual]
    niveles.append(valores_de_esta_capa)

    siguiente_capa = []
    for nodo in capa_actual:
      siguiente_capa.extend(nodo.children)
    capa_actual = siguiente_capa

  return niveles


# =====================================================================
# 3. VISTA JERÁRQUICA (Árbol con ramas)
# =====================================================================
def imprimir_jerarquia(nodo, prefijo="", es_ultimo=True):
  conector = "└── " if es_ultimo else "├── "
  print(prefijo + conector + str(nodo.val))

  prefijo += "    " if es_ultimo else "│   "
  total_hijos = len(nodo.children)

  for i, hijo in enumerate(nodo.children):
    imprimir_jerarquia(hijo, prefijo, i == (total_hijos - 1))


# =====================================================================
# EJECUCIÓN Y PRUEBA
# =====================================================================
if __name__ == "__main__":
  # DEFINIR AQUÍ LOS NODOS DE FORMA DIRECTA: (Padre, Hijo)
  conexiones = [
      ("root", "1"),
      ("root", "2"),
      ("1", "3"),
      ("1", "4"),
      ("2", "5"),
      ("2", "6"),
      ("5", "9"),
      ("9", "13"),
      ("13", "14"),
      ("13", "15"),
      ("3", "7"),
      ("3", "8"),
      ("8", "12"),
      ("7", "10"),
      ("7", "11"),
  ]

  # Construcción automática del árbol y la matriz interna
  raiz, matriz, etiquetas = construir_arbol_desde_relaciones(conexiones)

  # -------------------------------------------------------------
  # VISTA 1: POR NIVELES (Modifícalo a tu gusto fácilmente)
  # -------------------------------------------------------------
  print("\n=== VISTA POR NIVELES ===")
  niveles = obtener_niveles(raiz)

  for num_nivel, nodos_en_nivel in enumerate(niveles):
    # Aquí puedes cambiar el texto, separador o diseño que quieras:
    cadena_nodos = " • ".join(nodos_en_nivel)
    print(f"[Nivel {num_nivel}] -> {cadena_nodos}")

  # -------------------------------------------------------------
  # VISTA 2: POR JERARQUÍA
  # -------------------------------------------------------------
  print("\n=== VISTA POR JERARQUÍA ===")
  imprimir_jerarquia(raiz)