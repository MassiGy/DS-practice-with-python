"""
    This is a binary search tree class
    the left son value is less then the parent value
    the parent value is less then the right son value
"""


class BinaryTree:

    def __init__(self, valeur):
        self.val = valeur
        self.right = None
        self.left = None
    

    def isLeaf(self):
        return self.left == None and self.right == None

    def insert(self,value):

        if self.val == value: return
        
        # find the sub tree in which we will insert the value

        if self.val < value :
            if(self.right == None) : self.right = BinaryTree(value)
            return self.right.insert(value)
        else:
            if(self.left == None) : self.left = BinaryTree(value)
            return self.left.insert(value)

    


    def prefix_print(self):
        """
        we print the value of the current root
        then we print the value of the left son node
        and finally we print the value of the right son node
        """

        # base case
        if self == None:
            return

        if self.isLeaf(): 
            print(self.val)
            return

        # recursive case
        print(self.val)

        if self.left != None:
            self.left.prefix_print()                

        if self.right != None:
           self.right.prefix_print()
        
        return


    def infix_print(self):
        """
        on affiche le sous arbre gauche
        puis on affiche la racine actuelle
        puis enfin, on affiche le sous arbre droit
        """

        # base case
        if self == None: 
            return

        if self.isLeaf(): 
            print(self.val)
            return


        # recursive case

        if self.left != None:
            self.left.infix_print()
        
        print(self.val)

        if self.right != None:
            self.right.infix_print()

        return



    def posfix_print(self):
        """
        on affiche le sous arbre gauche
        puis, on affiche le sous arbre droit
        enfin, on affiche la racine
        """

        # base case
        if self == None: 
            return

        if self.isLeaf(): 
            print(self.val)
            return


        # recursive case

        if self.left != None:
            self.left.posfix_print()
        

        if self.right != None:
            self.right.posfix_print()

        print(self.val)
        return



    def search(self, value, currentDepth):
        """
        search the value withing the binary tree, 
        and return the depth in with it resides
        """

        # base case
        if self == None:
            return -1

        if self.isLeaf():
            if self.val == value:
                return currentDepth
            else:
                return -1
        
        if self.val == value:
            return currentDepth

        # recursive cases:

        if value < self.val:
            # search within the left sub tree
            if self.left != None:
               return self.left.search(value, currentDepth +1)
            else :
                return -1
        
        else :
            # search within the right sub tree
            if self.right != None:
               return self.right.search(value, currentDepth+1)
            else: 
                return -1


    def bfs(self, queue):
        """
        this is a breadth first search, in with we 
        visit all the adjacent nodes to the current node
        before going one depth further
        
        """ 

        # base case
        if self == None:
            return
        
        if self.isLeaf() and self.val not in queue:
            queue.append(self.val)
            return

        # visit the current adjacent nodes ( left and right then current)
        
        if self.val not in queue:
            queue.append(self.val)

        if self.left != None:
            if self.left.val not in queue:
                queue.append(self.left.val)
        
        if self.right != None:
            if self.right.val not in queue:
                queue.append(self.right.val)



        # recursive case
        if self.left != None:
            self.left.bfs(queue)
        
        if self.right != None:
            self.right.bfs(queue)

        
        return queue


