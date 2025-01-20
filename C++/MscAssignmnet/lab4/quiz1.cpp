#include <iostream>
using namespace std;

void factorial(int &x);

int main() {
  int N;
  cout << "What is your factorial Number" << endl;
  cin >> N;
  factorial(N);

  return 0;
}

void factorial(int &x) {
  int factorialresult = 1;
  for (int i = 1; i < x+1; i++) {

    factorialresult *= i;
  }
  cout << factorialresult;
}