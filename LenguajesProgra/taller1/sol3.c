#include <stdio.h>
#include <string.h>


int main () {

	int leidos = 0; 
    char concatenacion[500]="";
	char listaStrings[100][20];

	for(int i = 0; i < 100; i++) {
        printf("Ingrese el string %d: ", i + 1);
        scanf("%s", listaStrings[i]);
        if (strcmp(listaStrings[i], "stop") == 0) {break;}
        leidos++;
    }
    
    int largoMin = strlen(listaStrings[0]);
    for (int i = 0; i < leidos; i++) {
        int largoActual = strlen(listaStrings[i]);
        if(largoActual<largoMin){
            largoMin=largoActual;
     }
    }

    for(int i = 0; i<leidos;i++){
        if(strlen(listaStrings[i]) == largoMin){
            strcat(concatenacion,listaStrings[i]);
        }
    }
    
    printf("%s\n",concatenacion);



	return 0 ; 
}