
#include <iostream>
#include <cmath>
using namespace std ;

void countUpper(string &x);
// The function counts the number sting in a statement


int main(){

string UpCount;
countUpper(UpCount);
 
return 0;
}



void countUpper(string &x){
   cout << "My new Name is Now : ";
   getline(cin, x);
    // Traversing over a string
    int counter=0;
    for(int i=0; i<x.length();i++){
        // checking for upper case statement
    if(isupper(x[i])){
             counter++;
        }
    }
    cout << counter;
}
