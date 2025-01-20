using namespace std;
#include "Book.h"
#include <cctype>
#include <iostream>

int main() {
  int Opsvalue;
  string terminateValue;
  int SIZE = 10;

  Book Book1;
  Book Book2;
  Book Book3;
  Book Book4;
  Book Book5;
  Book Book6;
  Book Book7;
  Book Book8;
  Book Book9;
  Book Book10;

  Book bookList[SIZE];
  bookList[0] = Book1;
  bookList[1] = Book2;
  bookList[2] = Book3;
  bookList[3] = Book4;
  bookList[4] = Book5;
  bookList[5] = Book6;
  bookList[6] = Book7;
  bookList[7] = Book8;
  bookList[8] = Book9;
  bookList[10] = Book10;
  do {
    cout << "Please enter a number for the operation below you would like to "
            "perform today"
         << endl
         << "\n";
    cout << "Enter: 1 To Purchase a new bookName : Write code that request "
            "users to the book Name you would like purchase"
         << endl;
    cout << "Enter: 2 To display a book purchased: Write code that request "
            "users to enter the Book ID they purchased"
         << endl;
    cout << "Enter: 3 Display all purchased books: Write a function that "
            "display "
         << endl;
    cout << "Enter: 4  To exit the Operation" << endl;

    cin >> Opsvalue;
    // Ask if operation should terminate or not
    if (Opsvalue == 1) {
      int ID;
      string Title;
      float Price;
      string Author;

      for (int i = 0; i < SIZE; i++) {
        cout << "Enter the book ID" << endl;
        cin >> ID;
        bookList[i].setID(ID);
        cout << "Enter the book Title" << endl;
        cin >> Title;
        bookList[i].settitle(Title);
        cout << "Enter the book Price" << endl;
        cin >> Price;
        bookList[i].setprice(Price);
        cout << "Enter the book Author" << endl;
        cin >> Author;
        bookList[i].setauthor(Author);
      }
    }

    else if (Opsvalue == 2) {
      cout << "Which of the your purchased book list would you like to display"
           << endl;
      int noOfpuchasedbook;
      cin >> noOfpuchasedbook;
      bookList[noOfpuchasedbook].displayBookInfo();
    }

    else if (Opsvalue == 3) {

      for (int i = 0; i < SIZE; i++) {

        bookList[i].displayBookInfo();
      }
    }

    cout << "Do you want to continue please enter Y/N ? " << endl;
    cin >> terminateValue;

    // } while (tolower(terminateValue) == 'Yes');
  } while (terminateValue == "Y" || terminateValue == "y");

  return 0;
}
