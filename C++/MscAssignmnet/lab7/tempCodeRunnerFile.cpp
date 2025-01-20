#include <iostream>
using namespace std;


const int SIZE=5; 
int x[SIZE];

 //For the Array
void Bubblesort(int [],int );


int main(){

int counter =0;
while (counter < SIZE){

     cin >> x[counter];
     counter++;
}

Bubblesort(x,SIZE);


}



void Bubblesort(int x[],int SIZE){

int sortedArray[SIZE];
int k,i,temp,flag;

for (k =1 ; k<SIZE ;k++){
   flag=0;
   for(i=0;i< SIZE-k; i++){
       if(x[i] > x[i+1])
               temp=x[i];
                 x[i]=x[i+1];
                  x[i+1] = temp;
     if (x[i] > x[i+1]&& x[i+1]>x[i+2] && x[i+2]>x[i+3] &&x[i+3]>x[i+4])
          flag=1;
     
   }
sortedArray[i]=x[i];
cout << sortedArray << endl ;
if(flag !=0)
   break;
 }
}