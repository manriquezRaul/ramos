// solucion2.cpp
#include <cstdio>
#include <cstring>

class SopaLetras {
private:
    static const int N = 12;
    char sopa[N][N];

public:
    SopaLetras() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                sopa[i][j] = '+';
            }
        }
    }

    int ubica_horizontal(const char *palabra, int fila, int columna) {
        int largo = strlen(palabra);
        int f = fila - 1;
        int c = columna - 1;

        if (f < 0 || f >= N) return 0;
        if (c < 0 || c + largo > N) return 0;

        for (int i = 0; i < largo; i++) {
            sopa[f][c + i] = palabra[i];
        }
        return 1;
    }

    void muestra() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                printf("%c", sopa[i][j]);
            }
            printf("\n");
        }
    }
};

int main() {
    SopaLetras juego;
    char palabra[50];
    int fila, columna;
    char palabras_ingresadas[100][50];
    int resultados[100];
    int total = 0;

    while (scanf("%s", palabra) == 1) {
        if (strcmp(palabra, "stop") == 0) {
            break;
        }
        scanf("%d %d", &fila, &columna);

        int resultado = juego.ubica_horizontal(palabra, fila, columna);

        strcpy(palabras_ingresadas[total], palabra);
        resultados[total] = resultado;
        total++;
    }

    for (int i = 0; i < total; i++) {
        printf("%s %d\n", palabras_ingresadas[i], resultados[i]);
    }
    juego.muestra();

    return 0;
}