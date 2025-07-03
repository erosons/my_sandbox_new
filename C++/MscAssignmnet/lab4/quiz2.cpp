#include <iostream>
using namespace std;

void calculator(int , int ,int , double );



int main() {
  int Opsvalue;
  do {
    cout << "Please select one of the Math operation below you would like to "
            "perform today"
         << endl;
    cout << "1. Addition Operations" << endl;
    cout << "2. Substraction Operations" << endl;
    cout << "3. Divison Operations" << endl;
    cout << "4. Divison Operations" << endl;

    int Opsvalue;
    cin >> Opsvalue;
    double Value1;
    double Value2;
    double sumOps;
    cout << "Enter your First Number" << endl;
    cin >> Value1;
    cout << "Enter your Second Number" << endl;
    cin >> Value2;

    if (Opsvalue == 1) {

      sumOps = Value1 + Value2;
      cout << sumOps;
    }

    else if (Opsvalue == 2) {
      sumOps = Value1 * Value2;
      cout << sumOps;
    } 
    else if (Opsvalue == 3) {
      sumOps = Value1 - Value2;
      // cout << sumOps;
    } 
    else if (Opsvalue == 4) {
      sumOps = Value1 / Value2;
      cout << sumOps;
    }
  
  } while (Opsvalue != 5);
  return 0;
}
