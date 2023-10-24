from BinaryTree import BinaryTree 

root = BinaryTree(4)

root.insert(3)
root.insert(5)
root.insert(7)
root.insert(2)

root.infix_print()

print("\n\n")

print(root.bfs([]))









"""
                    4
            3               5
        2                           7


BFS: 3,5,4,2,7
     4,3,5,2,7
DFS: 2,3,4,5,7
postfix: 2,3,7,5,4
"""
