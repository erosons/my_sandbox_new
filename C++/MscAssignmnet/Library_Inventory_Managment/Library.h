#pragma once
#include <string>
#include <vector>
#include "/Users/s.eromonsei/my_sandbox/Engineering/C++/MscAssignmnet/Library_Inventory_Managment/Book.h"
using namespace std;


// Node class for linked list
class Node {
public:
    Book book;
    Node* next;
    Node(const Book& book);
};

// Library class
class Library {
public:
    // Initital a variable pointer head of a linkedlist
    Node* head;
    // Constructor
    Library();
    //Add book to the Library
    void add_book(string title, string author, string genre, int year, int copies, string isbn);
    //Remove book from the Library
    void remove_book(string isbn);
    // Display books in the Library
    void display_books();
    Node* search_book(string isbn);
    Node* merge_sort(Node* head);
    Node* find_middle(Node* head);
    Node* merge(Node* left, Node* right);
    int count_books();
    void sort_books();

};

