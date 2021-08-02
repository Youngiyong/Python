import collections


# def cutoffRanks(scores, cutOffRank):
#     count = collections.Counter(scores)
#     ans, curRank = 0, 1
#     for k, v in sorted(count.items(),reverse=True):
#         if curRank > cutOffRank:
#             break
#         ans += v
#         curRank += v
#     return ans

def numPlayers(k, score):
    temp = 0
    if k<=0:
        return
    count = collections.Counter(score)
    for key, value in sorted(count.items(), reverse=True):
        if k<temp:
            break;
        else:
            temp+=value
            print(key)
    return temp


print(numPlayers(4, [2, 2, 3, 4, 5]))