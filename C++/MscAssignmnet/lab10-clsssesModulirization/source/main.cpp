using namespace std;
#include <iostream>
#include <cctype>
#include "/home/samson/my_sandbox/Engineering/C++/MscAssignmnet/lab10-clsssesModulizarion/header/student.h"



int main() {
  int Opsvalue;
  string terminateValue;
  int const SIZE = 10;
  Book bookList[SIZE];
  do {
    cout << "Please enter a number for the operation below you would like to perform today" << endl<<"\n";
    cout << "Enter: 1 To Purchase a new bookName : Write code that request users to the book Name you would like purchase" << endl;
    cout << "Enter: 2 To display a book purchased: Write code that request users to enter the Book ID they purchased" << endl;
    cout << "Enter: 3 Display all purchased books: Write a function that display "<< endl;
    cout << "Enter: 4  To exit the Operation" << endl;

    cin >> Opsvalue;
    // Ask if operation should terminate or not
    if (Opsvalue==1){
        int ID;
        string Title;
        float Price;
        string Author;

       for(int i =0; i<SIZE; i++){
            cout << "Enter the book ID"<< endl;
            cin >> ID;
            bookList[i].setID(ID);
            cout << "Enter the book Title"<< endl;
            cin >> Title;
            bookList[i].settitle(Title);
            cout << "Enter the book Price"<< endl;
            cin >> Price;
            bookList[i].setprice(Price);
            cout << "Enter the book Author"<< endl;
            cin >> Author;
            bookList[i].setauthor(Author);
       }
      }

    else if(Opsvalue==2){
         cout << "Which of the your purchased book list would you like to display";
         int noOfpuchasedbook;
         cin >> noOfpuchasedbook;
           //cout << bookList[i].displayBookInfo();
         }

    else if(Opsvalue==3){
       
        for(int i=0; i<SIZE; i++){
      
          //cout << bookList[i].displayBookInfo();     
          }
        }
    else
        cout << "Do you want to continue please enter Y/N ? " << endl;
        cin >> terminateValue;
  
 // } while (tolower(terminateValue) == 'Yes');
  } 
  while (terminateValue == "Y" || terminateValue == "y");
  
  return 0;
}
