class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        final = []
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        for ele in nums1:
            dic[ele] = dic.get(ele, 0) + 1
        
        for ele in nums2:
            if ele in dic and dic[ele] > 0:
                dic[ele] -= 1
                final.append(ele)
        return final
