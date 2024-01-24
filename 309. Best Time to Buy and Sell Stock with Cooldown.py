class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cool_down, sell, hold = 0, 0, -float('inf')

        for price in prices:
            last_cool_down,last_sell,last_hold=cool_down,sell,hold
            cool_down=max(last_cool_down,last_sell)
            sell=hold+price
            hold=max(last_hold,last_cool_down-price)
        return max(sell,cool_down)
