#include <iostream>
#include <typeinfo>  // libray to get the data type
using namespace std;
 
int main() {
    float x = 12.5;
    cout << "Type of x : " << typeid(x).name() << endl;
}