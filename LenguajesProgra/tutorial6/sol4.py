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
    
        self.botones = [[None for _ in range(columnas)] for _ in range(filas)]

    def vive(self, x, y):
        if 0 <= x < self.filas and 0 <= y < self.columnas:
            self.matriz[x][y].vive()

    def muere(self, x, y):
        if 0 <= x < self.filas and 0 <= y < self.columnas:
            self.matriz[x][y].muere()

    def total_vivas(self):
        contador = 0
        for fila in self.matriz:
            for cel in fila:
                if cel.esta_viva():
                    contador += 1
        return contador

    def limpiar_ambiente(self):

        for fila in range(self.filas):
            for columna in range(self.columnas):
                self.matriz[fila][columna].muere()
            
                if self.botones[fila][columna] is not None:
                    self.botones[fila][columna].config(bg="grey")
        print("Ambiente limpiado: todas las células están muertas.")

    def muestraTxt(self):
        for fila in self.matriz:
            fila_str = "".join(["*" if cel.esta_viva() else " " for cel in fila])
            print(fila_str)

    def muestraTk(self):
        ventana = tk.Tk()
        ventana.title("Ambiente Conway")
        
        for fila in range(self.filas):
            for columna in range(self.columnas):
                valor = self.matriz[fila][columna].esta_viva()
                color = "green" if valor else "grey"
                
                boton = tk.Button(
                    ventana,
                    text="",
                    bg=color,
                    width=2,
                    height=1,
                    command=lambda f=fila, c=columna: self.cambiar_valor(f, c)
                )
                boton.grid(row=fila, column=columna)
                self.botones[fila][columna] = boton

        clear = tk.Button(ventana, text="Limpia", command=self.limpiar_ambiente)
        clear.grid(row=self.filas, column=0, columnspan=self.columnas, sticky="we")
        
        ventana.mainloop()

    def cambiar_valor(self, fila, columna):
        celula = self.matriz[fila][columna]
        
        if celula.esta_viva():
            celula.muere()
            nuevo_color = "grey"
        else:
            celula.vive()
            nuevo_color = "green"
            
        if self.botones[fila][columna] is not None:
            self.botones[fila][columna].config(bg=nuevo_color)
            
        print(f"Llega a fila: {fila}, columna: {columna}")
        print(f"Total de células vivas: {self.total_vivas()}")


if __name__ == "__main__":
    amb = Ambiente(15, 15)
    amb.vive(2, 2)
    amb.vive(3, 3)
    amb.vive(4, 4)
    amb.vive(5, 5)
    amb.muere(3, 3)
    amb.muere(3, 4)
    
    amb.muestraTxt()
    amb.muestraTk()