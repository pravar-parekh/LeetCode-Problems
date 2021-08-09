class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = dict()
        
        for num in nums:
            if num not in count:
                count[num] = 1
                
            else:
                count[num] += 1
                
        keys = list(count.keys())
        count = list(count.values())
        print(count)
        ans = []
        
        for i in range(k):
            index = count.index(max(count))
            ans.append(keys[index])
            
            count.pop(index)
            keys.pop(index)
        
        return ans