class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_start, matched = 0, 0
        char_frequency = {}
        results_indices = []

        for char in p:
            if char not in char_frequency:
                char_frequency[char] = 0
            char_frequency[char] += 1

        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in char_frequency:
                char_frequency[right_char] -= 1
                if char_frequency[right_char] == 0:
                    matched += 1

            if window_end >= len(p) - 1:
                if matched == len(char_frequency):
                    results_indices.append(window_start)

                left_char = s[window_start]
                window_start += 1
                if left_char in char_frequency:
                    if char_frequency[left_char] == 0:
                        matched -= 1
                    char_frequency[left_char] += 1

        return results_indices
