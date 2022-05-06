from Classes_BaseTree_BaseTrie import BaseTree
from Classes_BaseTree_BaseTrie import BaseTrie

class Trie(BaseTrie):
    def ConstructSuffixTrieWithNoUnions(self, Text, flag):
        textLength = len(Text)
        # переберем все индексы начала всех суффиксов
        for i in range(0, textLength):
            currentNode = self.root
            # двигаемся вниз по дереву
            for j in range(i, textLength):
                symbol = Text[j]
                isNextNodeFound = False
                for edge in currentNode.edges:
                    # если имеется продолжающая путь вершина, переходим
                    if edge.label == symbol:
                        currentNode = edge.to_node
                        isNextNodeFound = True
                        break
                # если нет, создаем новую вершину и добавляем
                if not isNextNodeFound:
                    newNode = self.add_node()
                    self.add_edge(currentNode, newNode, symbol, j)
                    currentNode = newNode
            if len(currentNode.edges) == 0:
                currentNode.flag = flag
                
class Tree(BaseTree):
    def СonstructSuffixTree(self, trie_node, tree_node, path = []):
        # удлиняем путь, пока из вершин выходит только одно ребро
        while len(trie_node.edges) == 1:
            trie_edge = trie_node.edges[0]
            path.append(trie_edge)
            trie_node = trie_edge.to_node
        # добавляем накопившийся путь в наше дерево
        if len(path) != 0:
            new_tree_node = self.add_node()
            self.add_edge(tree_node, new_tree_node, path[0].position, len(path))
            tree_node = new_tree_node
        # если вершина уже лист
        if len(trie_node.edges) == 0:
            tree_node.flag = trie_node.flag
            tree_node.label = trie_node.label
            return None
        for trie_edge in trie_node.edges:
            self.СonstructSuffixTree(trie_edge.to_node, tree_node, [trie_edge])  
            
def FindPath(tree, node, Text):
    if node.label == 0:
        return ""
    currPath = ""
    currEdge = tree.all_edges[0]
    for edge in tree.all_edges:
        if edge.to_node == node:
            currEdge = edge
    previousNode = currEdge.from_node
    position = currEdge.position
    return FindPath(tree, previousNode, Text) + Text[int(position): int(position) + int(currEdge.length)]


def LongestRepeat(Text_):
    Text = Text_ + '$'
    suffixTrie = Trie()
    tree = Tree()
    suffixTrie.ConstructSuffixTrieWithNoUnions(Text, "#")
    tree.СonstructSuffixTree(suffixTrie.root, tree.root)
    maxDepth = 0
    maxDepNode = 0
    for node in tree.all_nodes:
        if len(node.edges) != 0 and node.depth > maxDepth:
            maxDepth = node.depth
            maxDepNode = node
    resultString = FindPath(tree, maxDepNode, Text)
    return resultString


if __name__ == "__main__":
    f = open('input.txt', 'r')
    Text = f.read().rstrip()
#     Text = "ATATCGTTTTATCGTT"
    print(LongestRepeat(Text))


 
