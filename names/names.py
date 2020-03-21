import time

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert value into tree
    def insert(self, value):
        # check if new value is less than current node
        if value < self.value:
            # if there is no self.left value
            if not self.left:
                # set the new left child to new value
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)


    def contains(self, target):
        # if root node equals target return
        if self.value == target:
            return True
        
        # target is smaller, go left
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

binary_search_tree = BinarySearchTree(names_1[0])
for i in range(1, len(names_1)):
    binary_search_tree.insert(names_1[i])

for j in range(len(names_2)):
    if binary_search_tree.contains(names_2[j]):
        duplicates.append(names_2[j])

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
