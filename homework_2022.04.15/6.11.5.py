def ComplementOfDNA(pattern):
    reversedPattern = pattern[::-1]
    complement = ""
    for i in reversedPattern:
        if i == 'A':
            complement += 'T'
        elif i == 'T':
            complement += 'A'
        elif i == 'G':
            complement += 'C'
        elif i == 'C':
            complement += 'G'
    return complement

def SharedKMersProblem(k, s1, s2):
    shares = []
    for i in range(len(s1) - k + 1):
        positions = [(i, j) for j in range(len(s2)) if s2.startswith(s1[i: i + k], j)]
        reverse_positions = [(i, j) for j in range(len(s2)) if s2.startswith(ComplementOfDNA(s1[i: i + k]), j)]
        shares += positions
        shares += reverse_positions
    for i in shares:
        print(i)
    return

k = 3
s1 = "AAACTCATC"
s2 = "TTTCAAATC"
SharedKMersProblem(k, s1, s2)
