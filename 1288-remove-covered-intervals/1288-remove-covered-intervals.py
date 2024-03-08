class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        remaining_intervals = 0
        current_rightmost = float('-inf')
        
        for interval in intervals:
            start, end = interval
            
            if end > current_rightmost:
                remaining_intervals += 1
                current_rightmost = end
        return remaining_intervals