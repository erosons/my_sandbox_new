#include <iostream>
using namespace std;
#include <cmath>
#include <stdio.h>

void Bubblesort(int[], int);
void printArray(int[], int);

int main() {
  int x[5];
  int SIZE = 5;
  // sizeof(x) / sizeof(int);
  int counter = 0;
  cout << "Please enter your array values in any order" << endl;
  while (counter < SIZE) {
    cin >> x[counter];
    counter++;
  }

  Bubblesort(x, SIZE);
  printf("Sorted array: \n");
  printArray(x, SIZE);

  return 0;
}

// A function to implement bubble sort
void Bubblesort(int x[], int SIZE) {
  int k, i, temp;

for (k = 1; k < SIZE; k++) {
     for (i = 0; i < SIZE-1; i++) {
       if (x[i] > x[i + 1]){
          temp = x[i];
          x[i] = x[i + 1];
          x[i + 1] = temp;
       }
    }
  }
}

// A function to print out the sorted Array
void printArray(int x[], int SIZE) {

  for (int i = 0; i < SIZE; i++) {

    printf(" %d ", x[i]);
    // cout << x[i]<< ',';
  }
}
