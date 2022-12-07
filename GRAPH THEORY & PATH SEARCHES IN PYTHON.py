graph1  = {
    '1':['2','5'],
    '2':['5','3','1'],
    '3':['2','4'],
    '4':['3','5','6'],
    '5':['4','2','1'],
    '6':['4']
}
graph2  = {
    'A':['D','B','E'],
    'B':['A','D','E'],
    'C':['D'],
    'D':['A','B','C'],
    'E':['B','A']
}
graph3  = {
    '2':[],
    '3':['8','10'],
    '5':['11'],
    '7':['11','8'],
    '8':['9'],
    '9':[],
    '10':[],
    '11':['2','9']
}
def in_deg(graph):
    for i in graph:
        i_deg = 0
        for j in graph:
            if(i in graph[j]):
                i_deg = i_deg + 1
        print("In Degree of Node ",i," is ",i_deg)
        
def con_deg(graph):
    for i in graph:
        print("The Node ",i)
        print("Is connected to nodes: ")
        print(graph[i])
        print("The degree of node is: ",len(graph[i]))
#con_deg(graph3)
#in_deg(graph3)

def pathing(nodeA,nodeB,con=[]):
    con.append(nodeB)
    if(nodeB in graph1[nodeA]):
        con.append(nodeA)
        return con
    else:
        for i in graph1[nodeB]:
            a = pathing(nodeA,i,con)
            if(a):
                return con
#print(pathing('1','6'))

def find_all_paths(start, end, con=[]):
        con= con + [start]
        if start == end:
            return [con]
        all_paths = []
        for node in graph1[start]:
            if node not in con:
                a = find_all_paths(node, end, con)
                for j in a:
                    all_paths.append(j)
        return all_paths
#print(find_all_paths('1','6'))

#Lab Evalutaion Task
image = [['150','2','5'],['80','145','45'],['74','102','165']]
print(image[1][1])
im_graph = {}
for i in range(0,3):
    for j in range(0,3):
        if(i == j == 0):
            im_graph[image[i][j]] = [image[i][j+1],image[i+1][j]]
        if(i == j == 1):
            im_graph[image[i][j]] = [image[i][j-1],image[i-1][j],image[i][j+1],image[i+1][j]]
        if(i == j == 2):
            im_graph[image[i][j]] = [image[i][j-1],image[i-1][j]]
        if(i == 0 and j == 1):
            im_graph[image[i][j]] = [image[i][j-1],image[i][j+1],image[i+1][j]]
        if(i == 0 and j == 2):
            im_graph[image[i][j]] = [image[i][j-1],image[i+1][j]]
        if(i == 1 and j == 0):
            im_graph[image[i][j]] = [image[i-1][j],image[i][j+1],image[i+1][j]]
        if(i == 1 and j == 2):
            im_graph[image[i][j]] = [image[i][j-1],image[i-1][j],image[i+1][j]]
        if(i == 2 and j == 0):
            im_graph[image[i][j]] = [image[i-1][j],image[i][j+1]]
        if(i == 2 and j == 1):
            im_graph[image[i][j]] = [image[i][j-1],image[i-1][j],image[i][j+1]]
print(im_graph)
def find_all_paths_in_img(start, end, con=[]):
        con= con + [start]
        if start == end:
            return [con]
        all_paths = []
        for node in im_graph[start]:
            if node not in con:
                a = find_all_paths_in_img(node, end, con)
                for j in a:
                    all_paths.append(j)
        return all_paths
print("Paths:")
print(find_all_paths_in_img('150','165'))