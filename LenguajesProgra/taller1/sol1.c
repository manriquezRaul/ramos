#include <stdio.h>
#include <string.h>

int main () {
     
     float numero1, numero2 , numero3 , promedio , mayor , menor;  
     scanf("%f",&numero1);
     scanf("%f",&numero2);
     scanf("%f",&numero3);

    mayor = numero1 ; 
    if (numero2>mayor){mayor=numero2;}
    if (numero3>mayor){mayor=numero3;}
    menor = numero1 ; 
    if (numero2<menor){menor=numero2;}
    if (numero3<menor){menor=numero3;}

      
      promedio = (mayor+menor) / 2.0; 

      printf("%.3f\n",promedio);

    return 0;
}