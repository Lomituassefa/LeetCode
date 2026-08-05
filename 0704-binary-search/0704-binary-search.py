class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        high = len(nums)-1
        while lo <= high:
            mid_pos = (lo+high)//2
            if nums[mid_pos]==target:
                return mid_pos
            elif nums[mid_pos]< target:
                lo = mid_pos+1
            elif nums[mid_pos]>target:
                high = mid_pos -1
        return -1
        

