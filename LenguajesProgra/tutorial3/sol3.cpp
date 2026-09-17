#include <stdio.h>

class Complejo {
public:
    double real;
    double imaginario;

    // Constructores
    Complejo() {
        real = 0.0;
        imaginario = 0.0;
    }
    Complejo(double parteR, double parteI) {
        real = parteR;
        imaginario = parteI;
    }
    void leer() {
        scanf("%lf %lf", &real, &imaginario);
    }

    Complejo suma(Complejo c) {
        Complejo resultado;
        resultado.real = real + c.real;
        resultado.imaginario = imaginario + c.imaginario;
        return resultado;
    }

    void print() {
        printf("%.2f+%.2fi", real, imaginario);
    }
};

int main() {
    Complejo c1, c2, c3;

    c1.leer();
    c2.leer();
    c3.leer();

    Complejo total = c1.suma(c2).suma(c3);

    total.print();
    printf("\n");

    return 0;
}