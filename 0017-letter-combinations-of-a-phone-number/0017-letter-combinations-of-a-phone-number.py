class Solution(object):
    def letterCombinations(self, digits):
        """

        :type digits: str
        :rtype: List[str]
        """
        restore= [""]
        phone = { "2": "abc", "3":"def", "4":"ghi", "5" : "jkl",
        "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"
        }

        for n in digits:
            sub = []
            for combinations in restore:
                for letters in phone[n]:
                    sub.append(combinations + letters)
            restore = sub
        
        return restore