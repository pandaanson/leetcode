import heapq

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        """
        Problem Statement:
        You have 'n' robots, each with a specific charge time and running cost.
        The total cost of running 'k' chosen robots is calculated as the maximum charge time among these 'k' robots
        plus 'k' times the sum of their running costs.
        Given arrays 'chargeTimes' and 'runningCosts', and an integer 'budget',
        find the maximum number of consecutive robots that can be run without exceeding the budget.

        Example:
        chargeTimes = [5, 3, 10], runningCosts = [2, 1, 3], budget = 22
        The maximum number of robots that can be run without exceeding the budget is 2.
        """

        # Calculate prefix sums of running costs
        prefix = []
        total = 0
        n = len(chargeTimes)
        for i in range(n):
            total += runningCosts[i]
            prefix.append(total)

        # Initialize a max heap to store charge times and their indices
        heap = []
        heapq.heapify(heap)

        # Initialize variables for the sliding window approach
        start = 0  # Start index of the window
        max_consecutive = 0  # Maximum number of consecutive robots

        # Iterate over the array to find the optimal window size
        for i in range(n):
            # Push the current charge time and index onto the heap
            heapq.heappush(heap, (-chargeTimes[i], i))

            # Remove elements from the heap that are no longer in the window
            while len(heap) > 0 and heap[0][1] < start:
                heapq.heappop(heap)

            # Calculate the sum of running costs in the current window
            running_sum = prefix[i] - (prefix[start - 1] if start > 0 else 0)

            # Calculate the total cost for the current window
            total_cost = -heap[0][0] + (i - start + 1) * running_sum

            # If the total cost is within the budget, update the maximum window size
            if total_cost <= budget:
                max_consecutive = max(max_consecutive, i - start + 1)
            else:
                # If the budget is exceeded, move the start of the window
                start += 1

        return max_consecutive

# Example usage
# sol = Solution()
# print(sol.maximumRobots([5, 3, 10], [2, 1, 3], 22))  # Output: 2
