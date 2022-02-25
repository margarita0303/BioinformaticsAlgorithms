def MinimumSkews(genom):
    Gs = 0
    Cs = 0
    skews = []
    indexesOfMinSkews = ""
    for i in genom:
        if i == 'G':
            Gs += 1
        elif i == 'C':
            Cs += 1
        skews.append(Gs - Cs)
        
    minSkew = min(skews)
    for i in range(0, len(skews)):
        if skews[i] == minSkew:
            indexesOfMinSkews = indexesOfMinSkews + " " + str(i + 1)
            
    return indexesOfMinSkews

f = open('dataset6.txt', 'rt')
genom = f.read()
    

print("Тест из примера:")
print(MinimumSkews("TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"))
print("Тест на датасете:")
print(MinimumSkews(genom)) 
