'''
    Summary:-
        In a group of K adjacent empty seats between two people, the answer is (K+1) / 2.


        For each group of K empty seats between two people, we can take into account the
        candidate answer (K+1) / 2.

        For groups of empty seats between the edge of the row and one other person, the answer 
        is K, and we should take into account those answers too.
'''
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        ans = seats.index(1) #First index of 1
        seats.reverse()
        ans = max(ans, seats.index(1)) #First indext of 1 after reversing. Cause end could 
                                       #be zeroes too
        
        count = 0
        longest = 0
        for i in range(len(seats)):
            if seats[i] == 0:
                count += 1
                longest = max(count, longest)
            else:
                count = 0
            
        ans = max(ans, (longest + 1)/2 )
        return int(ans)
        
        