#include <iostream>
#include "/Users/s.eromonsei/my_sandbox/Engineering/C++/MscAssignmnet/Library_Inventory_Managment/Member.h"
#include "/Users/s.eromonsei/my_sandbox/Engineering/C++/MscAssignmnet/Library_Inventory_Managment/Library.h"


// Constructor
Member::Member(string name) {
    this->name = name;
}



// Borrow a book from library
void Member::borrow_book(Library& library, string isbn) {
    if (borrowed.size() == 3) {
        cout << "You have borrowed the maximum number of books allowed (3), ." << endl;
        cout << "Please return at one of the book borrowed books to have access to another book, ." << endl;
        return;
    }
    Node* current = library.head;
    while (current != nullptr) {
        if (current->book.get_isbn() == isbn && current->book.get_copies() > 0) {
            current->book.copies--;
            borrowed.push_back(current->book);
            cout << "You have borrowed \"" << isbn << "\" by " << current->book.get_author() << "." << endl;
            return;
        }
        current = current->next;

    }
    cout << "Book not available: " << isbn << endl;

}

// Return a book to library
void Member::return_book(Library& library, string  isbn) {
    for (int i = 0; i < borrowed.size(); i++) {
        if (borrowed[i].get_isbn() == isbn) {
            borrowed.erase(borrowed.begin() + i);
            Node* current = library.head;
            while (current != nullptr) {
                if (current->book.get_isbn() == isbn) {
                    current->book.copies++;
                    cout << "You have returned \"" << isbn << "\" by " << current->book.get_author() << "." << endl;
                    return;
                }
                current = current->next;
            }
        }
    }
    cout << "You have not borrowed \"" << isbn << "\"." << endl;
}

// Display all borrowed books
void Member::display_borrowed() {
    if (borrowed.size() == 0) {
        cout << "You have not borrowed any books." << endl;
    }
    cout << "Books you have borrowed:" << endl;
    for (int i = 0; i < borrowed.size(); i++) {
        cout << borrowed[i].get_isbn() << " by " << borrowed[i].get_author() << endl;
    }
};
