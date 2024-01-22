import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        """
        Problem Statement:
        Given 'k' lists of sorted integers, find the smallest range that includes at least one number
        from each of the 'k' lists.

        Example:
        nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
        Output: [20,24]
        The range [20,24] includes at least one number from each list and is the smallest such range.
        """

        # Initialize the priority queue (min heap) and the variable 'ma' for the maximum value in the current range
        pq = []
        ma = float('-inf')  # Start with the smallest possible integer

        # Populate the priority queue with the first element of each list and update 'ma'
        for i in range(len(nums)):
            heapq.heappush(pq, (nums[i][0], i, 0))  # Push (element, list index, element index)
            ma = max(ma, nums[i][0])  # Update 'ma' to the maximum of the first elements

        # Initialize the answer with the initial range [smallest element, ma]
        ans = [pq[0][0], ma]

        # Process the priority queue
        while pq:
            min_val, i, j = heapq.heappop(pq)  # Pop the smallest element in the range

            # If we reach the end of a list, stop, as we can't cover all lists anymore
            if j == len(nums[i]) - 1:
                break

            # Get the next number from the same list and update 'ma'
            next_num = nums[i][j + 1]
            ma = max(ma, next_num)  # Update 'ma' with the larger value
            heapq.heappush(pq, (next_num, i, j + 1))  # Push the next number onto the priority queue

            # Update the answer if the new range is smaller
            if ma - pq[0][0] < ans[1] - ans[0] or (ma - pq[0][0] == ans[1] - ans[0] and pq[0][0] < ans[0]):
                ans = [pq[0][0], ma]

        return ans

# Example usage
sol = Solution()
print(sol.smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]))  # Output: [20,24]
