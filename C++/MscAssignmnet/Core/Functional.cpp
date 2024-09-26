#include <iostream>
#include <cmath>
using namespace std ;

// Writing functional programm
float powerFunc(double x , int y){

    int loop =1;
    for(int i=0;i<abs(y);i++){
        loop *=x;
    }
    if(y>0){

    return loop;
    }
    else{
        return 1/loop;
    }
}


int main(){ 
   float powerCalc=powerFunc(2,-3);
   cout <<powerCalc;
}
