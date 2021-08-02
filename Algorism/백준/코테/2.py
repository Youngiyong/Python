

def reverseVowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']

    temp = list(s)
    temp2 = []
    idx = 0
    for i in range(len(temp)):
        for j in vowels:
            if temp[i]==j:
                temp2.append(temp[i])
    temp2.reverse()

    for i in range(len(temp)):
        for j in vowels:
            if temp[i]==j:
                temp[i]=temp2[idx]
                idx+=1



print('응?',reverseVowels("kongstudios"))