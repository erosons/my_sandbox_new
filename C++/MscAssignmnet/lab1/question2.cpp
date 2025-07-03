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
