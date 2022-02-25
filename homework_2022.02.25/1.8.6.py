def HammingDistance(pattern1, pattern2):
    count = 0
    for s1, s2 in zip(pattern1, pattern2):
        if s1 != s2:
            count += 1
    return count
   

def ApproximatePatternCount(text, pattern, d):
        count = 0
        for i in range (0, len(text) - len(pattern) + 1):
            tmpPattern = text[i:i+len(pattern)]
            if HammingDistance(pattern, tmpPattern) <= d:
                count += 1
        return count
    
f = open('dataset7.txt', 'rt')
input = f.read().split("\n")
pattern = input[0]
text = input[1]
d = input[2]


print("Тест из примера:")
print(ApproximatePatternCount("TTTAGAGCCTTCAGAGG", "GAGG", 2)) 
print("Тест на датасете:")
print(ApproximatePatternCount(text, pattern, int(d))) 
