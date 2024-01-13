"""

Given an array 'prices', where 'prices[i]' represents the price of the ith item in a shop, calculate the final prices after applying a special discount. The discount for the ith item is equal to the price of the item at the smallest index 'j' such that j > i and prices[j] <= prices[i]. If no such 'j' exists, no discount is applied to that item.

The task is to return an array 'answer', where 'answer[i]' is the final price to be paid for the ith item, after applying the special discount.

Example:
Input: prices = [8, 4, 6, 2, 3]
Output: [4, 2, 4, 2, 3]

Explanation:
- For the first item (price 8), the discount is 4 (price of the second item), so final price is 4.
- For the second item (price 4), there is no cheaper item ahead, so no discount.
- For the third item (price 6), the discount is 2 (price of the

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(prices)
        for i in range(len(prices)-1,-1,-1):
            ans[i]=prices[i]
            while stack and stack[-1]>prices[i]:
                stack.pop()
            if stack:
                ans[i]=prices[i]-stack[-1]
                
            stack.append(prices[i])
        return ans
