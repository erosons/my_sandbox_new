#include <iostream>
using namespace std ;

int main() {

   char greet[] = "Yellow";
   char* ptr ;
   ptr=greet;
   for(int i=0; i<6;i++){
     cout << ptr[i]<<"\n";
   }
    
    return 0;
}