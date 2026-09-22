#include <iostream>
#include <list>
using namespace std;

class Complejo {
public:
    double real;
    double imag;

    Complejo(double r, double i) {
        real = r;
        imag = i;
    }

    void mostrar() {
        cout << "(" << real << ", " << imag << ")" << endl;
    }
};

int main() {
    list<Complejo> lista;
    lista.push_back(Complejo(1.0, 2.0));
    lista.push_back(Complejo(3.0, 4.0));
    lista.push_back(Complejo(5.0, 6.0));

     cout << "Contenido de la pila :" << endl;
    for (list<Complejo>::iterator it = lista.begin(); it != lista.end(); ++it) {
        it->mostrar();
    }
    
    lista.push_front(Complejo(7.0, 8.0));
    lista.push_front(Complejo(9.0, 10.0));
    cout << "\nElementos agregados a la pila : (7,8) y (9,10)" ;

     cout << "\n" << endl;
    for (list<Complejo>::iterator it = lista.begin(); it != lista.end(); ++it) {
        it->mostrar();
    }

    if (!lista.empty()) {
        cout << "\nElemento removido de la pila: ";
        lista.front().mostrar();
        lista.pop_front();
    }

    cout << "\nEstado final de la pila:" << endl;
    for (list<Complejo>::iterator it = lista.begin(); it != lista.end(); ++it) {
        it->mostrar();
    }

    return 0;
}