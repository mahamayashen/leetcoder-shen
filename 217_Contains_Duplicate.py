class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for ele in nums:
            dic[ele] = dic.get(ele, 0) + 1
            if dic[ele] > 1:
                return True
        return False