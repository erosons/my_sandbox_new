#include <iostream>
using namespace std;
#include <iostream>


int main() {

    int a =1;
    int* p1 =&a;
    int b =2;
    int* p2 =&b;
    int c =3;
    int* p3= &c;


    cout << *p1 + *p2 + *p3<< endl;
    return 0;
}