#include <stdio.h>

class Complejo {
public:
    double real;
    double imaginario;

    Complejo() {
        real = 0.0;
        imaginario = 0.0;}

    Complejo(double parteR, double parteI) {
        real = parteR;
        imaginario = parteI;}

    void leer() {
        scanf("%lf", &real);
        scanf("%lf", &imaginario);}

    void print() {
        printf("%.2f+%.2fi", real, imaginario); }
};

int main() {
    Complejo c1, c2;
    Complejo *p1 = new Complejo();
    Complejo *p2 = new Complejo();


    c1.leer();
    c2.leer();
    p1->leer();
    p2->leer();

    c1.print();
    printf(" , ");
    c2.print();
    printf(" , ");
    p1->print();
    printf(" , ");
    p2->print();
    printf("\n");

    delete p1;
    delete p2;

    return 0;
}