from queue import PriorityQueue as pq
graph1 = {
    'A':[{'B':[5]},{'D':[3]}],
    'B':[{'C':[5]}],
    'C':[{'A':[3]},{'D':[2]},{'E':[4]}],
    'D':[{'F':[6]},{'E':[2]}],
    'E':[{'B':[2]},{'G':[1]}],
    'F':[{'G':[9]}],
    'G':[]
}
romania = {
    'Arad':[{'Sibiu':[140]},{'Timisoara':[118]},{'Zerind':[75]}],
    'Timisoara':[{'Arad':[118]},{'Lugoj':[111]}],
    'Zerind':[{'Arad':[75]},{'Oradea':[71]}],
    'Oradea':[{'Sibiu':[151]},{'Zerind':[71]}],
    'Lugoj':[{'Mehadia':[70]},{'Timisoara':[111]}],
    'Mehadia':[{'Dobreta':[75]},{'Lugoj':[70]}],
    'Dobreta':[{'Craiova':[120]},{'Mehadia':[75]}],
    'Craiova':[{'Pitesti':[138]},{'Rimnicu Vilcea':[146]},{'Dobreta':[120]}],
    'Rimnicu Vilcea':[{'Craiova':[146]},{'Pitesti':[97]},{'Sibiu':[80]}],
    'Pitesti':[{'Bucharest':[101]},{'Craiova':[138]},{'Rimnicu Vilcea':[97]}],
    'Sibiu':[{'Arad':[140]},{'Fagaras':[99]},{'Oradea':[151]},{'Rimnicu Vilcea':[80]}],
    'Fagaras':[{'Bucharest':[211]},{'Sibiu':[99]}],
    'Bucharest':[{'Giurgiu':[90]},{'Urziceni':[85]}],
    'Giurgiu':[{'Bucharest':[90]}],
    'Urziceni':[{'Hirsova':[98]},{'Vaslui':[142]}],
    'Hirsova':[{'Eforie':[86]},{'Urziceni':[98]}],
    'Eforie':[{'Hirsova':[86]}],
    'Vaslui':[{'Lasi':[92]},{'Urziceni':[142]}],
    'Lasi':[{'Neamt':[87]},{'Vaslui':[92]}],
    'Neamt':[{'Lasi':[87]}]
}
image={
    '150':[{'2':[148]},{'80':[70]}],
    '2':[{'5':[3]},{'145':[143]},{'150':[148]}],
    '5':[{'2':[3]},{'45':[40]}],
    '80':[{'74':[6]},{'145':[65]},{'150':[70]}],
    '145':[{'2':[143]},{'45':[100]},{'80':[65]},{'102':[43]}],
    '45':[{'5':[40]},{'145':[100]},{'165':[120]}],
    '74':[{'80':[6]},{'102':[38]}],
    '102':[{'74':[38]},{'145':[43]},{'165':[63]}],
    '165':[{'45':[20]},{'102':[63]}]
}
heuristics = {
    'Arad':[366],
    'Bucharest':[0],
    'Craiova':[160],
    'Dobreta':[242],
    'Eforie':[161],
    'Fagaras':[178],
    'Giurgiu':[77],
    'Hirsova':[151],
    'Lasi':[226],
    'Lugoj':[244],
    'Mehadia':[241],
    'Neamt':[234],
    'Oradea':[380],
    'Pitesti':[98],
    'Rimnicu Vilcea':[193],
    'Sibiu':[253],
    'Timisoara':[329],
    'Urziceni':[80],
    'Vaslui':[199],
    'Zerind':[374]
}
heuristics2 ={
    '150':[4],
    '2':[3],
    '5':[2],
    '80':[3],
    '145':[2],
    '45':[1],
    '74':[2],
    '102':[1],
    '165':[0]
}
def Astar(graphg,cost,sNode,goal):
    q = pq()
    q.put((0,sNode))
    cameFrom = {sNode:[]}
    costSoFar = {sNode:[0]}
    while(q.empty() is False):

        currentNode = q.get()
        print(currentNode)
        for neighbour in graphg[currentNode[1]]:
            for key in neighbour:
                newCost = costSoFar[currentNode[1]][0] + neighbour[key][0]
                if ((key not in costSoFar) or (newCost < costSoFar[key][0])):
                    costSoFar[key] = [newCost]
                    priority = newCost + heuristics2[key][0]
                    q.put((priority,key))
                    cameFrom[key] = [currentNode[1]]

    return reconstructPath(cameFrom,sNode,goal)
def reconstructPath(cameFrom,start,goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = cameFrom[current][0]
    path.append(start)
    path.reverse()
    return path

print(Astar(romania,366,'150','165'))
