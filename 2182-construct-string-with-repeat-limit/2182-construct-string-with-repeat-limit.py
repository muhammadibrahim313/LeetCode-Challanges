class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Step 1: Create a dictionary to count occurrences of each character
        d = {}
        for char in s:
            d[char] = d.get(char, 0) + 1

        # Step 2: Sort the characters in descending order
        p = sorted(d.keys(), reverse=True)  # Sorted unique characters in descending order
        
        result = []  # To store the final string
        i = 0  # Pointer to the current character in the sorted list
        
        while i < len(p):
            current_char = p[i]  # The current character we are processing
            count = min(repeatLimit, d[current_char])  # How many times we can use this character

            # Add the current character up to 'repeatLimit' times
            result.append(current_char * count)
            d[current_char] -= count  # Update the count in the dictionary

            # If there are more occurrences of the current character
            if d[current_char] > 0:
                # Find the next lexicographically smaller character (if available)
                j = i + 1
                while j < len(p) and d[p[j]] == 0:  # Skip exhausted characters
                    j += 1
                
                if j == len(p):  # No smaller character available to break the sequence
                    break

                # Add one instance of the smaller character to break the limit
                result.append(p[j])
                d[p[j]] -= 1  # Use one occurrence of the smaller character
            else:
                # Move to the next character
                i += 1

        return "".join(result)