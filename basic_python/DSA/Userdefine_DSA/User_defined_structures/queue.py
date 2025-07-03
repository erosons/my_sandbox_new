# This ops is FIFO => which is First in First Out
# Queue is buffering system for implementing decoupled loose applications
# The python queue works similiarly Kafka logging system.
from collections import deque

class strem_queue:
    def __init__(self) -> None:
        self.buffer=deque()
    
    # This serves as the stream producer 
    def enqueue(self,data):      
      self.buffer.appendleft(data)
      return  self.buffer
    
    # # This serves as the bulk stream producer 
    def enqueue_multiple_data(self,datalist):      
      self.buffer.extendleft(datalist)
      return  self.buffer

     # Because stream is appending from the left based
     # On when they arrived the pop ops work as First in is the First Out
    def dequeue(self):      
      self.buffer.pop()
      return  self.buffer
    
    def queue_size(self):      
      return self.buffer.count()
      
    def size_of_queue(self):      
      return len(self.buffer)