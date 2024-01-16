from collections import Counter

class Solution:
    def largestPalindromic(self, num: str) -> str:
        """
        Given a string 'num' consisting only of digits, return the largest palindromic integer
        (as a string) that can be formed using the digits from 'num'. The resulting palindromic
        integer should not have leading zeroes. It's allowed to reorder the digits and not use
        all of them, but at least one digit must be used.
        """

        # Count the frequency of each digit in 'num'
        count = Counter(num)

        # Initialize strings for the palindrome's middle part and half part
        palindrome_half, middle_part = '', ''

        # Iterate over the digits in descending order
        for digit in sorted(count.keys(), reverse=True):
            # Determine the middle part: the largest digit that occurs an odd number of times
            middle_part = max(middle_part, digit * (count[digit] & 1))
            
            # Append half the count of the digit to the palindrome_half
            palindrome_half += digit * (count[digit] // 2)

        # Remove leading zeros from the palindrome_half
        palindrome_half = palindrome_half.lstrip('0')

        # Form the palindrome and return it, or return '0' if it's empty
        return (palindrome_half + middle_part + palindrome_half[::-1]) or '0'
