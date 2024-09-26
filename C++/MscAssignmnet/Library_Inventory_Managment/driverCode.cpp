#include <iostream>
#include "/Users/s.eromonsei/my_sandbox/Engineering/C++/MscAssignmnet/Library_Inventory_Managment/Library.h"
#include "/Users/s.eromonsei/my_sandbox/Engineering/C++/MscAssignmnet/Library_Inventory_Managment/Member.h"

using namespace std;

int main() {
    Library library;
    Member user("Modupe Ifafore");

    // Adding sample books to the library
    library.add_book("The Catcher in the Rye", "J.D. Salinger", "Thriller", 1951, 5, "F9789");
    library.add_book("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960, 4, "F5479");
    library.add_book("1984", "George Orwell", "Fiction", 1949, 3, "B8906");
    library.add_book("In no order", "Peter Patay", "Non-Fiction", 1951, 5, "M9789");
    library.add_book("Eve of the Massacre", "Hartinton AdLee", "Science Fiction", 2001, 4, "A1890");
    library.add_book("Ten times", "Pepple Ibinoye", "Novel", 2005, 5, "B8906");
    library.add_book("Who did", "Mark Olisa", "Fiction", 1951, 5, "M9789");
    library.add_book("Untouchable", "Ola Dempton", "Romance", 1994, 9, "A5450");
    library.add_book("Replica", "Simpson Butcher", "Horror", 1949, 8, "C2505");

    // Display all books in the library
    library.display_books();
    // Interactive user interface
    int choice;

    while (true) {
        cout << "\n--- Library System Menu ---" << endl;
        cout << "1. Add books to the Library" << endl;
        cout << "2. Display all books in the Library" << endl;
        cout << "3. To borrow a book" << endl;
        cout << "4. To Return a book" << endl;
        cout << "5. To Display borrowed books" << endl;
        cout << "6. To search for a book" << endl;
        cout << "7. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
        {
            string title, author, genre, isbn;
            int year, copies;

            cout << "Enter the book title: ";
            cin.ignore();
            getline(cin, title);

            cout << "Enter the author's name: ";
            getline(cin, author);

            cout << "Enter the book genre: ";
            getline(cin, genre);

            cout << "Enter the publication year: ";
            cin >> year;

            cout << "Enter the number of copies: ";
            cin >> copies;

            cout << "Enter the ISBN: ";
            cin >> isbn;

            library.add_book(title, author, genre, year, copies, isbn);
            cout << "Book added successfully!" << endl;
        }
        break;

        case 2:
            library.display_books();
            break;
        case 3:
        {
            string isbn;
            cout << "Enter the ISBN of the book you want to borrow: ";
            cin >> isbn;
            user.borrow_book(library, isbn);
        }
        break;
        case 4:
        {
            string isbn;
            cout << "Enter the ISBN of the book you want to return: ";
            cin >> isbn;
            user.return_book(library, isbn);
        }
        break;
        case 5:
            user.display_borrowed();
            break;
        case 6:
        {
            string isbn;
            cout << "Enter the isbn for the book you want to search for: ";
            cin >> isbn;
            library.sort_books();
            library.search_book(isbn);
        };
            break;
        case 7:
            cout << "Exiting the library system." << endl;
            return 0;
        default:
            cout << "Invalid choice. Please try again." << endl;
        }
    }

    return 0;
}
