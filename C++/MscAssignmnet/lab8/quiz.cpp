#include <iostream>
using namespace std;
#include <stdio.h>

void numberSearch(int[], int);

const int SIZE = 10;
int x[SIZE];
int odd[SIZE];
int even[SIZE];
int evencounter, oddcounter = 0;
int arraylength = sizeof(x) / sizeof(int);



int main()
{

    numberSearch(x, SIZE);
    return 0;
}



void numberSearch(int x[], int arraylength)
{
    int userinputCounter = 0;
    cout << "Total Array length :" << arraylength << endl;
    while (userinputCounter < arraylength)
    {
        cin >> x[userinputCounter];
        userinputCounter++;
    }
    for (int i = 0; i < arraylength; i++)
    {
        if (x[i] % 2 == 0)
        {
            even[evencounter] = x[i];
            evencounter++;
        }
        else if (x[i] % 2 == 1)
        {
            odd[oddcounter] = x[i];
            oddcounter++;
        }
    }
    for (int i = 0; i < evencounter; i++)
    {
        cout << "Even inputs :" << even[i] << endl;
        // printf(" %d ", even[i]);
    }
    for (int i = 0; i < oddcounter; i++)
    {
        cout << "Odd inputs :" << odd[i] << endl;
        // printf(" %d ", odd[i]);
    }
}
