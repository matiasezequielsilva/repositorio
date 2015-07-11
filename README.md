# repositorio
Ejemplo C++
#include <cstdlib>
#include <iostream>

using namespace std;
struct cliente{
       int socio;
       float dinero;
       }pepe , mario , a;

void asignar(int s, float d, struct cliente)
{
     a.socio=s;
     a.dinero=d;
     };
int main(int argc, char *argv[])
{
    int s;
    float d;
    cout << "ingrese numero de socio y dinero de pepe" << endl;
    cin >> s >> d;
    asignar(s,d,a);
    pepe=a;
    cout << "ingrese numero de socio y dinero de mario" << endl;
    cin >> s >> d;
    asignar (s,d,a);
    mario=a;
    cout << pepe.socio << endl;
    cout << pepe.dinero << endl;
    cout << mario.socio << endl;
    cout << mario.dinero << endl;
    system("PAUSE");
    return EXIT_SUCCESS;
}
