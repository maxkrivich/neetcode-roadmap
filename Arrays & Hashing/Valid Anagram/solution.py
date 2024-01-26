class Solution(object):

    def breakCount(self, s):
        res = {}
        for l in s:
            if l not in res:
                res[l] = 0
            res[l] += 1
        return res

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.breakCount(s) == self.breakCount(t)
