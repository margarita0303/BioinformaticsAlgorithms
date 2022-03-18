# Task 5.8.5

import sys

def OutputLCS(backtrack, v, i, j):
    ans = ""
    while i > 0 and j > 0:
        if backtrack[i][j] == 1:
            i -= 1
        elif backtrack[i][j] == 2: 
            j -= 1
        else:
            i, j = i-1, j-1
            ans += v[i]
    return ans[::-1]

def LongestCommonSubsequence(s1, s2):
    len1 = len(s1) + 1
    len2 = len(s2) + 1
    backtracking = [[None] * len2 for i in range(len1)]
    s = [[0] * len2 for x in range(len1)]
    for i in range(1, len1):
        for j in range(1, len2):
            s[i][j] = max(s[i - 1][j] , s[i][j - 1])
            if s1[i - 1] == s2[j - 1]:
                s[i][j] = max(s[i][j] , s[i - 1][j - 1] + 1)     
            if s[i][j] == s[i - 1][j]:
                backtracking[i][j] = 1
            elif s[i][j] == s[i][j-1]:
                backtracking[i][j] = 2
            else:
                backtracking[i][j] = 3 
    return OutputLCS(backtracking, s1, len1 - 1, len2 - 1)

print("Тест из примера:")
print(LongestCommonSubsequence("AACCTGG", "ACACTGTGA"))

print("Тест на датасете:")
f = open('dataset_5.8.5.txt', 'rt')
input = f.read().split("\n")
s1 = input[0]
s2 = input[1]
sys.setrecursionlimit(2000)
print(LongestCommonSubsequence(s1, s2)) 
