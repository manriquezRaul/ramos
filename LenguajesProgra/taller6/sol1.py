import tkinter as tk

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

    def vecinasVivas(self, matriz, filas, columnas):
        contador = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                nx, ny = self.x + i, self.y + j
                if 0 <= nx < filas and 0 <= ny < columnas:
                    if matriz[nx][ny].esta_viva():
                        contador += 1
        return contador

class Ambiente:
    def __init__(self, master, filas=25, columnas=25):
        self.master = master
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[Celula(i, j) for j in range(columnas)] for i in range(filas)]
        
        self.botones = [[None for _ in range(columnas)] for _ in range(filas)]
        self.crear_interfaz()

    def crear_interfaz(self):
        frame_matriz = tk.Frame(self.master)
        frame_matriz.pack(pady=10)

        for i in range(self.filas):
            for j in range(self.columnas):
                btn = tk.Button(frame_matriz, width=2, height=1, bg="lightgray",
                                command=lambda r=i, c=j: self.clic_celula(r, c))
                btn.grid(row=i, column=j)
                self.botones[i][j] = btn

        btn_limpiar = tk.Button(self.master, text="Limpiar Ambiente", command=self.limpiaAmbiente)
        btn_limpiar.pack(pady=10)

    def vive(self, x, y):
        self.matriz[x][y].vive()
        self.botones[x][y].config(bg="green")

    def muere(self, x, y):
        self.matriz[x][y].muere()
        self.botones[x][y].config(bg="lightgray")

    def clic_celula(self, x, y):
        celula = self.matriz[x][y]
        if celula.esta_viva():
            self.muere(x, y)
        else:
            self.vive(x, y)
        
        vecinas = celula.vecinasVivas(self.matriz, self.filas, self.columnas)
        print(f"Célula ({x}, {y}) - Vecinas vivas: {vecinas}")

    def limpiaAmbiente(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                self.muere(i, j)
        print("Ambiente limpiado.")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Ambiente(ventana, filas=25, columnas=25)
    ventana.mainloop()