def longestChain(words):
    maxLength = 0
    minLength = 1
    mintemp = []
    for word in words:
        if len(word) <= minLength:
            mintemp.append(word)

    print(mintemp)
    for word in words:
        if len(word) > minLength:
            for test in mintemp:
                if word.find(test)!=-1 and maxLength < len(word):
                    print('what?', word)
                    print('maxLength', maxLength)
                    maxLength = len(word)

    print(maxLength)
                # if word:
                #     print(3)
                #     maxLength = len(word)
    return maxLength
if __name__ == "__main__":
    w = [ "a",  "b",  "ba", "bca", "bda", "bdca" ]
    print(longestChain(w))
    w = [ "bdcafg", "bdcaf", "a",  "b",  "ba", "bca", "bda", "bdca" ]
    print(longestChain(w))
