#include <iostream>
using namespace std;
#include <cmath>
#include <fstream>

void read();


int main(){

read();

  }


void read(){

ifstream read_file;
read_file.open("name.txt");
if (read_file){
  string line;
  while (getline(read_file, line))
    cout << line <<'\n';
read_file.close();  
}

}