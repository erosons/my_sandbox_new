#include <iostream>

using namespace std ;

int main(){
    cout << "Please enter the Temperature :";
    float temperature ;
    cin >> temperature ;
    if(temperature<=55){
        cout << "Visit a neighbor.";
    }
    else if(temperature<=70 && temperature>55){
        cout << "Turn on heat.";
  
   }
    else if(temperature<=80 && temperature>70){
        cout << "Do nothing.";
  
   }
    else if(temperature<=90 && temperature>80){
        cout << "Turn on air conditioning.";
  
   }
   else
     cout << "Visit a neighbor";

     return 0 ;
}
