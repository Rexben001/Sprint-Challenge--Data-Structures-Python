import time
from binary_search import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

bstree = BinarySearchTree(names_1[0])
for name_1 in range(1, len(names_1)):
    bstree.insert(names_1[name_1])

for name_2 in names_2:
    if bstree.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")