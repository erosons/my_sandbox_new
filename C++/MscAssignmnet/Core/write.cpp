#include <iostream>
using namespace std;
#include <cmath>
#include <fstream>

void write();


int main(){
  
  write();

  }


void write(){
  
ofstream outputfile;

outputfile.open("name.txt");
outputfile << "Hello Samson\n";
outputfile << "How are you\n";
outputfile << "Today\n";

outputfile.close();
  }
