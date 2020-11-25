#! /usr/bin/env python3

graph = {'A':['B','C'],
'B':['D','E'],
'C':['F'],
'D':[],
'E':['F'],
'F':[]
}

visited = []
q = []

def bfs(visited,queue,node):
	visited.append(node)
	q.append(node)

	while q:
		s = q.pop(0)
		for i in graph[s]:
			if i not in visited :
				visited.append(i)
				q.append(i)


bfs(visited,graph,'A') 