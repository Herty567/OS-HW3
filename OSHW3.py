# Needed libraries
import threading
import time
import random


# Holds the value and the next pointer
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.lock = threading.Lock()


# Manages the linked list operations with thread safety
class ConcurrentLinkedList:
    def __init__(self):
        self.head = None
        self.head_lock = threading.Lock()  # Locks for head operations

    # Inserts a new value at the head of the list
    def insert(self, value):
        new_node = Node(value)
        with self.head_lock:
            new_node.next = self.head
            self.head = new_node

    # Searches for a value in the list
    def search(self, value):
        current = self.head
        while current:
            with current.lock:
                if current.value == value:
                    return True
                current = current.next
        return False

    # Deletes a value from the list
    def delete(self, value):
        with self.head_lock:
            current = self.head
            prev = None
            while current:
                with current.lock:
                    if current.value == value:
                        if prev:
                            prev.next = current.next
                        else:
                            self.head = current.next
                        return True
                    prev = current
                    current = current.next
            return False


# Measures the time for operations
def benchmark(linked_list, num_operations):
    operations = []

    # Randomly generate operations: insert, search, delete
    for _ in range(num_operations):
        op_type = random.choice(['insert', 'search', 'delete'])
        operations.append((op_type, random.randint(1, 100)))

    # Processes the operations
    def worker(ops):
        for op, val in ops:
            if op == 'insert':
                linked_list.insert(val)
            elif op == 'search':
                linked_list.search(val)
            elif op == 'delete':
                linked_list.delete(val)

    # Splits operations across multiple threads
    threads = []
    start_time = time.time()
    for i in range(4):
        thread_ops = operations[i * (num_operations // 4):(i + 1) * (num_operations // 4)]
        t = threading.Thread(target=worker, args=(thread_ops,))
        threads.append(t)
        t.start()

    # Waits for all threads to complete
    for t in threads:
        t.join()
    end_time = time.time()

    # Outputs the execution time
    print(f"Executed {num_operations} operations in {end_time - start_time:.4f} seconds.")


# Main execution block for testing different workloads
if __name__ == "__main__":
    cll = ConcurrentLinkedList()

    # Low workload
    print("Low workload (100 operations):")
    benchmark(cll, 100)

    # Medium workload
    print("Medium workload (1,000 operations):")
    benchmark(cll, 1000)

    # High workload
    print("High workload (10,000 operations):")
    benchmark(cll, 10000)
