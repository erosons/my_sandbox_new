#include <iostream>

using namespace std ;


// Constant are values are not Modifable 
int main(){
    const int Mynum = 5 ;
    Mynum = 10;  //Give an error : assignment of read-only variable MyNum
    cout << Mynum ;
    return 0;
}
