from collections import deque
import string
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)

# perform FIFO i.e QUEUE elements removal from the every first entry
queue.popleft()
print(queue)
#  conditonal statement if  browser is empty or not
if not queue:
    print(queue)


"""
Deque is also known as deck which came from word double ended list
"""

d = deque(string.ascii_lowercase)

# TODO : deque support the len() function

print("Item count:", str(len(d)))


# TODO : deque can be iterated overyve

for elem in d:
    print(elem.upper(), end=",")

# TODO : remove elem and element from the deque
d.pop()
d.popleft()
d.append(1)
d.appendleft(2)
print(d)

# TODO :rotate item
print(d)
d.rotate(10)
print(d)
