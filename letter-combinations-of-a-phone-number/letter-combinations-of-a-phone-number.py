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