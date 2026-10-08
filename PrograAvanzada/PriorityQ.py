import json

class PriorityQueueUnsorted:
    def __init__(self):
        self.lista = []

    def insert(self, element, priority):
        """
        insert(element, priority):
            node.element ← element
            node.priority ← priority
            list.append(node)
        """
        node = {
            "element": element,
            "priority": priority
        }
        self.lista.append(node)

    def extract_max(self):
        """
        extract_max():
            highest ← 0
            foreach node in list:
                if highest.priority < node.priority:
                    highest ← node
            list.remove(highest)
            return highest.element
        """
        if not self.lista:
            return None

        highest = self.lista[0]

        for node in self.lista:
            if node["priority"] > highest["priority"]:
                highest = node

        self.lista.remove(highest)
        return highest["element"]


if __name__ == "__main__":
    with open("pacientes.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
        pacientes = datos["pacientes"]

    k = int(input("Ingrese K (cupos disponibles): "))
    pq = PriorityQueueUnsorted()

    for paciente in pacientes:
        pq.insert(element=paciente, priority=paciente["ivmt"])

    seleccionados = []
    for _ in range(k):
        max_paciente = pq.extract_max()
        if max_paciente is None:
            break
        seleccionados.append(max_paciente)

    print(f"\nTop {k} Pacientes (Unsorted PQ):")
    print(json.dumps(seleccionados, indent=2, ensure_ascii=False))