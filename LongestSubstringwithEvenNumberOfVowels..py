class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}  
        mask = 0  
        longest = 0  
        prefix_mask = {0: -1} 
        
        for i, char in enumerate(s):
            if char in vowels:
                mask ^= (1 << vowels[char])
    
            if mask in prefix_mask:
                longest = max(longest, i - prefix_mask[mask])
            else:
                prefix_mask[mask] = i
        
        return longest
