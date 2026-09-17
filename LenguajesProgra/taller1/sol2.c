#include <stdio.h>
#include <string.h>


int main () {

	int cantidad ;
	int leidos = 0; 
	printf(" Ingrese cuantas palabras ingresara : ");
	scanf("%d",&cantidad);
	char listaStrings[cantidad][20];

	for(int i = 0; i < cantidad; i++) {
        printf("Ingrese el string %d: ", i + 1);
        scanf("%s", listaStrings[i]);
        if (strcmp(listaStrings[i], "stop") == 0) {break;}
        leidos++;
    }

    int minConsonantes = -1;
    int posicionMinima = -1;

    for (int i = 0; i < leidos; i++) {
        int largo = strlen(listaStrings[i]);
        int vocales = 0;

        for (int j = 0; j < largo; j++) {
            char c = listaStrings[i][j];
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
                c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                vocales++;
            }
        }

        int consonantes = largo - vocales;
        if (i == 0 || consonantes <= minConsonantes) {
            minConsonantes = consonantes;
            posicionMinima = i + 1;
        }
    }
    

    if (posicionMinima != -1) {
        printf("\nEl string con menos consonantes es: %s\n", listaStrings[posicionMinima]);
    }

	return 0 ; 
}