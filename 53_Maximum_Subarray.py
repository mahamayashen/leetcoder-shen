class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        best_sum = nums[0]
        sums = [nums[0]] #list
        
        for i in range(1, len(nums)):
            sums.append(max(sums[i-1] + + nums[i], nums[i]))
            best_sum = max(best_sum, sums[i])
        
        return best_sum