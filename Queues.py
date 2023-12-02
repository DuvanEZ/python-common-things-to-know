# Import deque from the collections module
from collections import deque

# Initialize a deque
queue = deque()

# Append 1 and 2 to the right end of the deque
queue.append(1)
queue.append(2)

# Print the current state of the deque
print(queue)  # Output: deque([1, 2])

# Remove and return the leftmost element of the deque
queue.popleft()

# Print the current state of the deque
print(queue)  # Output: deque([2])

# Append 1 to the left end of the deque
queue.appendleft(1)

# Print the current state of the deque
print(queue)  # Output: deque([1, 2])

# Remove and return the rightmost element of the deque
queue.pop()

# Print the current state of the deque
print(queue)  # Output: deque([1])