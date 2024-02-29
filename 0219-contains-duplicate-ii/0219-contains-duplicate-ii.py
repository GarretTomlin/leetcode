class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window_start = 0
        num_frequency = {}
        
        for window_end in range(len(nums)):
            num = nums[window_end]
            if num not in num_frequency:
                num_frequency[num] = 0
            num_frequency[num] += 1
            
            if num_frequency[num] > 1:
                return True
            
            if window_end - window_start >= k:
                    num_frequency[nums[window_start]] -= 1
                    window_start +=1
        return False
            