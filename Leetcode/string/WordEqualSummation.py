#Instructions: return whether the numerical total value of firstWord and secondWord is equal to targetWord
def isSumEqual(firstWord, secondWord, targetWord):
    """
    :type firstWord: str
    :type secondWord: str
    :type targetWord: str
    :rtype: bool
    """
    item = {'a': '0',
            'b': '1',
            'c': '2',
            'd': '3',
            'e': '4',
            'f': '5',
            'g': '6', 
            'h': '7',
            'i': '8',
            'j': '9'
            }
    listFirstWord = list(firstWord)
    listSecondWord = list(secondWord)
    listTargetWord = list(targetWord)
    valueFirstWord = []
    valueSecondWord = []
    valueTargetWord = []

    for character in listFirstWord:
        valueFirstWord.append(item[character])

    for character in listSecondWord:
        valueSecondWord.append(item[character])

    for character in listTargetWord:
        valueTargetWord.append(item[character])

    # print(valueFirstWord)
    # print(valueSecondWord)
    # print(valueTargetWord)

    numFirstWord = int(''.join(valueFirstWord))
    numSecondWord = int(''.join(valueSecondWord))
    numTargetWord = int(''.join(valueTargetWord))

    # print(numFirstWord)
    # print(numSecondWord)
    # print(numTargetWord)

    if numFirstWord + numSecondWord == numTargetWord:
        return True
    else:
        return False

print(isSumEqual('aaa', 'a', 'aab'))
