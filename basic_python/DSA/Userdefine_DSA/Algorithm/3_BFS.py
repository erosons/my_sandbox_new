from collections import deque,ChainMap


networkList = [ 
                ('A',['F','D']),
                ('F',['L','G']),
                ('G',['H']),
                ('L',[]),
                ('X',['ZC','W','V']),
                ('ZC',[]),
                ('W',[]),
                ('V',['U','ZZC']),
                ('U',[]),
                ('ZZC',[]),
                ('ZQ',['ZR']),
                ('ZW',['ZX']),
                ('ZX',['ZT','ZZ']),
                ('ZT',['ZN']),
                ('ZN',['ZO']),
                ('ZO',['ZR']),
                ('H',[]),
                ('D',['E']),
                ('E',['M']),
                ('M',['N','Y']),
                ('Y',['Z','X']),
                ('Z',[]),
                ('N',['P']),
                ('P',['S']),
                ('S',['ZD']),
                ('ZD',['ZE']),
                ('ZE',['ZJ','ZW']),
                ('ZJ',['ZP']),
                ('ZP',['ZQ']),
                ('ZZ',['ZZB','ZZA']),
                ('ZZB',['']),
                ('ZZA',[]),
               ]
visited = []
graph = {}
for key, value in networkList:
    graph[key]=(value)

def search__shortest_path(start, end):
    """This function is used to find the shortest path in the graph"""
    """For each node in the graph, it will check if the node is the exit path, 
       if not it will add the neighbours of node if they exist  and add the current node
        visited list and add the node to the search queue.
    """
    search_queue = deque()
    search_queue += graph[start]
    visited.append(start)
    while search_queue:
        node = search_queue.popleft()
        if node not in visited and node == end:  
            # ZR is the exit path
            print('Yes, I found the exit Node')
            visited.append(node)
            print(f'Node visted be exit NODE ->',visited)
            return
        else:
                search_queue += graph[node]
                visited.append(node)
    return False

search__shortest_path('A','ZR')
