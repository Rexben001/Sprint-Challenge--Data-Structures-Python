import time
from binary_search import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


# Try binary search
names_1.sort()
names_2.sort()


def binary(arr, target):
    if len(arr) == 0:
        return False

    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low+high)//2

        if arr[middle] == target:
            return True
        if arr[middle] > target:
            high = middle - 1
        if arr[middle] < target:
            low = middle + 1


dup2 = []
for i in names_2:
    if binary(names_1, i):
        dup2.append(i)


end_time = time.time()
print(f"{len(dup2)} dup2:\n\n{', '.join(dup2)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
