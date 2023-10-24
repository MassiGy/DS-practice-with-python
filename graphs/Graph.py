class Graph:

    def __init__(self):
        # create the adjacency matrix
        self.adj_matrix = []

        # create our vertecies list
        self.vertecies = []

        
    
    def addVertex(self, value:int):

        if value == None:
            return
            
        self.vertecies.append(value)
        return

  
    def constructMatrix(self):

        if self.vertecies == [] : 
            return
        
        for _ in range(len(self.vertecies)):

            list = []

            for _ in range(len(self.vertecies)):
                list.append(0)
            
            self.adj_matrix.append(list)
        
        return
    



    def printGraph(self):
       
        if self.adj_matrix == [] or self.vertecies == []:
            return
        
        print("Graph { \n")

        print("\t .vertecies: " + str(self.vertecies))

        print("\t .adjacent_matrix: \n")

        for i in range(len(self.adj_matrix)):
            print("\t\t @" + str(i+1) + "\t " + str(self.adj_matrix[i]))

        print("}\n")


    # ecrire une fonction qui va afficher notre graph dans un fichier graph.dot

    def generateMarkup(self, pathToTargetFile: str):

        if self.adj_matrix == [] or self.vertecies == []:
            return 

        # check the extention of the target file to be equal to .dot

        if pathToTargetFile.endswith(".dot") == False:
            return
        
        # open the target file
        file = open(pathToTargetFile,'w')

        # write the graph markup in the xdot standard
        file.write("digraph mygraph {\n")

        # iterate through the verticies to add the equivalent relationships

        # iterte through the adj_matrix lines which correspend to all the verticies
        for i in range(len(self.adj_matrix)):
            
            # add to the markup all the verticies even though they do not have any relations
            file.write("\t"+str(self.vertecies[i])+ ";\n")

            
            # iterate through the colomns of the selected line, which correspend to the i^th vertex relations
            for j in range(len(self.adj_matrix[i])):

               
                # add to the markup each relation for each vertex
                if self.adj_matrix[i][j] == 1: 
                    file.write("\t"+str(self.vertecies[i]) + " -> " + str(self.vertecies[j]) + ";\n")

    

        # close the markup
        file.write("}")
        # close the file, to prevent any ressource loss 
        file.close()

        return





    # add relationships
    def addReltionship(self, first:int, second:int):

        if self.adj_matrix == [] or self.vertecies == []:
            return

        """
        # not really optemized since we are traversing the list two times per vertex

        if not(self.vertecies.__contains__(first)) or not(self.vertecies.__contains__(second)):
            return

        fstIndex = self.vertecies.index(first)
        sndIndex = self.vertecies.index(second)
       
        """
        # optemized version
        fstIndex = -1
        sndIndex = -1

        try :
            fstIndex = self.vertecies.index(first)
            sndIndex = self.vertecies.index(second)

        finally:
            # flip the relationship state to a 1
            if fstIndex != -1 and sndIndex != -1:
                self.adj_matrix[fstIndex][sndIndex] = 1
            
            return
            
    




    # get relationships

    def getRelationships(self, vertex:int) -> list:

        if self.adj_matrix == [] or self.vertecies == []:
            return []
        
        # if self.vertecies.count(vertex) != 1: 
        #     return None
        
        # # traverse the matrix line which corresponds to the vertex passed as 
        # # parameter

        # index = self.vertecies.index(vertex)

        # result =  self.adj_matrix[index].copy()


        """
        # not really optemized since we are traversing the list two times per vertex
    
        """
        index = -1 
        
        try:
            index = self.vertecies.index(vertex)
       
        except:
            return []
        
       
            
        result =  self.adj_matrix[index].copy()
        return result        









    # find path
    def findPath(self, origin:int, dest:int, visitedNodes:list):
        
        if self.adj_matrix == [] or self.vertecies == []:
            return None        

        originIndex = -1
        destIndex = -1
       
        try :
            originIndex = self.vertecies.index(origin)
            destIndex = self.vertecies.index(dest)
        except:
            return None

        # from here the indecies of origin and dest are correct

        # check if the dest is already on the visitedNodes list
        if visitedNodes.count(dest) != 0:
            return None

        # put the origin on the visitedNodes list at start
        visitedNodes.append(origin)

        # get the origin relationships
        relationships = self.getRelationships(origin)

        # check if there is a direct path to the dest
        if relationships[destIndex] == 1:
            # add the dest to the visited nodes
            visitedNodes.append(dest)
            return None
        
        # check if the dest is already on the visitedNodes list
        if visitedNodes.count(dest) != 0:
            return None

        
        # otherwise, recursively call the function to search from all
        # the neighboors ( relationships )
        for rel in relationships:
           
            if rel == 1:
                newOriginIndex = relationships.index(rel)
                self.findPath(self.vertecies[newOriginIndex], dest, visitedNodes)




