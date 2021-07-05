'''
    ****DP-Solution****
    
    Params:- 
        coins : List[int]
            List of available Coins
        
        amount : int
            Total amount of money
            
    Returns:-
        int
            Minimum number of coins required for that amount
            
    Summary:-
        The solution is a DP solution using memoization. We use the recursive function
        to find to minimum number of coins required for all the amounts leading upto the
        final amount. We store this in a dictionary to remove need of repeated calculation.
        The recursion logic goes like this: For each coin, if we take that coin into account,
        then the fewest number of coins we can get is 1+coinChange(amount-that_coin_value).
        So for all the coins, we return the smallest number as min(1+coinChange(amount-
        coin1_value), 1+coinChange(amount-coin2_value, ......).
        
        This can also be done using a DFS or BFS approach which should be faster and take
        less space. Something to explore.
'''
class Solution:
    def __init__(self):
        self.minCoinsReq = dict()
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0
        
        if amount in self.minCoinsReq:
            return self.minCoinsReq[amount]
        
        upper_limit = amount + 1 # This number of coins is not allowed (This is done to check)
        
        for coin in coins:
            current_count = 0
            if amount >= coin:
                previous_coin_val = self.coinChange(coins, amount - coin)
                
                if previous_coin_val >= 0:
                    current_count = previous_coin_val + 1
                    upper_limit = min(upper_limit, current_count)  
        
        finalCount = upper_limit if upper_limit != amount+1 else -1
        self.minCoinsReq[amount] = finalCount
        return finalCount
