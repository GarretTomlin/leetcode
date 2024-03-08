class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        end = intervals[0][1]
        min_remove = 0

        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]

            if current_start < end:
                min_remove += 1
            else:
                end = current_end

        return min_remove
