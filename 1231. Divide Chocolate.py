class Solution:
    def maximizeSweetness(self, sweetness, K: int) -> int:
        """
        Problem Statement:
        You have one chocolate bar that consists of some chunks, each with its own sweetness level given by the array 'sweetness'.
        You want to share the chocolate with your K friends, so you start cutting the chocolate bar into K + 1 pieces using K cuts.
        Each piece consists of some consecutive chunks. Being generous, you will eat the piece with the minimum total sweetness
        and give the other pieces to your friends. The goal is to find the maximum total sweetness of the piece you can get
        by cutting the chocolate bar optimally.
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
