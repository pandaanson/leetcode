from collections import deque
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # Transform costs into a queue
        cost_queue = deque(costs)

        # Create a priority queue to keep all candidates
        pq = []
        
        # Strings for total cost, and counters for front and back
        total_cost = 0
        front_counter, back_counter = 0, 0
        
        # Variables for last taken index from front and back
        latest_front = -1
        latest_back = len(costs)

        # Populate the priority queue with candidates from front and back
        while cost_queue and front_counter < candidates:
            # Pop from front
            front_cost = cost_queue.popleft()
            heapq.heappush(pq, (front_cost, latest_front + 1))
            latest_front += 1
            front_counter += 1

        while cost_queue and back_counter < candidates:
            # Pop from back
            back_cost = cost_queue.pop()
            heapq.heappush(pq, (back_cost, latest_back - 1))
            latest_back -= 1
            back_counter += 1

        # Run k sessions to hire workers
        for _ in range(k):
            # Pop the smallest cost worker
            min_cost, index = heapq.heappop(pq)
            total_cost += min_cost  # Add the cost to total

            # Determine if the worker is from the front or back
            if index <= latest_front and cost_queue:
                # Pop front to the priority queue
                front_cost = cost_queue.popleft()
                heapq.heappush(pq, (front_cost, latest_front + 1))
                latest_front += 1
            elif index >= latest_back and cost_queue:
                # Pop back to the priority queue
                back_cost = cost_queue.pop()
                heapq.heappush(pq, (back_cost, latest_back - 1))
                latest_back -= 1

        return total_cost
