import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = sticks
        heapq.heapify(heap)
        ans=0
        while len(heap)>1:
            temp1 = heapq.heappop(heap)
            temp2 = heapq.heappop(heap)
            ans+=temp1+temp2
            heapq.heappush( heap, temp1+temp2)

        return ans
