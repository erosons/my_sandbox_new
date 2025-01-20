#include <iostream>
using namespace std;

int main()
{

  string Book[5];
  int arraylength = sizeof(Book) / sizeof(string);
  string x;
  int counter = 0;
  cout << " Storing Values in the array" << endl;
  while (counter < arraylength)
  {
    cin >> Book[counter];
    counter++;
  }
  string *ptr;
  ptr = Book;
  cout << "Print a ponter mapped to Book" << endl;
  for (int i = 0; i < arraylength; i++)
  {
    cout << ptr[i] << endl;
  }
  return 0;
}