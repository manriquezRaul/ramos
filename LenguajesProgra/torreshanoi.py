import math
import time

def resolver_hanoi_generalizado(n_discos, torres):
    """
    Resuelve el problema de las Torres de Hanói para N discos y K torres.

    :param n_discos: Número total de discos.
    :param torres: Lista de nombres/identificadores de las torres (mínimo 3).
    """
    num_torres = len(torres)
    if num_torres < 3:
        raise ValueError("Se requieren al menos 3 torres para resolver el problema.")

    movimientos = []

    def frame_stewart(n, origen, destino, auxiliares):
        if n == 0:
            return

        if n == 1:
            movimientos.append((origen, destino, 1))
            return

        if len(auxiliares) == 1:
            aux = auxiliares[0]
            frame_stewart(n - 1, origen, aux, [destino])
            movimientos.append((origen, destino, n))
            frame_stewart(n - 1, aux, destino, [origen])
            return

        # División óptima de Frame-Stewart
        k = n - round(math.sqrt(2 * n))
        if k <= 0:
            k = n - 1

        # 1. Mover k discos a una torre auxiliar
        aux_target = auxiliares[0]
        otras_aux = auxiliares[1:] + [destino]
        frame_stewart(k, origen, aux_target, otras_aux)

        # 2. Mover n-k discos a la torre destino
        frame_stewart(n - k, origen, destino, auxiliares[1:])

        # 3. Mover k discos al destino final
        otras_aux_3 = auxiliares[1:] + [origen]
        frame_stewart(k, aux_target, destino, otras_aux_3)

    origen = torres[0]
    destino = torres[-1]
    auxiliares = torres[1:-1]

    # Medición del tiempo de ejecución
    inicio_tiempo = time.perf_counter()
    frame_stewart(n_discos, origen, destino, auxiliares)
    fin_tiempo = time.perf_counter()

    tiempo_total = fin_tiempo - inicio_tiempo

    return movimientos, tiempo_total


# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Configuración configurable de Discos y Torres
    N_DISCOS = 15
    TORRES = ["Torre A", "Torre B", "Torre C", "Torre D", "Torre E"]

    pasos, tiempo_ejecucion = resolver_hanoi_generalizado(N_DISCOS, TORRES)

    print(f"--- Solución para {N_DISCOS} discos y {len(TORRES)} torres ---")
    print(f"Total de movimientos calculados: {len(pasos)}")
    print(f"Tiempo de ejecución del algoritmo: {tiempo_ejecucion:.6f} segundos\n")

    # Muestra los primeros 5 pasos como vista previa
    print("Muestra de los primeros pasos:")
    for i, (origen, destino, disco) in enumerate(pasos[:5], 1):
        print(f"Paso {i:2d}: Mover Disco {disco} desde '{origen}' hasta '{destino}'")