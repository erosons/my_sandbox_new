#include <iostream>
using namespace std ;


struct Node
{
  int data;
  Node* link;
};

class IntegratedLinklist{

private:
 
  Node *head, *tail;
   
public:
  IntegratedLinklist(){
    tail=NULL;
    head=NULL;
  }

 void createNode(int value){

     Node* x=new Node();
     x->data=value;
     x->link =NULL; 
  
     if(head==NULL){
        head=x;
        tail=x;

        }
     else{
       head->link =x;
      }
   
    }
  void display(){
       Node* counter=head;
       while(counter !=NULL){
      cout << counter->data <<endl;
      counter=counter->link;
    }
  }

};



int main() {
IntegratedLinklist list;
list.createNode(1);
list.createNode(2);
list.createNode(3);
list.createNode(4);
list.createNode(5);
list.display();
 
return 0;
}