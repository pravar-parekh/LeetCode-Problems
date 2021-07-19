"""
    Summary:- 
        This can be done using back tracking by creating a dfs function. I have done it iteratively,
        in O(3^n). 
        
        I first created a list of mapping for the digits to letters. Then iterated through the given
        digits. For each letter that is represented by the digit, we add that letter to each combination 
        we already have found in the output.
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = [
            [""],
            [" "],
            ["a", "b", "c"], 
            ["d", "e", "f"], 
            ["g", "h", "i"], 
            ["j", "k", "l"], 
            ["m", "n", "o"],
            ["p", "q", "r", "s"],
            ["t", "u", "v"],
            ["w", "x", "y", "z"]
        ]
        
        output = [] if len(digits) == 0 else [""]
        
        for digit in digits:
            lis = mapping[int(digit)]
            newOutput = []
            for char in lis:
                for combo in output:
                    newOutput.append(combo + char)
            
            output = newOutput
            
        return output
