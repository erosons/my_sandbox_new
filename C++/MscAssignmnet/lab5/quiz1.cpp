#include <iostream>
using namespace std;


int main() {
  const int SIZE = 25;
  int x[SIZE];
  int ArrayLength = sizeof(x) / sizeof(int);
  int n=1;
  cout << "Print the first 25 old numbers :"<< endl;
  for(int i=1; n<=ArrayLength; i+=2 ){
    if (i % 2 != 0) {
      //cout << n;
      x[n-1] =i* 0.5 ;
      cout << x[n-1] << endl;
      }
     n+=1;
     }
    return 0;
    } 