📝 Python List Operations Example


📚 Table of Contents

Overview

Features

Code Explanation

Example Output

How to Run

Learning Points

License

📌 Overview

This Python script demonstrates basic list operations in Python, including adding, inserting, extending, removing, sorting, and finding elements.
It’s perfect for beginners learning Python data structures.

🛠 Features

✅ Create an empty list

✅ Append elements to the list

✅ Insert an element at a specific position

✅ Extend a list with another list

✅ Remove the last element

✅ Sort the list in ascending order

✅ Find the index of a specific element

📜 Code Explanation
# Step 1: Create an empty list
my_list = []

# Step 2: Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Insert 15 at the second position (index 1)
my_list.insert(1, 15)

# Step 4: Extend with another list
my_list.extend([50, 60, 70])

# Step 5: Remove the last element
my_list.pop()

# Step 6: Sort in ascending order
my_list.sort()

# Step 7: Find and print the index of 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

💻 Example Output
Index of 30: 3

🚀 How to Run

Save the code in a file named list_operations.py

Open a terminal/command prompt and navigate to the file’s directory.

Run:

python list_operations.py

📚 Learning Points

Lists in Python are mutable, meaning they can be changed after creation.

.append() → Add elements to the end of the list.

.insert(index, value) → Add an element at a specific index.

.extend() → Merge two lists.

.pop() → Remove the last element (or by index).

.sort() → Arrange elements in ascending order.

.index() → Find the position of an element.