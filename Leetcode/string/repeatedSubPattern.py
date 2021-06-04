#Instructions: Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. 
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