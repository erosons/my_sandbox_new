#include <iostream>
using namespace std;
#include <string>


void draw_a_rectangle();

int main(){
  draw_a_rectangle();
  return 0;
}


void draw_a_rectangle(){
  int length ;
  int breadth ;
  cout << "What is your length :";
  cin >> length ;
  cout << "What is your breadth :";
  cin >> breadth ;

  for(int i=0; i<breadth;i++){

    if(i != breadth && i%2==0){
      cout << string(length, '&') << endl;
      }
    else if(i != breadth && i%2 !=0){
      cout << string(length, ' ') << endl;
      }
    else {
    
     cout << string(length, '&') << endl;

    }
}
  }