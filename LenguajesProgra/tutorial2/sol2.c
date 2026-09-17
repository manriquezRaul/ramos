#include  <stdio.h>

int main() {
   int a=4;
   float b=3.15;
   char t[20]="Hola a todos ";
   double x=3.4;
   char r[25]="La risa abunda en todo";
   double *ptr, *qtr;
   ptr=(double *)r;
   qtr=(double *)t;
   printf("t en %p, x en %p, r en %p, ptr en %p, qtr en %p,a en %p ,b en %p\n", t, &x, r, ptr, qtr,&a,&b);

   //se muestran los espacios de memoria ocupados por las variables no se puede acceder a los valores de las
   //variables a través de ptr y qtr
    printf("se muestran los espacios de memoria ocupados por las variables no se puede acceder a los valores de las variables a través de ptr y qtr");
}