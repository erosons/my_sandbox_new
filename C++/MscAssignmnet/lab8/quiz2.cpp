#include <iostream>
using namespace std;
#include <stdio.h>

void Rotate(int[]);
void printArray(int [],int);

const int SIZE = 5;
int x[SIZE];
int rotated[SIZE];
int arrayLength = sizeof(x) / sizeof(int);



int main()
{
    
  Rotate(x);
  printf("Rotated array: \n");
  printArray(rotated,SIZE);
  return 0;
}




void Rotate(int x[])
{
    int temp;
    int userinputCounter = 0;
    cout << "Total Array length :" << arrayLength << endl;
    while (userinputCounter < arrayLength)
    {
        cin >> x[userinputCounter];
        userinputCounter++;
    }
    
    temp =x[arrayLength-1];
    
    for (int i = 0; i < arrayLength; i++)
    {
        if(i<4){
            rotated[i+1]=x[i];
        }

        else{
          rotated[0]=temp;
          break;
    
    }

 }
}

void printArray(int rotated[], int SIZE) {
    for(int i=0; i< arrayLength; i++){
         
         printf(" %d ", rotated[i]);

    }
}