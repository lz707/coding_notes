# if each element is not necessarily unique
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_nums = dict(zip(nums, range(len(nums))))
        nums1 = [target - num for num in nums]
        for i in range(len(nums1)):
            idx2 = idx_nums.get(nums1[i])
            if idx2 != None and i!=idx2:
                return i, idx2
            
# if each element is unique and return count of pairs only
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = set([target - num for num in nums])
        nums1 = set(nums)
        return len(nums2&nums1)
