def NumberofBreakpointsProblem(P):
    breakpoints = 0
    numbers = []
    numbers.append(0)
    n = len(P)
    for val in P:
        number = int(val[1:len(val)])
        sign = 1
        if val[0] == '-':
            sign = -1
        numbers.append(number*sign)
    numbers.append(n+1)
    for i in range(0, n+1):
        if numbers[i+1] - numbers[i] != 1:
            breakpoints += 1
    return breakpoints
    

s = "+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14"
P = s.split(' ')
print(NumberofBreakpointsProblem(P))

f = open('task2.txt', 'rt')
P = f.read().rstrip('\n').split(" ")
print(NumberofBreakpointsProblem(P))
 
