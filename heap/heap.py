class MinHeap:
    def __init__(self) -> None:
        """
        On this implementation the heap list is initialized with a value
        """

        self.heap_list = [0]
        self.current_size = 0
    
    def sift_up(self, i):
        """
        Moves the value up in the tree to maintain the heap property
        """

        # While the element is not the root or left element
        stop = False
        while (i // 2 > 0) and not stop:
            # If the element is less that its parent swap the element
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            else:
                stop = True
            # Move the index to the parent to keep the properties
            i = i // 2
    
    def insert(self, k):
        """
        Inserts a value into the heap
        """
        # Append the element to the heap
        self.heap_list.append(k)
        # Increase the size of the heap.
        self.current_size += 1
        # Move the element to its position from bottom to the top
        self.sift_up(self.current_size)

    def sift_down(self, i):
        # If the current node has at least one child
        while (i * 2) <= self.current_size:
            # Get the index of the min child of the current node
            mc = self.min_child(i)
            # Swap the values of the current element
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc
    
    def min_child(self, i):
        # If the current node has only one child, return the index of the unique child
        if (i * 2) + 1 <= self.current_size:
            left_child = i * 2
            right_child = (i * 2) + 1
            return left_child if self.heap_list[left_child] < self.heap_list[right_child] else right_child
        else:
            return i * 2
    
    def delete_min(self):
        # Equal to 1 since the heap list was initialized with a value
        if len(self.heap_list) == 1:
            return 'Empty heap'

        # Get root of the heap (The min value of the heap)
        root = self.heap_list[1]

        # Move the last value of the heap to the root
        self.heap_list[1] = self.heap_list[self.current_size]

        # Pop the last value since a copy was set on the root
        self.heap_list.pop()

        # Decrease the size of the heap
        self.current_size -= 1

        # Move down the root (value at index 1) to keep the heap property
        self.sift_down(1)

        # Return the min value of the heap
        return root

"""
Driver program
"""

# Example usage:
min_heap = MinHeap()
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(8)
min_heap.insert(1)

print("Initial Min Heap:", min_heap.heap_list)

min_value = min_heap.delete_min()
print(f"Minimum value deleted: {min_value}")

print("After Deletion Min Heap:", min_heap.heap_list)

min_heap.insert(2)

print("After Insertion Min Heap:", min_heap.heap_list)

sorted_values = []
while min_heap.current_size > 0:
    sorted_values.append(min_heap.delete_min())

print("Sorted values:", sorted_values)
