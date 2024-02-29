from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_sum = sum(cardPoints)
        n = len(cardPoints)
        
        window_sum = sum(cardPoints[:n-k])
        
        max_sum = total_sum - window_sum

        for i in range(n - k, n):
            window_sum = window_sum - cardPoints[i - (n - k)] + cardPoints[i]
            max_sum = max(max_sum, total_sum - window_sum)

        return max_sum
