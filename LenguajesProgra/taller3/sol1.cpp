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

        if (fila < 0 || fila >= N) return 0;
        if (columna < 0 || columna + largo > N) return 0;

        for (int i = 0; i < largo; i++) {
            sopa[fila][columna + i] = palabra[i];
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

    if (scanf("%s", palabra) == 1) {
        juego.ubica_horizontal(palabra, 2, 1);
    }

    juego.muestra();
    return 0;
}