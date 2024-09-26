"""
Linked list try to solve the following issues
  - Swap operation that happens durring Insert and delete Operation which is O(n)
  - Reallocating and copying elements from one memory location to another memory due to running out allocation space 
    result in creation on 3*times the original space.

  Note when creating a new memory it uses nth term Geometry with common ratio=2 a(r)^n 
  So if the initial size of the dynamic array is 10, python will 10 + 10(2)^1  => 30

Typically Array/List stores values in contingous location in memeory.
   But in linked list values are stores in random memory location with each element having the REFERENCE ADDRESS to the next element

   - Insert Elements at the begining =O(1)  || in Array is O(n)
   - Delete Elements at the begining =O(1)  || in Array is O(n)
   - Indexing a Linked List because you have to traverse =O(n) || in Array is O(1)
   - Insert Elements in the Middle because you have to traverse  = O(n) || in Array is O(n)
   - Insert/Delete Elemets at the end because you have to traverse =O(n) || O(1) in Array if the 
"""


class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

# TODO: Below we are creating the head of the linked List


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_begining(self, data):
        # This basically call the Node class above to create new node and inserting at the head/beginning
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is Empty")
            return

        itr = self.head
        linkedlist_str = ''  # I will use this string to print my linkedlist
        while itr:
            linkedlist_str += str(itr.data) + '->'
            itr = itr.next
        print(linkedlist_str)

    # I will be using this approach to insert values at the end of the linked list
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    # Create a how new list of multiple values adding to existing existing
    def insert_multiple_values_from_begining(self, data_list):
        if self.head is not None:
            for data in data_list:
                self.insert_at_begining(data)

    # Create a how new list of multiples values at the end of an existing list
    def insert_new_list_of_multiple_at_end(self, data_list):
        if self.head is not None:
            for data in data_list:
                self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr.next:
            count += 1
            itr = itr.next
        return count

    def remove_at_index(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next

            itr = itr.next
            count += 1

    def insert_at_index(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        elif index == 0:
            self.head = self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = Node(data, itr.next)
                break

            itr = itr.next
            count = count + 1


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(80)
    ll.insert_at_begining(100)
    # ll.inser_at_end(80)
    ll.insert_multiple_values_from_begining([1, 2, 3, 4])
    ll.insert_new_list_of_multiple_at_end([1, 2, 3, 4])
    ll.remove_at_index(2)
    ll.insert_at_index(3, 40)
    ll.print()
    ll.insert_at_index(2, 50)
    # print("length :", ll.get_length())
    ll.print()

# Output 100-->80-->5-->
