class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # Initialize two pointers
        i = 0  # Pointer for str1
        j = 0  # Pointer for str2

        # Continue until we reach the end of either string
        while i < len(str1) and j < len(str2):
            # Check three conditions:
            # 1. Characters are exactly the same
            # 2. Current character in str1 can be incremented to match str2
            # 3. Current character in str1 wraps around from 'z' to 'a'
            if (str1[i] == str2[j] or 
                ord(str1[i])+1 == ord(str2[j]) or 
                ord(str1[i])-25 == ord(str2[j])):
                # If any condition is true, move to next character in str2
                j += 1
            
            # Always move to next character in str1
            i += 1
        
        # Check if we successfully matched all characters in str2
        return j == len(str2)