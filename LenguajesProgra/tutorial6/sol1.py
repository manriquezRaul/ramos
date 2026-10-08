class Celula:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.viva = False

    def esta_viva(self):
        return self.viva

    def esta_muerta(self):
        return not self.viva

    def vive(self):
        self.viva = True

    def muere(self):
        self.viva = False

class Ambiente:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = []
        for i in range(filas):
            linea = []
            for j in range(columnas):
                linea.append(Celula(i, j))
            self.matriz.append(linea)

    def vive(self, x, y):
        if 0 <= x < self.filas and 0 <= y < self.columnas:
            self.matriz[x][y].vive()

    def muere(self, x, y):
        if 0 <= x < self.filas and 0 <= y < self.columnas:
            self.matriz[x][y].muere()

    def muestraTxt(self):
        for fila in self.matriz:
            fila_str = "".join(["*" if cel.esta_viva() else " " for cel in fila])
            print(fila_str)


if __name__ == "__main__":
    amb = Ambiente(15, 15)

    centro_fila = amb.filas // 2
    centro_col = amb.columnas // 2

    for i in range(amb.filas):
        for j in range(amb.columnas):
            if i == j:  
                if not (i == centro_fila and j == centro_col):
                    amb.vive(i, j)

    amb.muestraTxt()