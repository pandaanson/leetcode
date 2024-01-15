import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:  # Maintain the heap size to be k
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:  # If the heap size exceeds k, pop the smallest element
            heapq.heappop(self.heap)
        return self.heap[0]  # The root of the heap is the kth largest element
