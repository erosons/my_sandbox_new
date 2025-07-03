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

def search__shortest_path_dfs(start, goal):
    search_queue = deque()
    search_queue += graph[start]
    visited.append(start)
    
    while search_queue:
        node = search_queue.popleft()
        # ZR is the exit path
        if node not in visited:
            if node == goal:  
                print('Yes, I found the exit')
                visited.append(node)
                print(f'Node visted be exit NODE ->',visited)
                return
            else:
                if node == '':
                    continue
                else:
                  deep_neighbors = graph[node]
                print(f'Node -> {node} Neighbours -> {deep_neighbors}')
                for x in deep_neighbors:
                     search_queue.appendleft(x)
                visited.append(node)
    return False

search__shortest_path_dfs('A','ZR')
