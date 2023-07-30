import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
ruleArr = [[] for _ in range(N+1)]
countArr = [0 for _ in range(N+1)]
for i in range(M):
    forth, back = map(int, sys.stdin.readline().rstrip().split())
    ruleArr[forth].append(back)
    countArr[back] +=1

possibleCandidate = set()
for i in range(1, N+1):
    if countArr[i] == 0:
        possibleCandidate.add(i)

answerArr = []
while len(possibleCandidate):
    current = possibleCandidate.pop()
    answerArr.append(current)
    for back in ruleArr[current]:
        countArr[back] -= 1
        if not countArr[back]:
            possibleCandidate.add(back)

for entry in answerArr:
    print(entry, end=' ')