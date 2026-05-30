#collectins are data structures that can hold multiple items. They include lists, tuples, sets, and dictionaries.
#list is a collection of items that are ordered and changeable. It allows duplicate members.
#set is a collection of items that are unordered and unindexed. It does not allow duplicate members.
#tuple is a collection of items that are ordered and unchangeable. It allows duplicate members.

fruits = ["apple", "banana", "cherry"]

fruits.append("orange")  # Add an item to the end of the list

print(fruits)  # ['apple', 'banana', 'cherry', 'orange']
for x in fruits:
    print(x) # apple banana cherry orange
