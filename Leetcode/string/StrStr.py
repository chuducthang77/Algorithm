class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if needle == '':
            return 0
        for i in range(len(haystack)):
            if i > len(haystack) - len(needle):
                return -1
            if haystack[i] == needle[0] and haystack[i:i+len(needle)] == needle:
                return i
        
        return -1