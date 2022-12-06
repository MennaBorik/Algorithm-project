#!/usr/bin/env python
# coding: utf-8

# In[1]:


def insertionSort(arr):
 
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
 
 
arr = [60, 25, 9, 13, 91,50]
insertionSort(arr)
print(arr)


# In[10]:


def mergeArrays(nums1, nums2, m, n):
	nums3 = [None] * (m+n)
	i = 0
	j = 0
	k = 0
	while i < m:
		nums3[i]=nums1[i]
		i=i+1
	i=0
       
	while i<n:
		t=nums2[i]
		j=m-1
		while j>=0:
                   
		    if nums3[j]>t:
		        nums3[j+1]=nums3[j]
		    else:
		        break
		    j=j-1
		m=m+1
               
		nums3[j+1]=t
		i=i+1
       
	print("Array after merging")
	for i in nums3:
		print(str(i), end = " ")


nums1 = [15,17, 19, 21,23]
m = len(nums1)

nums2= [14, 16, 18, 20,22]
n = len(nums2)
#call function to merge sorted arrays
mergeArrays(nums1, nums2, m, n)


# In[11]:


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))
    def sort_edges(self):
        self.edges = sorted(self.edges, key=lambda item: item[2])
    def get_edges(self):
        return self.edges
    def number_of_vertices(self):
        return self.vertices

class DisjointSet:
    def __init__(self, size):
        self.parent = []
        self.rank = []
        for node in range(size):
            self.parent.append(node)
            self.rank.append(0)
    def find(self, v):
        if self.parent[v] == v:
            return v
        else:
            return self.find(self.parent[v])
    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        elif self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        else:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1

def kruskal(graph):
    forest = []
    graph.sort_edges()
    disjoint_set = DisjointSet(graph.number_of_vertices())
    for (u, v, weight) in graph.get_edges():
        if disjoint_set.find(u) != disjoint_set.find(v):
            forest.append((u, v, weight))
            disjoint_set.union(u, v)
    return forest

g = Graph(8)
g.add_edge(0, 1, 6)
g.add_edge(0, 2, 3)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 4)
g.add_edge(2, 3, 8)
g.add_edge(2, 4, 1)
g.add_edge(3, 4, 4)
g.add_edge(3, 6, 9)
g.add_edge(3, 7, 2)
g.add_edge(4, 5, 5)
g.add_edge(4, 7, 3)
g.add_edge(5, 6, 3)
g.add_edge(5, 7, 1)
g.add_edge(6, 7, 4)
result = kruskal(g)
for r in result:
    print(r)


# In[ ]:




