import sys

studentNum = int(sys.stdin.readline())
scoreArr = list(map(int, sys.stdin.readline().split()))
scoreArr.sort(reverse=True)

gradeArr = [4, 11, 23, 40, 60, 77, 89, 96, 100]
over = {}
answerArr = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i, score in enumerate(scoreArr):
    over[score] = i+1
scoreArr = list(set(scoreArr))
scoreArr.append(101)
scoreArr.sort(reverse=True)

over[101] = 0
grade = 0

for i in range(1, len(scoreArr)):
    if grade > 8:
        break
    while over[scoreArr[i-1]] >= gradeArr[grade]:
        grade += 1

    if over[scoreArr[i-1]] < gradeArr[grade]:
        answerArr[grade] = over[scoreArr[i]]
    else:
        grade += 1

for i, entry in enumerate(answerArr):
    if answerArr[i] == 0 and i > 0:
        answerArr[i] = answerArr[i-1]

acc = 0
for i in range(len(answerArr)-1):
    acc += answerArr[i]
    answerArr[i+1] -= acc

for entry in answerArr:
    print(entry)
