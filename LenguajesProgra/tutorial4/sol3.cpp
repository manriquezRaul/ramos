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

    void mostrar() const {
        cout << "(" << real << ", " << imag << ")" << endl;
    }

    bool operator==(const Complejo& otro) const {
        return real == otro.real && imag == otro.imag;
    }
};

int main() {
    list<Complejo> lista;
    lista.push_back(Complejo(1.0, 2.0));
    lista.push_back(Complejo(3.0, 4.0)); 
    lista.push_back(Complejo(5.0, 6.0));
    lista.push_front(Complejo(7.0, 8.0));
    lista.push_front(Complejo(9.0, 10.0));
    lista.push_back(Complejo(2.0, 5.0)); 
    lista.push_back(Complejo(0.0, 1.0));



    cout << "\nLista con todos los elementos " << endl;
    for (list<Complejo>::iterator it = lista.begin(); it != lista.end(); ++it) {
        it->mostrar();
    }

    if (!lista.empty()) {
        lista.front().mostrar();
        lista.pop_front();
    }

    list<Complejo> elementosAEliminar;
    for (list<Complejo>::iterator it = lista.begin(); it != lista.end(); ++it) {
        if (it->real + it->imag == 7.0) {
            elementosAEliminar.push_back(*it);
        }
    }

    for (list<Complejo>::iterator it = elementosAEliminar.begin(); it != elementosAEliminar.end(); ++it) {
        lista.remove(*it);
    }

    cout << "lista resultado " << endl;
    for (list<Complejo>::iterator it = lista.begin(); it != lista.end(); ++it) {
        it->mostrar();
    }

    return 0;
}