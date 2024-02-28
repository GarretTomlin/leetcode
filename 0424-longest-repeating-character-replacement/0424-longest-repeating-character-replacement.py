class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_start, max_length, max_repeated_char = 0, 0, 0
        char_frequency = {}

        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char not in char_frequency:
                char_frequency[right_char] = 0
            char_frequency[right_char] += 1
            max_repeated_char = max(max_repeated_char, char_frequency[right_char])

            if (window_end - window_start + 1 - max_repeated_char) > k:
                left_char = s[window_start]
                char_frequency[left_char] -= 1
                window_start += 1
            max_length = max(max_length, window_end - window_start + 1)

        return max_length
