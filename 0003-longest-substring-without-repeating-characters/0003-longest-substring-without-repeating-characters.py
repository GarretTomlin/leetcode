class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window_start, max_length = 0, 0
        char_map = {}

        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in char_map:
                window_start = max(window_start, char_map[right_char]+1)
            char_map[right_char] = window_end
            max_length = max(max_length, window_end - window_start + 1)
        return max_length


        
       
                
            