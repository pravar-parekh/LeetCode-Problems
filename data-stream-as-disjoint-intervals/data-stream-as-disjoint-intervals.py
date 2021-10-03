class SummaryRanges:

    def __init__(self):
        self.arr = [0 for i in range(10000)]

    def addNum(self, val: int) -> None:
        self.arr[val] += 1

    def getIntervals(self) -> List[List[int]]:
        ans = []
        
        start = 0
        end = 0
        counting_started_flag = 0
        for i in range(10000):
            
            if self.arr[i] == 0:
                if counting_started_flag == 1:
                    counting_started_flag = 0
                    ans.append([start, end])
                    
            else:
                if counting_started_flag == 1:
                    end = i
                
                else:
                    counting_started_flag = 1
                    start = i
                    end = i
        
        if counting_started_flag == 1:
            ans.append([start,end])
        
        return ans
                


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()