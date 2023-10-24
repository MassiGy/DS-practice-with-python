from Node import Node

def array2LinkedList(array): 
    res = LinkedList(array[0])

    for i in range(1,len(array)): 
        res.append(array[i])
    
    return res



class LinkedList:

    def __init__(self, data=None):
        # head of the list
        self.head = Node(data)
        # tail of the list
        self.tail = self.head

    


    # add to the tail of the list
    def append(self, data=None):
        # append to the end
        self.tail.next = Node(data)
        # shift the tail by one
        self.tail = self.tail.next
        
    # append to the end using an iterative approach
    def append_iterative(self, data=None):

        traversal = self.head

        # get to the end of the list
        while traversal.next != None:
            traversal = traversal.next

        # set the last element
        traversal.next = Node(data)

        # shift the tail by 1
        self.tail = traversal.next


    

    def search(self, data=None):
        
        # init the traversal to the head
        traversal = self.head

        # init a res boolean
        found = False

        while traversal != None and not(found) :
            if traversal.data == data:
                found = True
            
            # step ahead
            traversal = traversal.next
    
        return found

    
    def length(self):
        # init the traversal to the head
        traversal = self.head

        # init the res to 1
        res = 1

        while traversal.next != None:
            res+=1
            traversal = traversal.next


        return res 


    # for the recusive version, this wont work, since 
    # head is only availible at first.
    # def length_rec(self):
    #     if(self == None): return 0
    #     return 1 + self.head.length_rec()



    def get(self, index=-1):
        # if index is set to default return the tail data
        if index == -1 or index < 0 :
            return self.tail.data
        
        # check index < length
        if index >= self.length():
            return None
        

        # traverse the list up until the el at index = to the given index
        traversal = self.head
        # index counter
        counter = 0

        while traversal.next != None and counter < index:
            counter+=1
            traversal = traversal.next

        return traversal.data


    # splice
    def splice(self, start_index, el_count):

        # check if the start index is valid
        if start_index >= self.length() or start_index < 0:
            return
        
        # check if the el_count is also valid
        if el_count <= 0: 
            return

        # check that the removing process is also possible
        if start_index + el_count >= self.length():
            return



        # set the current index at the head
        current_index = 0
        # set a traversal node to walktrough the list
        traversal = self.head

        while traversal != None and current_index < start_index:
            traversal = traversal.next
            current_index+=1


        # traversal is set to the element with an index = start index
        counter = 0
        temp = traversal

        while counter <= el_count:
            temp = temp.next
            counter+=1
        
        # temp is now at a distence of +el_count forward then traversal

        traversal.next = temp


        






    
    

    
    # insert

    def insert(self, index,data=None):

        if data == None:
            return

        if index >= self.length():
            # add to the end
            self.tail.next = Node(data)
            # shift the tail by one pos
            self.tail = self.tail.next
            return
        

        if index <= 0:
            # add to the begining
            element = Node(data)
            element.next = self.head

            # shift the head by one pos backwards
            self.head = element
            return
        

        # init a traversal
        traversal = self.head
        #init a counter
        current_index = 0

        while traversal != None and current_index < index - 1:
            traversal = traversal.next
            current_index+=1
        
        # save the rest of the list
        rest = traversal.next

        # now traversal.next is on the specified index
        traversal.next = Node(data)

        # make the newely inserted element attached to the rest of the list
        traversal.next.next = rest


  
    # slice
    def slice(self, start_index, el_count):

        # check if the start index is valid
        if start_index >= self.length() or start_index < 0:
            return
        
        # check if the el_count is also valid
        if el_count <= 0: 
            return

        # check that the removing process is also possible
        if start_index + el_count >= self.length():
            return

        # set the current index at the head
        current_index = 0
        # set a traversal node to walktrough the list
        traversal = self.head

        while traversal != None and current_index < start_index:
            traversal = traversal.next
            current_index+=1

        
        # create the result lis
        res = LinkedList(traversal.data)

        # init a counter
        counter = 0

        while traversal != None and counter < el_count:
            
            traversal = traversal.next
    
            res.append(traversal.data)

            counter+=1



        return res



    # bubble sort
    # O(N²)
   
    def bubbleSort(self):
        traversal = self.head
        changeFlag = True

        while changeFlag and traversal.next != None:
           
            secondTraversal = self.head

            changeFlag = False
           
            while secondTraversal.next != None:
                if secondTraversal.data > secondTraversal.next.data : 
                    temp = secondTraversal.data
                    secondTraversal.data = secondTraversal.next.data
                    secondTraversal.next.data = temp
                    # trigger the flag
                    changeFlag = True
                
                secondTraversal = secondTraversal.next
        
            traversal = traversal.next



        
     




    # optimized version
    # O(N²) >> O(N * M ) where M > 0 and M < N
    def bubbleSort_optimized(self):

        traversal = self.head
        changeFlag = True

        while changeFlag and traversal.next != None:
           
            secondTraversal = self.head

            changeFlag = False
           
            while secondTraversal.next != None:
                if secondTraversal.data > secondTraversal.next.data : 
                    temp = secondTraversal.data
                    secondTraversal.data = secondTraversal.next.data
                    secondTraversal.next.data = temp
                    # trigger the flag
                    changeFlag = True
                
                secondTraversal = secondTraversal.next
        
            traversal = traversal.next




    # create helper methods to swap our linkedList to a regular list
    # and vice-versa

    def linkedList2array(self):

        traversal = self.head

        res = []

        while traversal != None:
            res.append(traversal.data)
           
            traversal = traversal.next


        return res

    

    # selection sort
    def selectionSort(self):
        # si la list est vide ou composé d'un seul element, on fait rien
        if self.head == None or self.head == self.tail:
            return self
        
        # si non
        # on transforme la liste vers un tableau
        array = self.linkedList2array()

        # puis on tri le tableau

        for i in range(len(array)):
           
            # initialiser les coordonée du max
            max = array[0]
            indexMax = 0

            # trouver le max du sous tableau courant
            for j in range(len(array) - i):
                if array[j] > max:
                    max = array[j]
                    indexMax = j
            
            # echanger le max et le dernier element du tableau courant
            temp = array[len(array) -i -1]
            array[len(array) -i -1] = max
            array[indexMax] = temp


        # puis on retransforme vers une liste
        return array2LinkedList(array)




    # insertion sort
    def insertionSort(self):
        # quand elle continent moin de deux element
        if self.head == None or self.head == self.tail:
            return self

        # si non

        # on va transfomer notre liste vers un tableau
        array = self.linkedList2array()

        # trier notre tableau, par insertion
        sub_array_last_element_index = 0


        for i in range(len(array)):
            
            # si un element est plus petit que le dernier element de notre sous tableau trié
            # on l'insere dans celui ci
            if array[i] <= array[sub_array_last_element_index]:

                for j in range(sub_array_last_element_index + 1):

                   if array[j] > array[i]:
                        # on les echange
                        temp = array[j]
                        array[j] = array[i]
                        array[i] = temp 
            
            sub_array_last_element_index+=1
            
        


        # on retournera une liste à partir de la version triée du tableau
        return array2LinkedList(array)



    # write the list to a file

    def writeToFile(self, filename):
        
        if self.head == None or filename == None:
            return
        
        # si non
        file = open(filename, 'w')

        traversal = self.head

        while traversal != None:
            # ecrire la valeur dans le fichier
            # en format csv
            file.write(str(traversal.data) + ",")

            # faire avencer le traversal
            traversal = traversal.next

        file.close()







    # read a list from a file





    # binary insertion sort

  
  
  
  
  
  

        






    def log(self):
        # set the traversal to the start
        traversal = self.head

        # init the res string
        res = "[ "


        # walktrough the list and print each item
        while traversal != None:
            res += str(traversal.data) + " -> "
            traversal = traversal.next
        
        # end the string
        res += " None ]"

        print(res)


