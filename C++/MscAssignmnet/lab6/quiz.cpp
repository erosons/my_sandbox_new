#include <iostream>
using namespace std;


int main() {
  int x[10];
  int ArrayLength = sizeof(x) / sizeof(int);
  int count=0;
  int userinput;
  int userSearch;
  while (count<ArrayLength){
    cout << "Please enter an interger Value:"<< endl;
    cin >> userinput;
    x[count]=userinput;
    count++;
     if (count==10)
        break; 
      else
        continue;
    }
  cout << "You have randomly entered 10 interger Values"<< endl;
  cout << "What Value will you like to search for"<< endl;
  cin >> userSearch;
  int counter=0;
  for (int i=0;i<= ArrayLength; i++){

    if (userSearch==x[i]){
       counter++;
    }
  }
  cout << "Total Number of occurrence of your search is :" << counter <<endl; 
  return 0;
  }