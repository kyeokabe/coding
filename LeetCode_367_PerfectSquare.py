class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for a in range(0,num+1):
            if a*a>num:
                return False
            if a*a==num:
                return True
