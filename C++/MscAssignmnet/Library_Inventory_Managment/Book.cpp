#include "/Users/s.eromonsei/my_sandbox/Engineering/C++/MscAssignmnet/Library_Inventory_Managment/Book.h"


Book::Book()
{
    title = "";
    author = "";
    genre = "";
    year = 0;
    copies = 0;
    isbn = "";
}

// Constructor
Book::Book(string title, string author, string genre, int year, int copies, string isbn) {
    this->title = title;
    this->author = author;
    this->genre = genre;
    this->year = year;
    this->copies = copies;
    this->isbn = isbn;
}



// Getters
string Book::get_title() const {
    return title;
}


void Book::set_copies(int Copies) {
    this->copies = Copies;
}

string Book::get_author() const {
    return author;
}

string Book::get_genre() const {
    return genre;
}

int Book::get_year() const {
    return year;
}

int Book::get_copies() const {
    return copies;
}

string Book::get_isbn() const {
    return isbn;
};