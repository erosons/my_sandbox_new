#include <iostream>
using namespace std;

void Reverse(string []);

int main() {
  string x[10];
  Reverse(x);
  return 0;
  }

void Reverse(string x[]){
  int m;
  int n;
<<<<<<< HEAD
<<<<<<< HEAD
  //int ArrayLength = sizeof(x) / sizeof(int);
  for (int i=0;i<10;i++){
=======
  //int ArrayLength = sizeof(x) / sizeof(string);
  for (m=0;m<10;m++){
>>>>>>> 33068ac372624781f20774414a2f3c19a28af9ac
=======
  //int ArrayLength = sizeof(x) / sizeof(string);
  for (m=0;m<10;m++){
>>>>>>> 15a1bf99f7fa80c709eeae69413af949ee28558c
    cout << "Please enter an string:"<< endl;
    cin >> x[m];
    m++;
    }

  while (m <1){
    cout << x[m]<<endl;
    m--;
      }
    }
