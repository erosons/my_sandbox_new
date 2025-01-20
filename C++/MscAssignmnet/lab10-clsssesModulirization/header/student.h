#include <iostream>
using namespace std;




class Book{

private:
    int ID;
    string title;
    float price;
    string author;


public:
   Book();
   Book(int id,string Title,float Price,string Author);
   void setID(int id);
   void settitle(string Title);
   void setprice(float Price);
   void setauthor(string Author);
   int getID() const;
   string gettitle() const;
   float getprice() const;
   string getauthor() const;
   void displayBookInfo() const;

};