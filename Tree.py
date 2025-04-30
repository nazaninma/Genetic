from collections import deque
from Node import *
from random import *
import math
import random

#.1  # control the size of tree.

class Tree:
    def __init__(self,size):
        self.root = Node('num',1)
        self.size=1
        self.depth=1
        self.fitness=float('inf')
        self.mutat_prob=0.05

        q=deque([self.root])
        while self.size<size:
            next=q.popleft() #for queue we use popleft
            if next is None:
                return
            if next.left is None and next.right is None:
                next.add_children()
                self.size+=2
                q.append(next.left)
                q.append(next.right)
                if next.right is not None:
                    if next.right.depth > self.depth :
                        self.depth= next.right.depth
                
            else:
                q.append(next.left)
                q.append(next.right)


    # eq for working ==
    def __eq__(self, other):
        #same object
        if self is other:
            return True
        else:
            return False
        
    #outputting the same number
    def __lt__(self, other):
        if self.fitness < other.fitness:
            return True
        else:
            return False
    
    def evaluate (self,x):
        return self.evaluateTree(self.root, x)


    #recursive function to calculate the final output for tree
    def evaluateTree(self,node, x):
        # empty tree
        if node is None:
            return 0
        #if divide by zero, return inf
        if node.value=='/' and node.right==0:
            print ("divided by zero")
            return float('inf')

        # leaf node
        if node.left is None and node.right is None:
            if node.value=='x':
                return float(x)

            else:
                return node.value
                # evaluate right tree
        right_sum = self.evaluateTree(node.right,x)

        # evaluate left tree
        left_sum = self.evaluateTree(node.left,x)


        if left_sum ==None or right_sum==None:
            return None

        # check which operation to apply
        if node.value == '+':
            return float(left_sum + right_sum)

        elif node.value == '-':
            return float(left_sum - right_sum)

        elif node.value == '*':
            return float(right_sum*left_sum)

        elif node.value == '**' :
            try:
                result = left_sum ** right_sum
                return float(result)
            except Exception:
                return float('inf')
        
        elif node.value == 'cos':
            if right_sum >= float('inf') or right_sum <= -float('inf'):
                return float('inf')
            return float(left_sum * math.cos(right_sum*math.pi/180 ))

        elif node.value == 'sin':
            if right_sum >= float('inf') or right_sum <= -float('inf'):
                return float('inf')
            return float(left_sum * math.sin(right_sum*math.pi/180 ))

        elif node.value == '%':
            if right_sum==0:
                return float('inf')
            else:
                return float(left_sum % right_sum)
            
    
        else:
            if right_sum!=0:
                return float(left_sum / right_sum)
            else:
                return float('inf')
            
    
    #calculate the fitness of the tree according to the mse
    def calFitness(self, data):
        sq = 0    #squared error between b=predictions and actual target
        #use each set of data points
        for r in range(len(data)):
            ans = self.evaluate(data[r][0])
            try:
                sq += (ans-data[r][1])**2
            except Exception:
                sq=float('inf')
        mse = sq/len(data)
        rmse= math.sqrt(mse)
        #Need to add size penalty
        rmse+=.1*self.size
        self.fitness = mse
        return mse
    
    #generate random path
    def generateRandomPath(self,length):
        string=''
        for i in range(length):
            bit = randint(0,1)
            string+=str(bit)
        return string

    #crossover of two subtree
    def crossover(self, other):
        #random path to chose which subtree we want to change
        # when we have 0 we go left, when we see 1 we go right
        if(self.depth==1 or other.depth==1):
            return None
        selfPath = self.generateRandomPath(randint(1,self.depth))
        otherPath = other.generateRandomPath(randint(1,other.depth))


        #Find node on first
        root1 = self.root
        parent1=root1
        direct1 ='r'
        direct2 = 'r'
        root_depth1 = 1
        for i in range(len(selfPath)):
            if selfPath[i] == '0' and root1.left:
                parent1=root1   #save parent to change its child later
                direct1='l'     #save direct to know which child should be changed
                root1 = root1.left
                root_depth1+=1
           
            elif selfPath[i]=='1' and root1.right:
                parent1=root1
                direct1='r'
                root1 = root1.right
                root_depth1+=1


        #Find node on otherPath
        root2 = other.root
        parent2=root2
        root_depth2 = 1
        for i in range(len(otherPath)):
            if otherPath[i] == '0' and root2.left:
                parent2=root2
                direct2='l'
                root2 = root2.left
                root_depth2+=1
            elif otherPath[i]=='1' and root2.right:
                parent2=root2
                direct2='r'
                root2 = root2.right
                root_depth2+=1

        #Swap places
        if direct1=='l':
            parent1.left=root2
        elif direct1=='r':
            parent1.right=root2
        else:
            print (' not crossover parent1')

        if direct2=='l':
            parent2.left=root1
        elif direct2=='r':
            parent2.right=root1
        else:
            print (' not crossover parent2')


        #Update depth and size
        other.depth=other.updateDepth(other.root)
        other.size=other.updateSize(other.root)
        self.depth = self.updateDepth(self.root)
        self.size = self.updateSize(self.root)


        return other
    

    #recursive algorithm that updates the size of a tree
    def updateSize(self, root,size=0):
        if root==None:
            return size
        return self.updateSize(root.right,size)+self.updateSize(root.left,size)
    
    #recursive algorithm that returns the depth of a tree
    def updateDepth(self,root, depth=0):
        if root == None or root.right == None or root.left == None:
            return depth
        depth+=1
        return max(self.updateDepth(root.right, depth),
        self.updateDepth(root.left,depth))
    


    def mutate(self, root):
        if random.random() < self.mutat_prob:
            # Never mutate closer to root than 2 places from depth
            # Never mutate the root
            path = self.generateRandomPath(randint(1, self.depth))
            direct = ''
            parent = None
            depth = 1
            current_node = root

            # Traverse the tree using the random path to find the node to mutate
            for i in range(len(path)):
                if path[i] == '0' and current_node.left:
                    parent = current_node
                    direct = 'l'
                    current_node = current_node.left
                    depth += 1

                elif path[i] == '1' and current_node.right:
                    parent = current_node
                    direct = 'r'
                    current_node = current_node.right
                    depth += 1

            # Once we've found the node to mutate, replace its subtree
            # new_subtree = self.generateRandomSubTree(depth)
            new_left=Tree(randint(2,5))
            new_right=Tree(randint(2,5))

            # Replace the selected node's subtree with the new randomly generated subtree
            if(parent!=None):
                parent.left=new_left.root
                parent.right=new_right.root
            
                self.size = self.updateSize(self.root)
                self.depth = self.updateDepth(self.root)

    
