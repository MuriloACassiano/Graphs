from random import *

#classe generica para trabalhar com fila
#o espaço em memoria alocado cresce de acordo com o uso
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
        
#*********************************************************************
#classe que representa a lista encadeada
class leaf:
	value = None
	weight = 0
	nxt = None
	
	#função interna para adicionar uma lista no processo de criacao
	def insert(self, neo):
		if(self.nxt == None):
			self.nxt = neo
		else:
			self.nxt.insert(neo)
	
	#função interna para contagem do grau do nó
	def dg(self):
		if(self.nxt == None):
			return 1
		else:
			return 1+self.nxt.dg()
	
	#função interna para saber se um dado no possui um vertice
	def he(self, v):
		if(self.value == v ):
			return True
		elif(self.value < v):
			if(self.nxt != None):
				return self.nxt.he(v)
			else:
				return False
            
#classe para a representação de um grafo como uma lista de listas
#encadeadas
class graphy:
	main = []
	node_n = 0
	directed = False
	
	#a criação se faz com a entrada de uma matriz esparca
	def create(self, sparse, direc, num):
		sparse.sort()
		self.main = []
		self.directed = direc
		self.node_n = num
		
		for e in range(self.node_n):
			self.main.append(None)
			  
		for edge in sparse:
			#print(edge)
			aux = leaf()
			aux.value = edge[1]
			aux.weight = edge[2]
			if(self.main[ edge[0] ] == None):
				self.main[ edge[0] ] = aux
			else:
				self.main[edge[0]].insert(aux)
			if(self.directed == False):
				aux = leaf()
				aux.value = edge[0]
				aux.weight = edge[2]
				if(self.main[ edge[1] ] == None):
					self.main[ edge[1] ] = aux
				else:
					self.main[edge[1]].insert(aux)
	
	#inicia a contagem dos graus dos nos
	def degree(self):
		d=[]
		for n in self.main:
			if(n == None):
				d.append(0)
			elif(n.value != None and n.nxt == None):
				d.append(1)
			else:
				d.append(1+n.nxt.dg())
		return d
	
	#inicia a busca de um vertice u--v
	def has_edge(self, u, v):
		if(self.main[u] == None):
			return False
		elif(self.main[u].value == v):
			return True
		elif(self.main[u].value > v):
			return False
		elif(self.main[u].nxt != None):
			return self.main[u].nxt.he(v)
	
	def dist(self, r):
		D = [] 
		for j in range(self.node_n):
			D.append(self.node_n)
		D[r] = 0
		qu = QUEUE()  
		qu.put(r)
		while not qu.is_empty():     
			u = qu.pop()
			for v in range(self.node_n):
				if(self.has_edge(u, v)):
					if (D[v] == self.node_n):
						D[v] = D[u] + 1
						qu.put(v)
		return D

#função que representa o conceito de um "dado viciado"
def magic_dice(p):
	if uniform(0,1) > p:
		return False
	else:
		return True
    
def graph_generation_undirected(p,size):#(p = 0.5, size = 100):
	sparse = []
	for i in range(0,size):
		for j in range(i+1,size):
			if(magic_dice(p)):
				sparse.append([i,j,0])
	return sparse

#*******************************************************************************
#*******************************************************************************
prob = [0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.15]


print("p P")
for p in prob:
	result = []
	for mi in range(1000):
		m = graphy()
		m.create(graph_generation_undirected(p, 1000), False, 1000)
		#print(m.dist(0))
		if (m.node_n in m.dist(0)):
			result.append(0)
		else:
			result.append(1)
	print(p, result.count(1)/len(result))




