# Step 1: Create an empty list
my_list = []

# Step 2: Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After appending:", my_list)

# Step 3: Insert 15 at the second position (index 1)
my_list.insert(1, 15)
print("After inserting 15:", my_list)

# Step 4: Extend the list with [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extending:", my_list)

# Step 5: Remove the last element
my_list.pop()
print("After removing last element:", my_list)

# Step 6: Sort the list in ascending order
my_list.sort()
print("After sorting:", my_list)

# Step 7: Find and print the index of value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
