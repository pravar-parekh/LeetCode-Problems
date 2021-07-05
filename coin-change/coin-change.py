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
                
            if current_count > 0:
                upper_limit = min(upper_limit, current_count)
        
        finalCount = upper_limit if upper_limit != amount+1 else -1
        self.minCoinsReq[amount] = finalCount
        return finalCount