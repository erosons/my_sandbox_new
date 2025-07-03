#pragma once
#include <string>
using namespace std;

class Book
{

public:

    string title;
    string author;
    string genre;
    int year;
    int copies;
    string isbn;


    // Constructor
    Book(string title, string author, string genre, int year, int copies, string isbn);
    Book();
    string get_title() const;
    int get_copies() const;
    string get_author() const;
    string get_genre() const;
    int get_year() const;
    //int get_copies() const;
    void set_copies(int copies);
    string get_isbn() const;

};
