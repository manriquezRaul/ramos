#include <iostream> 
using namespace std ; 

int main() { 
  int edad;
  char nombre[50];
  
  cout << "Ingrese su Nombre: ";
  cin  >> nombre;
  cout << "Ingrese su edad: ";
  cin  >> edad ; 
  
  cout << nombre << " tienes " << edad << " años." << endl;
  
  return 0 ; 
}