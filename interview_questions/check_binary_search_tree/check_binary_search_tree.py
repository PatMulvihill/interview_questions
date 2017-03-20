# Question taken from: https://www.hackerrank.com/challenges/ctci-is-binary-search-tree

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def __lt__(self, other):
        return self.data < other.data
        
    def __gt__(self, other):
        return self.data > other.data
"""

def check_binary_search_tree_(pnode):
    if pnode == None:
        return True
        
    if pnode.left and pnode.left.data >= pnode.data:
        return False
    
    if pnode.right and pnode.right.data <= pnode.data:
        return False
        
    
    return check_binary_search_tree_(pnode.right) and check_binary_search_tree_(pnode.left)
    
    
# L1: 4 10 15 7  20 49
# L2: 3 19 5  7  20 49

len(L1)

L1[difference] L1.next.next.next.etc

// This is the text editor interface. 
// Anything you type or change here will be seen by the other person in real time.


// linked list
// L1 - node(12), node(35) 67 9 29 45 11
// L2 - 97 52 45 11 

def check_intersection(L1, L2):
    L1_len = len(L1)
    L2_len = len(L2)
    if L1_len > L2_len:
        larger = L1
        smaller = L2
        difference = L1_len - L2_len
    elif L2_len > L1_len:
        larger = L2
        smaller = L1
        difference = L2_len - L1_len
    else:
        larger = L1
        smaller = L2
        difference = 0
        
    for i in range(0, len(larger)):
        if larger[i + difference] == smaller[i]:
            return smaller[i]
            
    return None