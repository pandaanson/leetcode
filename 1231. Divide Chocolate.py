class Solution:
    def maximizeSweetness(self, sweetness, K: int) -> int:
        """
        Problem Statement:
        clarify the problem with an example. The goal is to cut a chocolate bar, represented as an array of chunks with varying levels of sweetness, into k + 1 pieces such that:

Each piece consists of one or more consecutive chunks.
You will eat the piece with the least total sweetness (being generous to your friends).
The aim is to maximize the sweetness of the piece you eat, under the constraint that it must have the least sweetness among all pieces.
Let's consider an example to illustrate this:

Example:

Suppose the sweetness levels of the chocolate chunks are given by the array sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9].
You want to share the chocolate with k = 2 friends (meaning you need to make k + 1 = 3 pieces in total).
Goal:

Find the way to cut the chocolate such that the piece you choose for yourself has the maximum possible sweetness, but is still the least sweet among the three pieces.
Approach:

One way to cut the chocolate is into [1, 2, 3, 4], [5, 6], and [7, 8, 9]. The total sweetness of these pieces are 10, 11, and 24, respectively. If you choose the first piece [1, 2, 3, 4], your piece's sweetness is 10.
Another way could be [1, 2, 3], [4, 5, 6], and [7, 8, 9]. The total sweetness of these pieces are 6, 15, and 24, respectively. Here, you would choose the first piece [1, 2, 3], with sweetness 6.
Optimal Solution:

The goal is to maximize the sweetness of your piece while ensuring it's the least sweet. In the examples above, the first way of cutting gives you a piece with sweetness 10, which is higher than 6 in the second method. Thus, the first method is better in this scenario.
The problem asks to find the optimal way of cutting to achieve the maximum sweetness for your piece, under these constraints.
In summary, the problem is about balancing the generosity of giving sweeter pieces to friends while still maximizing the sweetness of the piece you get, within the given constraints.
        """

        # Initialize binary search bounds
        low = 1  # Minimum possible sweetness per piece
        high = sum(sweetness) // (K + 1)  # Maximum possible average sweetness per piece

        while low < high:
            # Calculate the mid-point of the current search range
            mid = (low + high + 1) // 2

            # Initialize variables to count the number of cuts and track the current chunk sweetness
            cuts = 0
            chunk_sweetness = 0

            # Iterate through the chunks to determine the number of cuts needed for the current sweetness target (mid)
            for piece in sweetness:
                chunk_sweetness += piece
                # If the current chunk sweetness reaches or exceeds the target, make a cut
                if chunk_sweetness >= mid:
                    cuts += 1
                    chunk_sweetness = 0

            # Adjust binary search bounds based on the number of cuts
            if cuts > K:  # If more cuts than needed, increase the target sweetness
                low = mid
            else:  # If fewer or equal cuts, decrease the target sweetness
                high = mid - 1

        # Return the maximum possible sweetness you can achieve for your piece
        return low
