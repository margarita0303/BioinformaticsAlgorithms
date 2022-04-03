# 4.4.4

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

peptide = "IAQMLFYCKVATN"
subpeptides = Subpeptides(peptide)

#f = open('dataset_4.4.4.txt', 'rt')
#peptide = f.read().split("\n")[0]
#subpeptides = Subpeptides(peptide)

cyclospectrum = []
for subpeptide in subpeptides:
    cyclospectrum.append(Mass(subpeptide))
    
print(*sorted(cyclospectrum)) 
