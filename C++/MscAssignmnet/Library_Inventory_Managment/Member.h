#pragma once
#pragma once
#include <vector>
#include <string>
#include "/Users/s.eromonsei/my_sandbox/Engineering/C++/MscAssignmnet/Library_Inventory_Managment/Book.h"
#include "/Users/s.eromonsei/my_sandbox/Engineering/C++/MscAssignmnet/Library_Inventory_Managment/Library.h"

using namespace std;

// Member class
class Member {
public:
    string name;
    vector<Book> borrowed;


    // Constructor
    Member(string name);
    void borrow_book(Library& library, string isbn);
    void return_book(Library& library, string  isbn);
    void display_borrowed();
};