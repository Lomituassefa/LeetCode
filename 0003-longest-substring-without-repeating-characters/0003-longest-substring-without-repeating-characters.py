class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        for i in range(len(s)):
            counter = 0
            last = []
            for j in range(i, len(s)):
                if s[j] in last:
                    break
                else:
                    last.append(s[j])
                    counter+=1

            if counter> max_length:
                max_length = counter

        return max_length
