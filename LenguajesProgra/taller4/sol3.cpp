#include <iostream>
#include <list>
#include <utility>
using namespace std;

class ListaDeCoordenadas {
private:
    list<pair<double, double>> elementos;
    int cantidad_interna;

public:
    ListaDeCoordenadas() {
        cantidad_interna = 0; }

    int cantidad() { return cantidad_interna; }

    bool inserta_ordenado(pair<double, double> p) {
        list<pair<double, double>>::iterator it = elementos.begin();
        while (it != elementos.end()) {
            if (it->first > p.first) {
                elementos.insert(it, p);
                cantidad_interna++;
                return true; }
            ++it; }

        elementos.push_back(p);
        cantidad_interna++;
        return true; }

    void muestra_enum() {
        int id= 1;
        for (list<pair<double, double>>::iterator it = elementos.begin(); it != elementos.end(); ++it) {
            cout << id << ": [" << it->first << "," << it->second << "]" << endl;
            id++; } }

    bool operator<=(ListaDeCoordenadas otra) {
        double suma1 = 0;
        for (list<pair<double, double>>::iterator it = elementos.begin(); it != elementos.end(); ++it) {
            suma1 = suma1 + (it->first * it->second);}

        double suma2 = 0;
        for (list<pair<double, double>>::iterator it = otra.elementos.begin(); it != otra.elementos.end(); ++it) {
            suma2 = suma2 + (it->first * it->second); }
        if (suma1 <= suma2) { return true;} 
        else { return false;}  }
};

int main() {
    ListaDeCoordenadas lista1, lista2;
    double c1, c2;

    while (true) {cin >> c1 >> c2;
        if (c1 == -1 && c2 == -1) {break; }
        lista1.inserta_ordenado(make_pair(c1, c2));
    }

    while (true) {
        cin >> c1 >> c2;
        if (c1 == -1 && c2 == -1) { break;}
        lista2.inserta_ordenado(make_pair(c1, c2));
    }
    if (lista2 <= lista1) {
        cout << "TRUE" << endl;} 
        else {cout << "FALSE" << endl;}

    return 0;
}