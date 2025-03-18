"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Work some of the more advanced features of lists in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Here is a list of 10 fruits:
fruits = ["Grape", "Apple", "Lemon", "Cherry", "Date", "Elderberry", "Fig",  "Honeydew", "Kiwi", "Banana"]


# Remove the third fruit from the list using the pop() method.
fruits.pop(2)
print(fruits)

# Use the remove() method to remove a fruit of your choice from the list.
fruits.remove("Date")
print(fruits)

# Search for "Apple" in the list and print a message saying whether or not it was found.
try:
    position = fruits.index("Fig")
    print(f"Fig is at {position} in list")
except:
    print("Fig not found")

# Sort the List in alphabetical order.
fruits.sort()
print(fruits)

# Create a new list that contains a slice of the first 5 items
first_half = fruits[0:3]

# Print out the new sliced list using a for loop
for fruit in first_half:
    print(fruit)