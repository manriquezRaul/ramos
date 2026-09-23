import json
from pathlib import Path

class TreeNode:

  def __init__(self, nombre, id=None):
    self.id = id
    self.nombre = nombre
    self.children = []
    self.parents = []

  def add_child(self, child_node):
    if child_node not in self.children:
      self.children.append(child_node) 
    if self not in child_node.parents:
      child_node.parents.append(self)

def construir_arbol_desde_relaciones(relaciones):

  nodos_set = []
  for padre, hijo in relaciones:
    if padre not in nodos_set:
      nodos_set.append(padre)
    if hijo not in nodos_set:
      nodos_set.append(hijo)

  n = len(nodos_set)
  indices = {nombre: i for i, nombre in enumerate(nodos_set)}

  matriz = [[0] * n for _ in range(n)]
  in_degree = [0] * n  

  for padre, hijo in relaciones:
    i = indices[padre]
    j = indices[hijo]
    matriz[i][j] = 1
    in_degree[j] += 1

  tree_nodes = [TreeNode(nombre) for nombre in nodos_set]

  for i in range(n):
    for j in range(n):
      if matriz[i][j] == 1:
        tree_nodes[i].add_child(tree_nodes[j])

  raices = [tree_nodes[i] for i in range(n) if in_degree[i] == 0]

  if not raices:
    raise ValueError("Hay un ciclo en las relaciones (no hay una raíz clara).")
  return raices[0], matriz, nodos_set

def construir_arbol_genealogico(ruta_archivo):
  with open(ruta_archivo, "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

  personas = {}
  for persona in datos["personas"]:
    nodo = TreeNode(persona["nombre"], persona["id"])
    personas[persona["id"]] = nodo

  for relacion in datos["padres"]:
    padre = personas[relacion["padre"]]
    hijo = personas[relacion["hijo"]]
    padre.add_child(hijo)

  raices = []
  for nodo in personas.values():
    if not nodo.parents:
      raices.append(nodo)

  return raices, personas

def buscar_persona(personas, nombre):
  for persona in personas.values():
    if persona.nombre.lower() == nombre.lower():
      return persona
  return None

def obtener_padres_y_hermanos(persona):
  padres = persona.parents
  hermanos = []

  for padre in padres:
    for hijo in padre.children:
      if hijo is not persona and hijo not in hermanos:
        hermanos.append(hijo)

  return padres, hermanos

def obtener_antepasados(persona):
  generaciones = []
  generacion_actual = persona.parents
  visitados = []

  while generacion_actual:
    generacion = []
    for antepasado in generacion_actual:
      if antepasado not in visitados:
        generacion.append(antepasado)
        visitados.append(antepasado)

    if generacion:
      generaciones.append(generacion)

    siguiente_generacion = []
    for antepasado in generacion:
      for padre in antepasado.parents:
        if padre not in siguiente_generacion:
          siguiente_generacion.append(padre)
    generacion_actual = siguiente_generacion

  return generaciones

def obtener_niveles(raiz):
  if not raiz:
    return []

  niveles = []
  capa_actual = [raiz]

  while capa_actual:
    valores_de_esta_capa = [nodo.nombre for nodo in capa_actual]
    niveles.append(valores_de_esta_capa)

    siguiente_capa = []
    for nodo in capa_actual:
      siguiente_capa.extend(nodo.children)
    capa_actual = siguiente_capa

  return niveles

def imprimir_jerarquia(nodo, prefijo="", es_ultimo=True):
  conector = "└── " if es_ultimo else "├── "
  print(prefijo + conector + str(nodo.nombre))

  prefijo += "    " if es_ultimo else "│   "
  total_hijos = len(nodo.children)

  for i, hijo in enumerate(nodo.children):
    imprimir_jerarquia(hijo, prefijo, i == (total_hijos - 1))

# =====================================================================

if __name__ == "__main__":
  ruta_json = Path(__file__).with_name("arbol_genealogico.json")
  raices, personas = construir_arbol_genealogico(ruta_json)

  print("=== ARBOL GENEALOGICO ===")
  for raiz in raices:
    imprimir_jerarquia(raiz)

  nombre_consultado = "Pedro"
  persona = buscar_persona(personas, nombre_consultado)

  if persona is None:
    print(f"No se encontro a {nombre_consultado}.")
  else:
    padres, hermanos = obtener_padres_y_hermanos(persona)
    print(f"\n=== Padres Y Hermanos de {persona.nombre} ===")
    print("Padres:", ", ".join(padre.nombre for padre in padres))
    print("Hermanos:", ", ".join(hermano.nombre for hermano in hermanos))


