import heapq

# 1. Creating a Heap
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(numbers)  # Transform list into a heap, in-place
print("Heap:", numbers)

# 2. Inserting into a Heap
heapq.heappush(numbers, 8)  # Adds element to the heap
print("After inserting 8:", numbers)

# 3. Removing from a Heap
smallest = heapq.heappop(numbers)  # Removes the smallest element
print("Smallest element:", smallest)
print("Heap after removing the smallest element:", numbers)

# 4. Accessing the Smallest Item
print("Smallest item without removing:", numbers[0])

# 5. Transforming a List into a Heap In-place
new_numbers = [10, 1, 7, 3, 2, 8, 4]
heapq.heapify(new_numbers)
print("New heap:", new_numbers)

# 6. Heap Sort
def heap_sort(iterable):
  h = []
  for value in iterable:
    heapq.heappush(h, value)
  return [heapq.heappop(h) for i in range(len(h))]

sorted_numbers = heap_sort([5, 3, 8, 1, 2, 7])
print("Sorted numbers:", sorted_numbers)

# Explanation:
# 1. `heapify` transforms a list into a heap. The smallest element is moved to the root.
# 2. `heappush` adds a new element to the heap while maintaining the heap property.
# 3. `heappop` removes and returns the smallest element from the heap, adjusting the heap accordingly.
# 4. The smallest item can be accessed directly as the first item in the list.
# 5. Demonstrates again how `heapify` can be used to convert a list into a heap.
# 6. `heap_sort` function demonstrates how to perform a heap sort. It builds a heap from the elements and then pops the smallest elements one by one to get a sorted list.

'''A heap is a specialized tree-based data structure that satisfies the heap property. In a heap, for any given node C, if P is a parent node of C, then the key (the value) of P is either greater than or equal to (in a max heap) or less than or equal to (in a min heap) the key of C. The node at the "top" of the heap (with no parents) is called the root node.

The heap is one efficient way of implementing a priority queue, which is an abstract data type designed to manage a collection of records with totally or partially ordered keys (e.g., a to-do list where some tasks are more important than others).

Key Characteristics of Heaps:
Heap Property: The key property of a heap, which can be of two types:
Max Heap: In a max heap, for any given node C, the key of C is less than or equal to the key of its parent P. The maximum element is at the root.
Min Heap: In a min heap, for any given node C, the key of C is greater than or equal to the key of its parent P. The minimum element is at the root.
Complete Binary Tree: A heap is a complete binary tree. This means it is a binary tree in which all the levels, except possibly the last one, are fully filled, and all nodes are as far left as possible.
Efficient Operations: Heaps allow a number of efficient operations, including inserting a new element, merging two heaps, and removing the root node (the largest element in a max heap or the smallest in a min heap). These operations can typically be performed in logarithmic time complexity.
Implementation: Heaps are usually implemented using arrays, where the relationships between parent and child nodes can be represented using indices. For a node at index i, its children are at indices 2*i + 1 and 2*i + 2, and its parent is at index (i-1)/2.'''