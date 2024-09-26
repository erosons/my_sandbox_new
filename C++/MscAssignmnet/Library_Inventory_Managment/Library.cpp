#include <iostream>
#include "/Users/s.eromonsei/my_sandbox/Engineering/C++/MscAssignmnet/Library_Inventory_Managment/Library.h"


//Node::Node(Book book){};

Node::Node(const Book& book) : book(book), next(nullptr) {}

// Constructor
Library::Library() {
    head = nullptr;
};


// Add book to library
void Library::add_book(string title, string author, string genre, int year, int copies, string isbn) {
    Book new_book(title, author, genre, year, copies, isbn);
    Node* new_node = new Node(new_book);
    if (head == nullptr) {
        head = new_node;
    }
    else {
        Node* current = head;
        while (current->next != nullptr) {
            current = current->next;
        }
        current->next = new_node;
    }
    cout << "Book added: " << isbn << endl;
}

// Remove book from library
void Library::remove_book(string isbn) {
    if (head == nullptr) {
        cout << "Library is empty." << endl;
        return;
    }
    // Library inherit the public functions of the book Class
    else if (head->book.get_isbn() == isbn) {
        Node* temp = head;
        head = head->next;
        delete temp;
        cout << "Book removed: " << isbn << endl;
        return;
    }
    else {
        Node* current = head;
        while (current->next != nullptr && current->next->book.get_isbn() != isbn) {
            current = current->next;
        }
        if (current->next == nullptr) {
            cout << "Book not found: " << isbn << endl;
            return;
        }
        else {
            Node* temp = current->next;
            current->next = current->next->next;
            delete temp;
            cout << "Book removed: " << isbn << endl;
            return;
        }
    }
}
// Display all books in library
void Library::display_books() {
    if (head == nullptr) {
        cout << "Library is empty." << endl;
        return;
    }
    Node* current = head;
    cout << "Books in library:" << endl;
    while (current != nullptr) {
        cout << "Publisher No" << " " << current->book.get_isbn() << " " << "for" 
            << current->book.get_title() << " " << " by " << current->book.get_author() << endl;
        current = current->next;
    }
}


//Binary search for book in the Library
Node* Library::search_book(string isbn) {
    int left = 0;
    int right = count_books() - 1;  
    //Sort Operation 
    //merge_sort(head);
    sort_books();
    Node* current = head;
    cout << " " << "First Book Isbn in Ascending order" <<  " " << head->book.get_isbn() << endl;
    while (left <= right) {
            int mid = left + (right - left) / 2; 
            
            for (int i = 0; i < mid; i++) {

                current = current->next;
            }

            if (current->book.get_isbn() == isbn) {
                cout << current->book.get_isbn() << " " << current->book.get_title() << endl;
                return current;
            }
            else if (current->book.get_isbn() < isbn) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        
    }
    cout << "The Book not found in the Library" << endl;
    return nullptr;
}




// Count the number of books in the library
int Library::count_books() {
    int count = 0;
    Node* current = head;
    while (current != nullptr) {
        count++;
        current = current->next;
    }
    return count;
};



// Sort the books in Ascending order base on their title
void Library::sort_books() {
    head = merge_sort(head);
}


// Recursive function uses a divide linked list into two equal halves and sort each half recursively
// using merge sort and then merg the sorted halves using the merge helper function
// conquer approach  uses a linked list and call merge() function
//The merge function takes two sorted linked lists as input and returns a single sorted linked list
//  that contains all the nodes from both input lists. 
//The function compares the titles of the books in the input nodes, and links the nodes together 
// in ascending order based on the title comparison result.
//Overall, the Merge Sort algorithm has a time complexity of O(n log n),
//where n is the number of books in the Library.This makes it an efficient algorithm for sorting 
// a large number of books in the Library.

// helper Function1 


Node* Library::merge_sort(Node* head) {
    if (head == nullptr || head->next == nullptr) {
        return head;
    }
    Node* mid = find_middle(head);
    Node* left = head;
    Node* right = mid->next;
    mid->next = nullptr;
    left = merge_sort(left);
    right = merge_sort(right);
    return merge(left, right);
}

// Helper function to find the middle node of a linked list
Node* Library::find_middle(Node* head) {
    if (head == nullptr || head->next == nullptr) {
        return head;
    }
    Node* slow = head;
    Node* fast = head->next;
    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
};


// Helper function to merge the the splited into a single list.
Node* Library::merge(Node* left, Node* right) {
    Node* result = nullptr;
    if (left == nullptr) {
        return right;
    }
    else if (right == nullptr) {
        return left;
    }
    //else if (left->book.get_title() <= right->book.get_title()) {
    else if (left->book.get_isbn() <= right->book.get_isbn()) {
        result = left;
        result->next = merge(left->next, right);
    }
    else {
        result = right;
        result->next = merge(left, right->next);
    }
    return result;
}


