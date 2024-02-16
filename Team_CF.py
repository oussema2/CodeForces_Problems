n = int(input())
res = 0
for i in range(n):
    s = str(input())
    arrS = s.split(" ")
    solutionNumber = 0
    for i in range(len(arrS)):
        if(arrS[i] == "1"):
            solutionNumber+=1
    if(solutionNumber>1):
        res+=1
print(res)