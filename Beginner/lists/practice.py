'''
 1.  What is []?
A = It is a representation of an empty list
  2.  How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
A = spam[2] = "hello"
For the following three questions, assume spam contains the list ['a', 'b', 'c', 'd'].

  3.  What does spam[int(int('3' * 2) // 11)] evaluate to?
A = The index with the number 3 in the list with the value 'd'
  4.  What does spam[-1] evaluate to?
A = The last item in the list
  5.  What does spam[:2] evaluate to?
A = The first two items in the list
For the following three questions, assume bacon contains the list [3.14, 'cat', 11, 'cat', True].

  6.  What does bacon.index('cat') evaluate to?
A = returns the index of cat which is 1
  7.  What does bacon.append(99) make the list value in bacon look like?
A = add 99 integer at the end of the list
  8.  What does bacon.remove('cat') make the list value in bacon look like?
A = It will remove the first element with the name 'cat' because there are 2 of them
  9.  What are the operators for list concatenation and list replication?
A = For list concatenation we use + and for list replication we use *
10.  What is the difference between the append() and insert() list methods?
A = With append() we add the item to the end of the list while usind insert() we can indicate in which index we want the item be inserted
11.  What are two ways to remove values from a list?
A = using remove() and using del
12.  Name a few ways that list values are similar to string values.
A = They are similar because they have indexs, you can call them by the index and you can iterate over this
13.  What is the difference between lists and tuples?
A = The main difference is the lists are mutable values while the tuples are inmutable
14.  How do you write the tuple value that has just the integer value 42 in it?
A = name_of_tuple(42,)
15.  How can you get the tuple form of a list value? How can you get the list form of a tuple value?
A = tuple(list_name) and list(tuple_name)
16.  Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
A = This variables are references for the values into the list
17.  What is the difference between copy.copy() and copy.deepcopy()?
A = with copy we only copy the direct list we are referencing to while using deepcopy() we go inside that list and copy what's inside
'''

print(int('3' * 2)//11)