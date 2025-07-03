#include <iostream>
using namespace std;


int x[6]={2,49,55,3,9,2};

int arraylength=sizeof(x)/sizeof(int);

int smallest ,largest =x[0];


int main(){

for(int i=1;i<arraylength;i++){

    if(smallest<x[i]){
         smallest=x[i];

    }


    if(largest>x[i]){
         largest=x[i];
    }

}

cout << smallest << "\n" << largest ;

}