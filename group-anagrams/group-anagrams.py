'''
Summary:- 
    First sort each string in the copied list by their letter. Once sorted, for each new string find the
    index for which output strings will be appended to. This is done by adding the sorted string as key 
    and index as its value in a dictionary. After that iterate through the original list, and for that
    same element in the sorted list, find the index, and append the original string to that index.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs2 = strs[:]
        for i in range(len(strs2)):
            strs2[i] = ''.join(sorted(strs2[i]))
        
        index = dict()
        i = 0    
        for s in strs2:
            if str(s) in index.keys():
                continue
            else:
                index[str(s)] = i
                i += 1
        
        output = [[] for l in range(i)] 

        for j in range(len(strs)):
            output[index[strs2[j]]].append(strs[j])
        
        return output