class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        position_counter = dict()
        total = sum(wall[0])
        
        for row in wall:
            sum_ = 0
            for i in range(len(row) - 1):
                sum_ += row[i]
                if sum_ in position_counter:
                    position_counter[sum_] += 1
                    
                else:
                    position_counter[sum_] = 1
                    
        
        max_ = 0
        
        for i in position_counter:
            if position_counter[i] > max_:
                max_ = position_counter[i]
        
        return len(wall) - max_