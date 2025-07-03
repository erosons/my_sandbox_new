bowser = []
bowser.append(1)
bowser.append(2)
bowser.append(3)
bowser.append(4)
print(bowser)
# perform LIFO i.e browser removal
bowser.pop()
print(bowser)
#  conditonal statement if  browser is empty or not
if not bowser:
    bowser[-1]
print(bowser)
