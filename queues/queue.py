from collections import deque

# Initialize an empty deque
queue = deque()

# Add elements to the right end of the deque
queue.append(1)
queue.append(2)
queue.append(3)

print('Initial Queue:')
print(queue)

# Remove and return an element from the left end of the deque
queue.popleft()
print('\nLeft Elements popped from queue:')
print(queue)

# Add an element to the left end of the deque
queue.appendleft(1)
print('\nAdd element to the left:')
print(queue)

# pop() function to pop element from stack in LIFO order
print('\nElements popped from stack:')
print(queue.pop())
print(queue.pop())
print(queue.pop())

print('\nQueue after elements are popped:')
print(queue)
