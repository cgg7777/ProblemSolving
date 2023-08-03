import sys

N = int(sys.stdin.readline())
answer = sys.stdin.readline().rstrip()
candidate = []

listedAnswer = list(answer)
# N 300 / 간판 길이 25
for i in range(N):
    candidate.append(sys.stdin.readline().rstrip())
answer  = 0
def findPattern(sign, targetIndex, currentIndex, blank):
    answer = 0
    if targetIndex == len(listedAnswer):
        return 1

    for i in range(currentIndex, len(sign)):
        if sign[i] == listedAnswer[targetIndex]:
            if targetIndex == 0:
                answer += findPattern(sign, targetIndex+1, i+1, 0)
            elif targetIndex == 1:
                answer += findPattern(sign, targetIndex + 1, i + 1, i -currentIndex)
            elif blank == i - currentIndex:
                answer += findPattern(sign, targetIndex+1, i+1, i -currentIndex)
    return answer

answerCount = 0
for i in range(N):
    if findPattern(candidate[i], 0, 0, 0):
        answerCount +=1
print(answerCount)


