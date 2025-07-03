#include <iostream>
using namespace std;
 


int main() {

int id;
const int  SIZE=6;
int sales_id[SIZE] = {1,2,3,4,5,6} ;
float salesAmount[SIZE]={12.6,100.5,56.7,56.9,40.0,56.4};

for(int i=0;i<SIZE;i++){

  cout <<  "Enter a Value";
  cin >> id;
  if (sales_id[i]==id)
   cout << salesAmount[id] << "\n";
        
}

return 0;
}