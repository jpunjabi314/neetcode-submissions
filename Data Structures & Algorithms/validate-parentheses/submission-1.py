class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(": ")", "[": "]", "{": "}"}

        for i in range(len(s)):
            if s[i] in pairs:
                stack.append(pairs[s[i]])
            else:                     
                if not stack:            
                    return False

                expected = stack.pop()    

                if expected != s[i]:    
                    return False
        
        return True

            


                

            

                























        """
        prev_len = -1
        while len(s) != prev_len:
            prev_len = len(s)
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
        return s == ''
        """