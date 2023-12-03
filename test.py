#Answer: 507214
def test1():
    input = open("Day 3/testcase.txt")
    sum = 0
    inputLines = input.readlines()
    for i in range(0, len(inputLines)):
        j = 0
        while (j < len(inputLines[i])):
            if (inputLines[i][j].isdigit()):
                tempstart = j
                check1 = False
                check2 = False
                check3 = False
                while (j < len(inputLines[i]) and inputLines[i][j].isdigit()):
                    j += 1
                if (tempstart > 0):
                    tempstart -= 1
                    check1 = True
                if (j < len(inputLines[i])):
                    j += 1
                    check2 = True
                if (i-1 >= 0):
                    for s in inputLines[i-1][tempstart:j]:
                        if (not s.isdigit() and s != "."):
                            check3 = True
                            break
                if (i+1 < len(inputLines)):
                    for s in inputLines[i+1][tempstart:j]:
                        if (not s.isdigit() and s != "."):
                            check3 = True
                            break
                if (check1 and inputLines[i][tempstart] != "." and not inputLines[i][tempstart].isdigit()):
                    check3 = True
                if (check2 and inputLines[i][j-1] != "." and not inputLines[i][j-1].isdigit()):
                    check3 = True
                if (check3):
                    if (check1):
                        tempstart += 1
                    if (check2):
                        j -= 1
                    sum += int(inputLines[i][tempstart:j])
            j += 1
    j = 0
    print(sum)
test1()