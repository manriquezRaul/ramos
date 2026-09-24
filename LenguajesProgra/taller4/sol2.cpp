#include <iostream>
#include <list>
#include <utility>
using namespace std;

class ListaDeCoordenadas {
private:
    std::list<std::pair<double, double>> elementos;
    int cantidad_interna;

public:
    ListaDeCoordenadas() {
        cantidad_interna = 0;}

    int cantidad() {return cantidad_interna; }

    bool inserta_ordenado(std::pair<double, double> p) {
      std::list<std::pair<double, double>>::iterator it = elementos.begin();
        while (it != elementos.end()) {
            if (it->first > p.first) {
                elementos.insert(it, p);
                cantidad_interna++;
                return true; }
            ++it; }
      
        elementos.push_back(p);
        cantidad_interna++;
        return true;}

    void muestra_enum() {
        int idx = 1;
        for (auto it = elementos.begin(); it != elementos.end(); ++it) {
            cout << idx << ": [" << it->first << "," << it->second << "]" << endl;
            idx++; }  }

    std::pair<double, double> obtenerMaximos() {

     std::list<std::pair<double, double>>::iterator it = elementos.begin();
        double max1 = it->first;
        double max2 = it->second;

        for (; it != elementos.end(); ++it) {
            if (it->first > max1) max1 = it->first;
            if (it->second > max2) max2 = it->second; }

        return {max1, max2}; }
};

int main() {
    ListaDeCoordenadas lista;
    double c1, c2;

    while (true) {
        cin >> c1 >> c2;
        if (c1 == -1 && c2 == -1) { break;  }
        lista.inserta_ordenado(make_pair(c1, c2));
    }
    lista.muestra_enum();
    if (lista.cantidad() > 0) {
        pair<double, double> maximos = lista.obtenerMaximos();
        cout << "max [" << maximos.first << "," << maximos.second << "]" << endl;  }

    return 0;
}