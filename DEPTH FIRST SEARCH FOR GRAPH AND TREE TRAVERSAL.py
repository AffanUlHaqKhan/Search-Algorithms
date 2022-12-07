class stack:
    def __init__(self):
        self.s = []
    def push(self,value):
        self.s.append(value)
    def pop(self):
        return self.s.pop()
    def queuelength(self):
        return len(self.s)
graph1  = {
    '1':['2','5'],
    '2':['1','5','3'],
    '3':['2','4'],
    '4':['3','5','6'],
    '5':['1','2','4'],
    '6':['4']
}
graph2  = {
    'A':['B','D','E'],
    'B':['A','D','E'],
    'C':['D'],
    'D':['A','B','C'],
    'E':['A','B']
}
def dfs_recursive(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs_recursive(graph,n, visited)
    return visited
visited = dfs_recursive(graph1,'6', [])
print(visited)

def dfs_iter(graph, start, path=[]):
    q=[start]
    while q:
        v = q.pop()
        if v not in path:
            path += [v]
            q += graph[v]
    return path
#print(dfs_iter(graph2,'A'))
tree1={
    '1':['2','3'],
    '2':['4','5'],
    '3':[],
    '4':['6'],
    '5':['7','8'],
    '6':[],
    '7':[],
    '8':[]
}
print(dfs_recursive(tree1,'1',[]))

image={
    '150':['2','80'],
    '2':['5','145','150'],
    '5':['2','45'],
    '80':['74','145','150'],
    '145':['2','45','80','102'],
    '45':['5','145','165'],
    '74':['80','102'],
    '102':['74','145','165'],
    '165':['45','102']
}
print(dfs_recursive(image,'150',[]))