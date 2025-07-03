# This ops is LIFO => which is Last in First Out
#Basically the use is UNDO  which is available in most system
# Example => When a user visit a page and navigate to multiple other pages, 
# the user can use undo button to navigate back to the first page
# This is similiar to what happen when you undo in microsoft word or excel => This action is pop()

from collections import deque

class Stack_ops:
  def __init__(self):
    self.container=deque()

  # Add the messages stream sequentially 
  def stackadd(self, key):
     self.container.append(key)
     return  self.container

  # Add bulk messages stream sequentially 
  def stack_extend(self,datalist):      
      self.container.extend(datalist)
      return  self.container

  # This is also a queue operations removes Last in the First Out
  # Because stream is appending from the right based
  # on when the work stream arrived the pop ops work as Last in is the First Out
  def pop(self):      
      self.container.pop()
      return  self.container
 
  def popleft(self):      
      self.container.popleft()
      return  self.container


  def stack_rotate(self,number_of_times):      
      self.container.rotate(number_of_times)
      return  self.container




testSc=Stack_ops()
testSc.stack_array("Apple")
testSc.stack_array("Orange")
testSc.stack_array("Grape")
testSc.stack_array("Juice")

testSc.stack()