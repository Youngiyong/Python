import collections
def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = list(collections.Counter(participant) - collections.Counter(completion))[0]
    return answer


print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))