import sys

N = int(sys.stdin.readline())
SArr = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())
KArr = list(map(int, sys.stdin.readline().split()))
KArr = set(KArr)

answer = 0
def sol(s1 : list, s2 : list):
    global answer
    s = [0, 0, 0]
    rowflag = True
    totalflag = True
    upflag = 0

    for i, entry1 in enumerate(reversed(s2)):
        for j, entry2 in enumerate(reversed(s1)):
            multivalue = entry1 * entry2
            current = multivalue % 10 + upflag
            upflag = 0
            upflag = multivalue // 10
            if current not in KArr:
                rowflag = False
                break
            s[i] += current * pow(10, j) * pow(10, i)
        s[i] += upflag * pow(10, len(s1)) * pow(10, i)
        if (upflag and upflag not in KArr) or (rowflag is False):
            totalflag = False
            break
    if totalflag is False:
        return False


    lastS = str(sum(s))
    for num in lastS:
        if int(num) not in KArr:
            return False
    for i, num in enumerate(s):
        if(num != 0 and len(str(num)) != SArr[i+2] + i):
            return False

    answer +=1
    return True


def recursiveTest(s1 : list, s2 : list, depth : int):
    if len(s1) + len(s2) == depth:
        sol(s1,s2)
        return
    index = depth
    s2flag = False
    if depth > len(s1)-1:
        s2flag = True
        index = depth - (len(s1))

    for num in KArr:
        if s2flag == True:
            s2[index] = num
        else:
            s1[index] = num
        recursiveTest(s1[:], s2[:], depth+1)
s1 = [0] * SArr[0]
s2 = [0] * SArr[1]
recursiveTest(s1,s2,0)
print(answer)


