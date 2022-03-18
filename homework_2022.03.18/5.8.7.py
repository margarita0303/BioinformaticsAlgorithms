# Task 5.8.7

def LongestPathInDAGProblem(graph, start, end, preds, weights):
    longestPath = [end]
    s = [-1e9 for i in range(max(graph) + 1)]
    b = [-1e9 for i in range(max(graph) + 1)]
    s[start] = 0
    graph.remove(start)
    for vert in graph:
        for pred in preds[vert]:
            if s[pred] + weights[(pred, vert)] > s[vert]:
                b[vert] = pred
                s[vert] = s[pred] + weights[(pred, vert)]
    while longestPath[0] != start:
        longestPath = [b[longestPath[0]]] + longestPath
    return s[end], longestPath

print("Тест из примера:")
start = 0
end = 4
weights = {}
weights[(0, 1)] = 7
weights[(0, 2)] = 4
weights[(2, 3)] = 2
weights[(1, 4)] = 1
weights[(3, 4)] = 3
preds = {}
preds[1] = [0]
preds[2] = [0]
preds[3] = [2]
preds[4] = [1, 3]
graph = [0, 1, 2, 3, 4]
answer = LongestPathInDAGProblem(graph, start, end, preds, weights)
print(answer[0])
print(*answer[1])

print("Тест на датасете:")
f = open('dataset_5.8.7.txt', 'rt')
string = f.readline().rstrip().split(' ')
start = int(string[0])
end = int(string[1])
preds = {}
weights = {}
graph = []
string = f.readline().rstrip().split(' ')
while string and len(string) == 3:
    s, e, w = int(string[0]), int(string[1]), int(string[2])
    if e in preds:
        preds[e].append(s)
    else:
        preds[e] = [s]
    weights[(s, e)] = w
    graph.append(s)
    graph.append(e)
    string = f.readline().rstrip().split(' ')
graph = sorted(list(set(graph)))
answer = LongestPathInDAGProblem(graph, start, end, preds, weights)
print(answer[0])
print(*answer[1])
