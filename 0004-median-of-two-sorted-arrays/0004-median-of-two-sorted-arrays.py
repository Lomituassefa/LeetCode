class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #
        i =0
        j = 0
        result = []
        while  i < len(nums1) and j< len(nums2):
            if nums1[i]< nums2[j]:
                result.append(nums1[i])
                i+=1
            else:
                result.append(nums2[j])
                j+=1
        result.extend(nums1[i:])
        result.extend(nums2[j:])
        if len(result)%2 ==0:
            return (result[len(result)//2]+ result[len(result)//2 -1 ])/2.0
        else:
            return result[len(result)//2]

        