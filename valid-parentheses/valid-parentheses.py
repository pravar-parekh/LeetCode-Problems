'''
    ****USE STACK****
    
    Params:-
        s : str
            Input Bracket String
    Returns:-
        bool
            True if valid else false.
    
    Summary:-
        Add opening brakets to stack. Pop when closing bracket encountered. Check if popped and
        closing brackets match. If not then return false. Check if stack is empty at end, if
        not then return false.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        
        if s == "":
            return True
        
        stack = []
        
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
                
            else:
                if stack == []:
                    return False
                
                popped_bracket = stack.pop()
                if i == ")" and popped_bracket != "(":
                    return False
                
                elif i == "}" and popped_bracket != "{":
                    return False
                
                elif i == "]" and popped_bracket != "[":
                    return False
                
        if stack == []:
            return True
        
        else:
            return False