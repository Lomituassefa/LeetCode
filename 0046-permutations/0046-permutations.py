class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        visited = [False] * len(nums)
        def backtrack(curr):
            if len(curr) == len(nums):
                result.append(list(curr)) 
                return
            
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True      
                    curr.append(nums[i])
                    backtrack(curr)        
                    curr.pop()             
                    visited[i] = False
        backtrack([]) 
        return result