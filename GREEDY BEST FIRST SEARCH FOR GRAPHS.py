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
    'Giurgiu':[{'Buhcarest':[90]}],
    'Urziceni':[{'Hirsova':[98]},{'Vaslui':[142]}],
    'Hirsova':[{'Eforie':[86]},{'Urziceni':[98]}],
    'Eforie':[{'Hirsova':[86]}],
    'Vaslui':[{'Lasi':[92]},{'Urzeceni':[142]}],
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
def GBFS(graphg,sNode,goal,priority=0,path=[]):
    q = pq()
    q.put((priority,sNode))
    while(~q.empty()):
        u = q.get()
        if(u[1] == goal):
            path.append(goal)
            return path
        else:
            for neighbour in graphg[u[1]]:
                for key in neighbour:
                    if (key not in path):
                        q.put((neighbour[key],key))
        path.append(u[1])
    return path
#print(GBFS(graph1,'A','G'))
#print(GBFS(romania,'Arad','Bucharest'))
print(GBFS(image,'150','165'))
