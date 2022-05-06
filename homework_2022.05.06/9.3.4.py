# 9.3.4: Trie Construction Problem

def ConstructTrie(patterns):
    trie = dict()
    trie[0] = dict()
    new_node = 1
    for pattern in patterns:
        curr_node = 0
        for pos in range(len(pattern)):
            symbol = pattern[pos]
            if symbol in trie[curr_node]:
                curr_node = trie[curr_node][symbol]
            else:
                trie[new_node] = dict()
                trie[curr_node][symbol] = new_node
                curr_node = new_node
                new_node += 1
    return trie
                    
if __name__ == "__main__":
    f = open('input.txt', 'r')
    patterns = f.read().strip().split(' ')
#     patterns = ["ATAGA", "ATC", "GAT"]
    
    trie = ConstructTrie(patterns)
    f = open('result.txt', 'w')
    for node in trie:
        for i in trie[node]:
#             print('{} {} {}'.format(node, trie[node][i], i))
            f.write('{} {} {}\n'.format(node, trie[node][i], i))
    f.close()
