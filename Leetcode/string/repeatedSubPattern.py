class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 1
        while i < len(s) + 1:
            subString = s[0:i]
            lenSubString = len(subString)
            if lenSubString != len(s) and subString * int(len(s) / lenSubString) == s :
                return True
            i += 1
        return False