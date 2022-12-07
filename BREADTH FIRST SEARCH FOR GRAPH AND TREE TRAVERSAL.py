import time
class Node:
       def __init__(self,data):
           self.data = data
           self.children = []
class Queue:
    def __init__(self):
        self.q = []
    def enqueue(self,value):
        self.q.insert(0,value)
    def dequeue(self):
        return self.q.pop()
    def queuelength(self):
        return len(self.q)
fringe = Queue()
graph1  = {
    '1':['2','5'],
    '2':['5','3','1'],
    '3':['2','4'],
    '4':['3','5','6'],
    '5':['4','2','1'],
    '6':['4']
}
graph2  = {
    'A':['B','D','E'],
    'B':['A','D','E'],
    'C':['D'],
    'D':['A','B','C'],
    'E':['A','B']
}
def bfs(graph, start, end):
    q = Queue()
    q.enqueue([start])
    while (q.queuelength() != 0):
        path = q.dequeue()
        node = path[-1]
        if node == end:
            return path
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            q.enqueue(new_path)
print (bfs(graph1, '6', '1'))
print (bfs(graph2, 'C', 'E'))

image = {
    '150':['2','80','145'],
    '2':['150','80','145','45','5'],
    '5':['2','145','45'],
    '80':['150','2','145','74','102'],
    '145':['150','2','5','80','45','74','102','165'],
    '45':['5','2','145','102','165'],
    '74':['80','145','102'],
    '102':['74','80','145','45','165'],
    '165':['102','145','45']
}
start_time = time.clock()
for i in image.keys():
    if(i != '5'):
        
        print (bfs(image, '5', str(i)))
print('Execution Time: ',time.clock()-start_time)