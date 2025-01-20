#include <iostream>
#include <fstream>
using namespace std;


int main() {
// Create a text string, which is used to output the text file
string myText;

// Read from the text file
ifstream MyReadFile("filename.txt");
// Using  while loop together  with the getline(), this function read the file line by line
int e_count=0;
int big_e_count=0;
while (getline (MyReadFile, myText)) {
  // Output the text from the file
  cout << myText<< endl;
  for(int i=0; i<myText.length();i++){
    if(myText[i]=='e'){
       e_count++ ;
    }
    else if(myText[i]=='E'){
       big_e_count++ ;
    }
  }

  }
cout << e_count << endl;
cout << big_e_count << endl;
// Close the file
MyReadFile.close();

}

