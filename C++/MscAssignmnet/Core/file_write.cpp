#include <iostream>
#include <fstream>
using namespace std;

//ofstream	Creates and writes to files
//ifstream	Reads from files
//fstream	A combination of ofstream and ifstream: creates, reads, and writes to files

int main() {
  // Create and open a text file
  ofstream MyFile("filename.txt");

  // Write to the file
  MyFile << "Files can be tricky, but it is fun enough!";

  // Close the file
  MyFile.close();
}