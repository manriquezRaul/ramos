import json
import random

def crear_sensores(cantidad=2000):
    return [
        {
            "id": sensor_id,
            "hora": random.randint(1, 23),
            "minuto": random.randint(1, 59),
        }
        for sensor_id in range(1, cantidad + 1)
    ]


def generar_json(sensor, archivo="event.json"):
    """Guarda el evento seleccionado para que otro programa lo lea."""
    with open(archivo, "w", encoding="utf-8") as file:
        json.dump(sensor, file, indent=4, ensure_ascii=False)


def simulacion():
    sensores = crear_sensores()
    contador=0;

    while True:
        evento = random.randint(0, len(sensores))
        contador+=1
        if evento == 0:
            break

        sensor = sensores[evento - 1]
        generar_json(sensor)
        print(f"Evento generado: sensor {sensor['id']} -> evento.{contador}.json")

        respuesta = input("¿Desea generar otro evento? (1=si, 0=no): ").strip()
        if respuesta == "0":
            break

    print("Simulacion terminada")


if __name__ == "__main__":
    simulacion()
