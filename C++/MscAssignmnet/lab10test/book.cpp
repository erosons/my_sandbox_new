#include "Book.h"
#include <iostream>
using namespace std;

Book::Book()
{

  ID = 0;
  title = "";
  price = 0.0;
  author = "";
}

Book::Book(int id, string Title, float Price, string Author)
{

  ID = id;
  title = Title;
  price = Price;
  author = Author;
}

void Book::setID(int id)
{
  ID = id;
}
int Book::getID()
    const
{
  return ID;
}
void Book::settitle(string Title)
{
  title = Title;
}
string Book::gettitle() const { return title; }
void Book::setprice(float Price) { price = Price; }
float Book::getprice() const { return price; }
void Book::setauthor(string Author) { author = Author; }
string Book::getauthor() const { return author; }
void Book::displayBookInfo() const
{
  cout << "The Book is ID:" << getID() << "\nThe Book Name :" << gettitle()
       << "\n Book Price is:" << getprice() << "\n Book author :" << getauthor()
       << "\n"
       << "----------------------"
       << "\n";
}
