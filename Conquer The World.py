#!/usr/bin/env python
# coding: utf-8


import collections

class Node:
    def __init__(self, id_):
        self.id = id_
        self.residual_flows = {}

class Minimo_costoArmy:
    INF = 250000
    
    def __init__(self, N_):
        self.N = N_
        
        self.node_table = []
        for i in range(0, self.N):
            self.node_table.append(Node(i))
            
        self.source = 0
        self.sink = N_ - 1
        
        self.max_flow = 0
        
        self.parent_links = [-1] * self.N
        
        self.main_flows = []
        
    def getMainFlows(self):
        net_flows = []
        for [u, v, c] in self.main_flows:
            net_flows.append([u, v, c, self.node_table[v].residual_flows[u]])
        return net_flows
        
    def addCapacity(self, u, v, c):
        self.node_table[u].residual_flows[v] = c
        self.node_table[v].residual_flows[u] = 0
        
        self.main_flows.append([u, v, c])
        
    def addCapacityBoth(self, u, v, c_uv, c_vu):
        self.node_table[u].residual_flows[v] = c_uv
        self.node_table[v].residual_flows[u] = c_vu
        
        self.main_flows.append([u, v, c_uv])
        self.main_flows.append([v, u, c_vu])            
            
    def bfs(self):
        visited = [False] * self.N
        
        pending = collections.deque();
        
        visited[self.source] = True
        pending.append(self.source)
        self.parent_links[self.source] = -1
        
        while len(pending) > 0:
            curr_node = pending.popleft()
            
            if curr_node == self.sink:
                return True
            
            for adj_node, res_flow in self.node_table[curr_node].residual_flows.items():
                if res_flow > 0 and not visited[adj_node]:
                    self.parent_links[adj_node] = curr_node
                    pending.append(adj_node)
                    visited[adj_node] = True
                    
        return False
    
    def findMinFlow(self):
        max_total_flow = 0
        
        while self.bfs():
            
            # encuentra el maximo flujo en el bfs path
            max_path_flow = Minimo_costoArmy.INF
            v = self.sink
            while v != self.source:
                u = self.parent_links[v]
                max_path_flow = min(max_path_flow, self.node_table[u].residual_flows[v])
                v = u
            
            # modificar los flujos residuales:
            # - elimina el flujo de los flujos residuales desde la fuente hasta el inferior
            # - agregue el flujo a los flujos residuales desde el inferior a la fuente
            
            v = self.sink
            while v != self.source:
                u = self.parent_links[v]
                self.node_table[u].residual_flows[v] -= max_path_flow
                self.node_table[v].residual_flows[u] += max_path_flow
                v = u
            
            max_total_flow += max_path_flow
            
        return max_total_flow
    

[n] = list(map(int, input().split()))
C = list(map(int, input().split()))

X = []
Y = []

for i in range(0, n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    X.append(a[1:])
    Y.append(b[1:])
    
def getXIdx(w, i):
    return sum(len(a) for a in X[:w]) + i + 1 + n*2

def getYIdx(w, i):
    return sum(len(a) for a in X) + sum(len(b) for b in Y[:w]) + i + 1 + 2*n

# total nodes = 1sink + 1source + 2*N + sum_of_sizes_X + sum_of_sizes_Y
total_nodes = 2 + 2 * n + sum(len(a) for a in X) + sum(len(b) for b in Y)

flow_network = Minimo_costoArmy(total_nodes)

for [i, c] in enumerate(C):
    flow_network.addCapacity(0, i+1, c)
    flow_network.addCapacityBoth(i+1, n+1+i, 1, 1000000)
    flow_network.addCapacity(n+1+i, total_nodes-1, 1)

for w in range(0, len(X)):
    for i in range(0, len(X[w])):
        flow_network.addCapacity(X[w][i], getXIdx(w, i), 1)
        
for w in range(0, len(Y)):
    for i in range(0, len(Y[w])):
        flow_network.addCapacity(getYIdx(w, i), n+Y[w][i], 1)
        
for w in range(0, len(X)):
    for i in range(0, len(X[w])):
        for j in range(0, len(Y[w])):
            
            flow_network.addCapacity(getXIdx(w, i), getYIdx(w, j), 1)
            
print (flow_network.findMinFlow())



