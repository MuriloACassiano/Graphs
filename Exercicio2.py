#esta é milha classe geral quando trabalho com pilha
class QUEUE:
	sizeDefault = 2

	def __init__(self):
		self.queue = [None]*QUEUE.sizeDefault
		self.size = 0
		self.front = 0
	
	def leng(self):
		return self.size

	def is_empty(self):
		return self.leng()==0

	def malloc(self, newSIZE):
		old = self.queue
		self.queue = [None]*newSIZE
		theElementPosition = self.front
		for i in range(self.size):
			self.queue[i] = old[theElementPosition]
			theElementPosition = (1+theElementPosition) % len(old)
		self.front = 0

	def put(self, elem):
		if(self.size == len(self.queue)):
			self.malloc(2*len(self.queue))
		position = (self.front + self.size) % len(self.queue)
		self.queue[position] = elem
		self.size = self.size + 1

	def pop(self):
		if(self.is_empty()):
			return -1 
		else:
			firstElement = self.queue[self.front]
			self.queue[self.front] = None
			self.front = (self.front+1) % len(self.queue)
			self.size = self.size - 1			
			return firstElement

#grafos utilizando matriz de adjacencias (exemplo didatico)
class Graph_MA:
	node_number = 0
	edge_number = 0
	oriented = False
	matrix = []

	def __init__(self, n, e, o, m):
		self.node_number = n
		self.edge_number = e
		self.oriented = o
		self.matrix = m

	#para ver se o grafo é completo
	def is_complete(self):
		n = self.node_number
		e = self.edge_number
		if self.oriented:
			return (e == n*(n-1))
		else:
			return (e >= n*(n-1)/2)

	#para ver o grau do nó
	def degree(self, v):
		ansl = 0
		ansc = 0
		if self.oriented:
			for j in range(0,n):
				if self.matrix[v][j] != 0:
					ansl += 1
			for j in range(0,n):
				if self.matrix[j][v] != 0:
					ansc += 1
			return (ansl, ansc)
		else:
			for j in range(0,n):
				if self.matrix[v][j] != 0:
					ansl += 1
			return ansl

	#retornar os vértices adj (ou adj de saída)
	def get_adjs(self, v):
		adj = []
		for a in range(0,self.node_number):
				if self.matrix[v][a] != 0:
					adj.append(a)
		return sorted(adj)#.sort()

	#busca em profundidade (recursiva)
	def DepthFirstSearch(self, v, vis, search):
		s = search
		VISITED = vis
		VISITED[v] = True
		search.append(v)
		for w in self.get_adjs(v):
			if not VISITED[w]:
				VISITED[w] = True
				self.DepthFirstSearch(w, vis, s)
		return search

	#busca em largura (com pilha)
	def BreadthFirstSearch(self, v):
		search = []
		VISITED = []
		for i in range(0,self.node_number):
			VISITED.append(False)
		VISITED[v] = True
		Q = QUEUE()
		Q.put(v)
		search.append(v)
		while not Q.is_empty():
			a = Q.pop()
			for w in self.get_adjs(a):
				if not VISITED[w]:
					Q.put(w)
					VISITED[w] = True
					search.append(w)
		return search
		

#transformador esparça -> mtrx adj
def transform(esp, n, ori):
	(mtx, aux) = ([], [])
	for x in range(0,n):
		aux.append(0)
	for x in range(0,n):
		mtx.append(aux[:])
	if(ori):
		for edg in esp:
			mtx[edg[0]][edg[1]] = 1
	else:
		for edg in esp:
			mtx[edg[0]][edg[1]] = 1
			mtx[edg[1]][edg[0]] = 1
	return mtx

#*****************************************************************************
#matrizes esparcas do exeercício 2
gr_undi = [["A","B"],["A","C"],["A","D"],["B","C"],["B","E"],["B","G"],["C","E"],["C","F"],["D","F"],["E","F"],["E","G"],["F","H"],["G","H"],["G","J"],["H","I"],["I","J"]]
gr_dir = [["A","B"],["A","C"],["A","D"],["C","B"],["C","E"],["C","G"],["D","A"],["D","E"],["E","H"],["F","B"],["G","D"],["G","F"],["G","H"]]

dictio = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

espA = []
for elem in gr_undi:
	espA.append([dictio.index(elem[0]),dictio.index(elem[1])])
matrixA = transform(espA, 10, False)
grafoA = Graph_MA(10, len(espA), False, matrixA)

espB = []
for elem in gr_dir:
	espB.append([dictio.index(elem[0]),dictio.index(elem[1])])
matrixB = transform(espB, 8, True)
grafoB = Graph_MA(8, len(espB), True, matrixB)


visitation = []
for i in range(0,10):
	visitation.append(False)
s = []
grafoA.DepthFirstSearch(2, visitation, s)
print("A")
print("DepthFirstSearch")
print([dictio[x] for x in s])
print("BreadthFirstSearch")
print( [dictio[x] for x in grafoA.BreadthFirstSearch(2)])

visitation = []
for i in range(0,8):
	visitation.append(False)
s = []
grafoB.DepthFirstSearch(2, visitation, s)
print("B")
print("DepthFirstSearch")
print( [dictio[x] for x in s])
print("BreadthFirstSearch")
print( [dictio[x] for x in grafoB.BreadthFirstSearch(2)])


