#include <stdio.h>

class Complejo {
public:
    double real;
    double imaginario;

    Complejo(){
         real=0.0;
         imaginario=0.0;
  }
  void leer(){
    scanf("%lf", &real);
    scanf("%lf", &imaginario);
  }

  void print(){
    printf(" %.3lf+%.3lfi \n", real, imaginario);
  }
};

int main(){
  Complejo c;
  c.leer();
  c.print();
  return 0 ;
}