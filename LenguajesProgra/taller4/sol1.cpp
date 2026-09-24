#include <iostream>
#include <list>
#include <utility> 
using namespace std;

int main(){
    list<pair<double, double>> lista;
    double c1, c2;
    bool continuar = true;

    while(continuar){
        cin >> c1 >> c2;
        if(c1 == -1 && c2 == -1){  break;}
        lista.push_back(make_pair(c1, c2));  
    }
    

    if (!lista.empty()) {
        list<pair<double, double>>::iterator it_init = lista.begin();
        double mayor1 = it_init->first;
        double mayor2 = it_init->second;
        
        if (mayor2 > mayor1) {
            double aux = mayor1;
            mayor1 = mayor2;
            mayor2 = aux; }

        for (list<pair<double,double>>::iterator it = lista.begin();it !=lista.end();++it) {
            cout << "[" << it->first << "," << it->second << "]" << endl;

            double nums[2] = {it->first, it->second};
            for (int i = 0; i < 2; ++i) {
                double actual = nums[i];
                if (actual > mayor1) {
                    mayor2 = mayor1;
                    mayor1 = actual;  } 
                else if (actual > mayor2 && actual != mayor1) {
                    mayor2 = actual;}
            }
        }
        pair<double, double> parMayor(mayor2, mayor1);
        cout << "max [" << parMayor.first << "," << parMayor.second << "]" << endl;
        
    } 

    return 0;
}