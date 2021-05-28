def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        word = s.strip().split(' ')
        if word[-1].isalpha():
            return len(word[-1])
        return counter

print(lengthOfLastWord(' a'))
print(lengthOfLastWord('a '))
print(lengthOfLastWord('Hello world'))
print(lengthOfLastWord(' a@ '))
print(lengthOfLastWord("Today is a nice day"))