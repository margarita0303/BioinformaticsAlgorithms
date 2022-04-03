# 4.2.7

table = {}
f = open('RNA_codon_table_1.txt', 'rt')
input = f.read().split("\n")
for s in input: 
    if s == '':
        continue
    else:
        data = s.split(' ')
        table[data[0]] = data[1]

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

        
def ComplementOfDNAList(patterns):
    compPatterns = []
    for pattern in reversed(patterns):
        compPatterns.append(ComplementOfDNA(pattern))
    return compPatterns

def TranscribeString(pattern):
    transcribed = ""
    for i in pattern:
        if i == 'T':
            transcribed = transcribed + 'U'
        else:
            transcribed = transcribed + i
    return transcribed
    
def Codons(DNA):
    codons = []
    for i in range(len(DNA) // 3):
        index = i * 3
        newString = DNA[index] + DNA[index + 1] + DNA[index + 2]
        codons.append(newString)
    return codons

def Aminos(codons):
    aminos = []
    for codon in codons:
        trCodon = TranscribeString(codon)
        aminos.append(table[trCodon])
    return aminos

answers = []

DNA = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
geneticCode = "MA"

#f = open('dataset_4.2.7.txt', 'rt')
#input = f.read().split("\n")
#DNA = input[0]
#geneticCode = input[1]

codons = Codons(DNA)
aminos = Aminos(codons)
for i in range(len(aminos) - len(geneticCode) + 1):
    if aminos[i:i+len(geneticCode)] == list(geneticCode):
        answers.append(codons[i:i+len(geneticCode)])
        
codons = Codons(DNA[1:len(DNA)])
aminos = Aminos(codons)
for i in range(len(aminos) - len(geneticCode) + 1):
    if aminos[i:i+len(geneticCode)] == list(geneticCode):
        answers.append(codons[i:i+len(geneticCode)])
        
codons = Codons(DNA[2:len(DNA)])
aminos = Aminos(codons)
for i in range(len(aminos) - len(geneticCode) + 1):
    if aminos[i:i+len(geneticCode)] == list(geneticCode):
        answers.append(codons[i:i+len(geneticCode)])
        
compDNA = ComplementOfDNA(DNA)

codons = Codons(compDNA)
aminos = Aminos(codons)
for i in range(len(aminos) - len(geneticCode) + 1):
    if aminos[i:i+len(geneticCode)] == list(geneticCode):
        answers.append(ComplementOfDNAList(codons[i:i+len(geneticCode)]))
        
codons = Codons(compDNA[1:len(compDNA)])
aminos = Aminos(codons)
for i in range(len(aminos) - len(geneticCode) + 1):
    if aminos[i:i+len(geneticCode)] == list(geneticCode):
        answers.append(ComplementOfDNAList(codons[i:i+len(geneticCode)]))
        
codons = Codons(compDNA[2:len(compDNA)])
aminos = Aminos(codons)
for i in range(len(aminos) - len(geneticCode) + 1):
    if aminos[i:i+len(geneticCode)] == list(geneticCode):
        answers.append(ComplementOfDNAList(codons[i:i+len(geneticCode)]))
        
answersAsStrings = []
for ans in answers:
    s = ""
    for codon in ans:
        s = s + str(codon)
    answersAsStrings.append(s)
    
for i in answersAsStrings:
    print(i)
 
