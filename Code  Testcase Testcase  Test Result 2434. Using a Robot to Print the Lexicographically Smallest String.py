#Rephrased Question:
#Create a method in a class called Solution that transforms a given string s. This method, rearrangeString, should process the string to produce a new string in which characters are rearranged according to specific rules. The rearrangement should be done by comparing each character in s with the lexicographically smallest suffix character for each position in s, and then selectively moving characters to form a new string.
class Solution:
    def robotWithString(self, s: str) -> str:

        # Determine the length of the string
        length = len(s)

        # Initialize a list to keep track of the smallest suffix character from each position in the string
        smallest_suffix = [s[-1]] * length

        # Update the smallest_suffix list so that each position contains the minimum character
        # from the current position to the end of the string
        for i in range(length - 2, -1, -1):
            smallest_suffix[i] = min(s[i], smallest_suffix[i + 1])

        # Temporary storage to help in rearranging characters
        temp_storage = []
        # List to accumulate the rearranged characters to form the result string
        result = []

        # Iterate through each character in the string
        for i, character in enumerate(s):
            # Append current character to temporary storage
            temp_storage.append(character)
            # Check and move characters from temp_storage to result based on their
            # lexicographical order compared to the next character in the smallest_suffix
            while i + 1 < length and temp_storage and smallest_suffix[i + 1] >= temp_storage[-1]:
                result.append(temp_storage.pop())

        # Append remaining characters from temp_storage to result in reverse order
        result.extend(reversed(temp_storage))

        # Return the joined result as a string
        return ''.join(result)
