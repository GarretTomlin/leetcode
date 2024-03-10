class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        subset.append([])
        
        for currentNum in nums:
            n = len(subset)
            
            for i in range(n):
                set =  list(subset[i])
                set.append(currentNum)
                subset.append(set)
        return subset
        