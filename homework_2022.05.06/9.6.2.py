def SuffixArray(text):
    suffixes = []
    suffix_array = []
    for i in range(len(text)):
        suffixes.append(text[i:])
        suffix_array.append(i)
    sorted_array = sorted(zip(suffixes, suffix_array), key=lambda pair: pair[0])
    suffix_array = [i for j, i in sorted_array]
    return suffix_array

if __name__ == "__main__":
    f = open('input.txt', 'r')
    text = f.read().rstrip()
    ans = SuffixArray(text)
    print(' '.join(str(i) for i in ans)) 
