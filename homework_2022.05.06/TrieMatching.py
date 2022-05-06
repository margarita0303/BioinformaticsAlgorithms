# Multiple Pattern Matching Problem
# Input: A string Text and a space-separated collection of strings Patterns.
# Output: All starting positions in Text where a string from Patterns appears as a substring.

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


def PrefixTrieMatching(text, pos, trie):
    suff = text[pos:]
    i = 0
    next_symbol = suff[0]
    curr_node = 0
    while True:
        if '$' in trie[curr_node]:
            return True
        elif next_symbol in trie[curr_node]:
            curr_node = trie[curr_node][next_symbol]
            if i < (len(suff) - 1):
                i += 1
                next_symbol = suff[i]
            elif not '$' in trie[curr_node]:
                return False
        else:
            return False     
    
def TrieMatching(text, patterns):
        result = []
        trie = ConstructTrie(patterns)
        for i in range(len(text)):
            if PrefixTrieMatching(text, i, trie):
                result.append(i)
        answer = []
        for pattern_ in patterns:
            pattern = pattern_[0:len(pattern_)-1]
            length = len(pattern)
            next_answer = pattern + ":"
            for i in result:
                if text[i:i+length] == pattern:
                    next_answer += (" " + str(i))
            if len(next_answer) != len(pattern + ": "):
                answer.append(next_answer)
        return answer
    
    
if __name__ == "__main__":
    f = open('input.txt', 'r')
    data = f.read().strip().split('\n')
    text = data[0]
    patterns = data[1].strip().split(' ')
    patterns = [str(pattern) + "$" for pattern in patterns]
    f.close()
    answer = TrieMatching(text, patterns)
    for i in answer:
        print(i)

    
    
 
