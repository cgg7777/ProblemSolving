import sys
import re

slumpCheck = re.compile('^[DE]F+([DE]F+)*G$')
def slimpyCheck(string):
    check = False
    if len(string) <= 2:
        if len(string) == 2 and string == 'AH':
            return True
        else:
            return False

    else:
        if string[0:2] == 'AB' and string[-1] == 'C':
            check = check | slimpyCheck(string[2:-1])
        if string[0] == 'A' and string[-1] == 'C':
            check = check | bool(slumpCheck.match(string[1:-1]))

    return check


N = int(sys.stdin.readline())
strArr = []
for i in range(N):
    strArr.append(sys.stdin.readline().strip())


print("SLURPYS OUTPUT")
for sentence in strArr:
    flag = False
    for i, cha in enumerate(sentence):
        if 2 <= i <= len(sentence)-3 and slumpCheck.match(sentence[i:]) and slimpyCheck(sentence[0:i]):
            flag = True
            break

    if flag == True:
        print('YES')
    else:
        print('NO')
print('END OF OUTPUT')
