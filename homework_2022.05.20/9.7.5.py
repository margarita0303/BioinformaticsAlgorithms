def BurrowsWheeler(text):
    rotations = sorted([text[i:] + text[:i] for i in range(len(text))])
    return ''.join([rot[-1] for rot in rotations])


if __name__ == "__main__":
    f = open('input.txt', 'r')
    data = f.read().strip().split('\n')
    text = data[0]

    print(BurrowsWheeler(text)) 
