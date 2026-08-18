class Solution(object):
    def baseNeg2(self, n, result=""):
        """
        :type n: int
        :rtype: str
        """
        if n == 0 and result == "":
            return "0"
        if n==0:
            return result
        result = str(n%2) + result
        return self.baseNeg2( (n-n%2)//-2, result)
        