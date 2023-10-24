from Graph import Graph



graph = Graph()

graph.addVertex(1)
graph.addVertex(2)
graph.addVertex(3)
graph.addVertex(4)

graph.constructMatrix()


graph.addReltionship(2,3)
graph.addReltionship(1,2)
graph.addReltionship(1,4)
graph.addReltionship(3,4)


graph.printGraph()




path = []

graph.findPath(2,4,path)

print(path)

