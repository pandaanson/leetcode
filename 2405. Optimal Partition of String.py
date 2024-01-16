class Solution:
    def partitionString(self, s: str) -> int:
        """
        Given a string 's', the task is to partition the string into the minimum number of substrings,
        ensuring that each substring contains unique characters. Each character in the string 's' must
        belong to exactly one substring in the partition. The function returns the minimum number of
        such substrings needed.
        """
        
        used = set()  # Set to store unique characters in the current substring
        ans = 1  # Initialize the count of substrings

        for char in s:
            if char in used:
                # If the character is already in the current substring, start a new substring
                used = set()
                ans += 1
            # Add the current character to the set
            used.add(char)



        return ans
