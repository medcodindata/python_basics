a = {1}
print(type(a)) # return <class 'set'>

""" ************  add a value to a set *********** """
a.add(2)  # a = {1, 2}
# add it again
a.add(2)  # => sets cannot contains duplicated values => a = {1, 2}
""" ******** remove an element ********* """
a.pop() # return 1 and a = {2}
""" ************  copy a set ********* """
# case of = operator
b = a # => a = {1} and b = {1}
b.add(2) # a = {1, 2} and b = {1, 2} yes the a is modified too
# case of copy() method
b = a.copy() # => a = {1, 2} and b = {1, 2}
b.add(3) # a = {1, 2} and b = {1, 2, 3} cool !!
""" ************   difference between two sets ************ """
b.difference(a)  # return {3}, because a = {1, 2} and b = {1, 2, 3}
