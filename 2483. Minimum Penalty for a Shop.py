class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Initialize lengths, counters for 'N' and 'Y', and lists for prefix and suffix sums.
        n, cntN, cntY = len(customers), 0, 0
        prefixN, suffixY = [0], [0]
        
        # Calculate prefix sums for 'N' occurrences.
        # Loop through customers and update cntN whenever there is an 'N'.
        # Append cntN to prefixN to keep track of the number of 'N's up to the ith hour.
        for c in customers:
            cntN += (c == 'N')
            prefixN.append(cntN)
        
        # Calculate suffix sums for 'Y' occurrences.
        # Loop through customers in reverse and update cntY whenever there is a 'Y'.
        # Append cntY to suffixY to keep track of the number of 'Y's after the ith hour.
        for c in reversed(customers):
            cntY += (c == 'Y')
            suffixY.append(cntY)
        
        # Reverse suffixY so that its indices correspond to the same hours as prefixN.
        suffixY.reverse()
        
        # Find the hour to close the shop with minimum penalty.
        # Use Python's min function to find the tuple (hour, penalty), where penalty is minimum.
        # We use enumerate to also get the index, which represents the hour.
        best_hour, _ = min(enumerate(a + b for a, b in zip(prefixN, suffixY)), key=lambda x: x[1])
        
        # Return the best hour to close the shop to minimize the penalty.
        return best_hour
