# Enter your code here. Read input from STDIN. Print output to STDOUT
import heapq

def main():
    # Read the number of queries
    Q = int(input().strip())

    heap = []
    
    for _ in range(Q):
        query = list(map(int, input().strip().split()))

        operation = query[0]

        if operation == 1:
            # Insert element into the heap
            heapq.heappush(heap, query[1])
        elif operation == 2:
            # Remove specific element from the heap
            # Note: heapq does not support direct removal, so we rebuild the heap without the element
            heap.remove(query[1])
            heapq.heapify(heap)
        elif operation == 3:
            # Print the minimum element in the heap
            if heap:
                print(heap[0])
            else:
                print("Heap is empty")

if __name__ == "__main__":
    main()
