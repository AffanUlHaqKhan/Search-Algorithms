import time
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)
inf = float("INF")
ninf = -1*float("INF")
a = Node(-7)
b = Node(-10)
c = Node(-7)
a.add_child(b)
a.add_child(c)
d = Node(10)
e = Node(-10)
b.add_child(d)
b.add_child(e)
f = Node(5)
g = Node(-7)
c.add_child(f)
c.add_child(g)
h = Node(10)
i = Node(5)
j = Node(-10)
k = Node(5)
l = Node(ninf)
m = Node(-7)
d.add_child(h)
d.add_child(i)
e.add_child(j)
f.add_child(k)
f.add_child(l)
g.add_child(m)
n = Node(10)
o = Node(inf)
p = Node(5)
q = Node(-10)
r = Node(7)
s = Node(5)
t = Node(ninf)
u = Node(-7)
v = Node(-5)
h.add_child(n)
h.add_child(o)
i.add_child(p)
j.add_child(q)
k.add_child(r)
k.add_child(s)
l.add_child(t)
m.add_child(u)
m.add_child(v)

def minimax(node,depth,maximizingPlayer):
    if ((depth==0) or (len(node.children) == 0)):
        return node.data
    if (maximizingPlayer):
        bestValue = ninf
        for child in node.children:
            v = minimax(child,depth-1,False)
            bestValue = max(bestValue,v)
        return bestValue
    else:
        bestValue = inf
        for child in node.children:
            v = minimax(child,depth-1,True)
            bestValue = min(bestValue,v)
        return bestValue

start = time.clock()
print(minimax(a,4,True))
end = time.clock()

print("Time is:",end-start)
def alphabeta(node,depth,alpha,beta,maximizingPlayer):
    if ((depth==0) or (len(node.children) == 0)):
        return node.data
    if maximizingPlayer:
        v = ninf
        for child in node.children:
            v = max(v, alphabeta(child, depth-1, alpha, beta, False))
            alpha = max(alpha,v)
            if (beta<=alpha):
                break
        return v
    else:
        v = inf
        for child in node.children:
            v = min(v, alphabeta(child, depth - 1, alpha, beta, True))
            beta = min(beta,v)
            if (beta<=alpha):
                break
        return v
start = time.clock()
print(alphabeta(a,4,ninf,inf,True))
end = time.clock()

print("Time is:",end-start)