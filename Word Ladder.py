from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Rephrased Question:
        Given two words 'beginWord' and 'endWord', and a list of words 'wordList',
        find the length of the shortest transformation sequence from 'beginWord' to 'endWord'.
        A transformation sequence is a series of words where each word differs by only one letter
        from the previous word, and each intermediate word must be in 'wordList'.
        Return the number of words in this shortest sequence, or 0 if no such sequence exists.

        Solution with Inline Explanation:
        """
        if endWord not in wordList:
            return 0  # If the endWord is not in wordList, no transformation sequence is possible

        wordSet = set(wordList)  # Convert wordList to a set for efficient lookup
        queue = deque([(beginWord, 1)])  # BFS queue initialized with beginWord and its sequence length

        while queue:
            word, length = queue.popleft()  # Current word and the length of the transformation sequence so far
            if word == endWord:
                return length  # If endWord is reached, return the length of the sequence

            # Try transforming each letter of the word
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]  # Create a new word by changing one letter
                    if next_word in wordSet:
                        wordSet.remove(next_word)  # Remove the word from the set to prevent revisiting
                        queue.append((next_word, length + 1))  # Add the new word to the BFS queue

        return 0  # If endWord is not reached, return 0 indicating no transformation sequence is possible

# Example usage
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
sol = Solution()
print(sol.ladderLength(beginWord, endWord, wordList))  # Output will be the length of the shortest sequence or 0
