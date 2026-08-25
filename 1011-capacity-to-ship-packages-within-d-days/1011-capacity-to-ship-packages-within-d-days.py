class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        left = max(weights)
        right = sum(weights)
        while left<right:
            mid = left +(right-left)//2
            needed_days = 1
            current_capacity = 0
            for w in weights:
                if current_capacity + w > mid:
                    needed_days += 1
                    current_capacity = w
                else:
                    current_capacity += w
                
            if needed_days > days:
                left = mid +1
            else:
                right = mid
        return left  

        