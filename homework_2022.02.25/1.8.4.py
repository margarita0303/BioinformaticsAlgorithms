def HammingDistance(pattern1, pattern2):
    count = 0
    for s1, s2 in zip(pattern1, pattern2):
        if s1 != s2:
            count += 1
    return count

def ApproximatePatternMatching(text, pattern, d):
        ans = ""
        for i in range (0, len(text) - len(pattern) + 1):
            tmpPattern = text[i:i+len(pattern)]
            if HammingDistance(pattern, tmpPattern) <= d:
                ans = ans + " " + str(i)
        return ans
    
f = open('dataset8.txt', 'rt')
input = f.read().split("\n")
pattern = input[0]
text = input[1]
d = input[2]

print("Тест из примера:")
print(ApproximatePatternMatching("CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT", "ATTCTGGA", 3)) 
print("Тест на датасете:")
print(ApproximatePatternMatching(text, pattern, int(d))) 
