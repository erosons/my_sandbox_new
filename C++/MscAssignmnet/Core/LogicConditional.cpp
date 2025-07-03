#include <iostream>

using namespace std ;

int main(){
    cout << "Please enter the number of hours worked for the week :";
    float overtimerate;
    float hourlyRate =18.25;
    float totalhour;
    cin >> totalhour;
    if(totalhour<=40){
        cout << "$" << totalhour * hourlyRate ;
    }
   else
      overtimerate = hourlyRate * 1.5;
      float overtimeAmount = (totalhour-40)* overtimerate;
       
      cout << "$" << (totalhour * hourlyRate) + overtimeAmount;
      return 0;
}


// Scenario Two

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
    return 0;
   }
    else if(temperature<=80 && temperature>70){
        cout << "Do nothing.";
    return 0;
   }
    else if(temperature<=90 && temperature>80){
        cout << "Turn on air conditioning.";
    return 0;
   }
   else
     cout << "Visit a neighbor";

     return 0;
}
