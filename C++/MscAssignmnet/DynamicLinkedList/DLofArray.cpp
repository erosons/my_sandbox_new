
#include <iostream>

using namespace std;

struct node
{
    int data;
    node *next;
};

class linked_list
{
private:
    node *head,*tail;
public:
    linked_list()
    {
        head = NULL;
        tail = NULL;
    }

    void add_node(int n)
    {
        node *tmp = new node;
        tmp->data = n;
        tmp->next = NULL;

        if(head == NULL)
        {
            head = tmp;
            tail = tmp;
        }
        else
        {
            tail->next = tmp;
            tail = tail->next;
        }
    }

    void display()
    {
        node *tmp;
        tmp = head;
        while (tmp != NULL)
        {
            cout << tmp->data << "->";
            tmp = tmp->next;
        }
    }
};

int main()
{
    linked_list a;
    cout << "Please enter your values"<< endl;
    int counter=0;
    int userinput;
    while(counter<5){
    counter ++;
    cin >> userinput;
    a.add_node(userinput);
    }
    a.display();
    return 0;
}

