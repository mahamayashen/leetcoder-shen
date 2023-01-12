class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_n = len(nums)
        sums = []
        for i in range(len_n - 1):
            for j in range(i + 1, len_n):
                base_sum = nums[i] + nums[j]
                if base_sum == target:
                    return[i, j]
                else:
                    j += 1