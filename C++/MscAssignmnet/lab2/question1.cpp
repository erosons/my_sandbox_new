#include <iostream>
#include <cmath>
using namespace std ;

float  powerFunc(int,int);

int main(){ 
   float powerCalc = powerFunc(2,-3);
   cout << powerCalc;
}

float powerFunc(int x , int y){

    float loop =1.0;
    for(int i=0;i<abs(y);i++){

   if(y>0){ 
        loop *=x;
   }

    else
      
        loop = 1/(loop *=x);
    
}
return loop
}