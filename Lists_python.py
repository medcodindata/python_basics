
a = [1]
""" *****************   Add a value to a list   ****************************"""
a.append(2)         # => a = [1,2]

"""******  Extend a list by appending all element from an iterable *********"""
a.extend([3, 4])    # => a = [1,2,3,4]

""""********** Insert an element at a given position in a list  ************"""
a.insert(1, 5)      # => a = [1,5,2,3,4]

"""************  Remove the first occurred element from a list   ***********"""
a.append(5)         # => a = [1,5,2,3,4,5]
a.remove(5)         # => a = [1,2,3,4,5] the first 5 were removed

"""************ Get the value at a given position and remove it  **********"""
a.pop(2)            # return 3 => a = [1,2,4,5]

"""************ Get the last value and remove it from the list ************"""
a.pop()             # return 5 =>  a = [1,2,4]

"""************ Count the occurrence of an element in a list **************"""
a.count(2)          # return 1 because a = [1,2,4]

"""*************************** Sort a list ********************************"""
a.sort()            # ascending order =>  a = [1,2,4]
a.sort(reverse=True)# descending order => a = [4,2,1]

"""*************************** Get the index of an element   **************"""
a.index(4)          # return 0 because a = [4,2,1]

"""************************** Truncate a list *****************************"""
a.clear()           # a = []
