class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums, reverse = True)
        if k <= len(nums):
            self.kthlargest = self.nums[k-1]
        else:
             self.kthlargest = None
        self.k = k

    def add(self, val: int) -> int:
        if self.kthlargest == None:
            self.nums.append(val)
            self.nums = sorted(self.nums, reverse = True)
            self.kthlargest = self.nums[self.k - 1]
            return self.kthlargest
        
        elif val < self.kthlargest:
            return self.kthlargest
        
        else:
            for i in range(0, self.k):
                if val >= self.nums[i]:
                    self.nums.pop()
                    self.nums.insert(i, val)
                    break
                
            self.kthlargest = self.nums[self.k - 1]
            return self.kthlargest



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)