# 4.6.6

mass_table = {}
f = open('integer_mass_table.txt', 'rt')
input = f.read().split("\n")
for s in input: 
    if s == '':
        continue
    else:
        data = s.split(' ')
        mass_table[data[0]] = int(data[1])
        
def Subpeptides(string):
    subpeptides = []
    for lenOfSubPeptide in range(1, len(string)):
        currentString = string + string[0:(lenOfSubPeptide - 1)]
        for i in range(len(currentString) - lenOfSubPeptide + 1):
            subpeptides.append(currentString[i:i+lenOfSubPeptide])
    subpeptides.append("")
    subpeptides.append(string)
    return subpeptides

def Mass(peptide):
    mass = 0
    for i in peptide:
        mass += mass_table[i]
    return mass

def Cyclospectrum(peptide):
    subpeptides = Subpeptides(peptide)
    cyclospectrum = []
    for subpeptide in subpeptides:
        cyclospectrum.append(Mass(subpeptide))
    return sorted(cyclospectrum)

def ExpandPeps(peptides):
    out = []
    for i in peptides:
        aminos = "GASPVTCILNDKQEMHFRYW"
        for j in aminos:
            out.append(i + j)
    return list(set(out))

def Mass(peptide):
    mass = 0
    for i in peptide:
        mass += mass_table[i]
    return mass

def isConsistent(peptide, spectrum):
    spectPept = LinearSpectrum(peptide)
    for i in spectPept:
        if spectPept.count(i) > spectrum.count(i):
            return False
    return True

def ParentMass(spectrum):
    return spectrum[len(spectrum) - 1]

def LinearSpectrum(peptide):
    spectrum = [0]
    prefix = [0 for i in range(len(peptide) + 1)]
    for i in range(len(peptide)):
        prefix[i + 1] = prefix[i] + mass_table[peptide[i]]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            spectrum.append(prefix[j] - prefix[i])
    return sorted(spectrum)

def CyclopeptideSequencing(spectrum):
    candidatePeptides = ['']
    finalPeptides = []
    while len(candidatePeptides) > 0:
        candidatePeptides = ExpandPeps(candidatePeptides)
        current = []
        for i in range(len(candidatePeptides)):
            peptide = candidatePeptides[i]
            if Mass(peptide) == ParentMass(spectrum):
                if Cyclospectrum(peptide) == spectrum:
                    finalPeptides.append(peptide)
                current.append(peptide)
            elif not isConsistent(peptide, spectrum):
                current.append(peptide)
        for i in range(len(current)):
            candidatePeptides.remove(current[i])
    answer = []
    for peptide in finalPeptides:
        s = str(mass_table[peptide[0]])
        for i in range(1, len(peptide)):
            s += '-' + str(mass_table[peptide[i]])
        answer.append(s)
    return answer

spectrum = list(map(int, open('dataset_3.txt').readline().split()))
print(*CyclopeptideSequencing(spectrum)) 
