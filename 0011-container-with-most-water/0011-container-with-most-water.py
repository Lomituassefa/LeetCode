class Solution(object):
    def maxArea(self, height):
        """
        :type : List[int]
        :rtype: int
        """
        left_Pointer = 0
        right_Pointer = len(height)-1
        max_water = 0
        while left_Pointer < right_Pointer:
            width = right_Pointer - left_Pointer
            Area = width * min(height[left_Pointer],height[right_Pointer])
            if Area> max_water:
                max_water = Area    
            if height[left_Pointer]>height[right_Pointer]:
                right_Pointer -=1
            else:
                left_Pointer +=1
        return max_water

                


        