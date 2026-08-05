class node:

    def __init__(self, key = None, val = None):
        self.key = key
        self.val= val
        self.right = None
        self.left = None


class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newnode = node(key, val)
        if not self.root:
            self.root = newnode
            return

        cur = self.root
        while True:
            if key < cur.key:
                if cur.left == None:
                    cur.left = newnode
                cur = cur.left
            elif key > cur.key:
                if cur.right == None:
                    cur.right = newnode
                cur = cur.right
            else:
                cur.val = val
                return
            
    def get(self, key: int) -> int:
        cur = self.root
        while cur != None:
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return cur.val
        return -1

    def getMin(self) -> int:
        cur = self.root
        while cur and cur.left:
            cur = cur.left
        return cur.val if cur else -1

    def findmin(self, node):
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        cur = self.root
        while cur and cur.right:
            cur = cur.right
        return cur.val if cur else -1

    def remove(self, key: int) -> None: 
        self.root = self.helper(self.root, key)
    
    def helper(self, cur:node, key):
        if cur == None:
            return None
        
        if key > cur.key:
            cur.right = helper(cur.right, key)
        elif key < cur.key:
            cur.left = helper(cur.left, key)
        else:
            if cur.left == None:
                return cur.right
            elif cur.right == None:
                return cur.left
            else:
                minnode = self.findmin(cur.right)
                cur.key = minnode.key
                cur.val = minnode.val
                cur.right = self.helper(cur.right, minnode.key)
        return cur

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorder(self.root, result)
        return result

    def inorder(self, root: node, result):
        if root != None:
            self.inorder(root.left, result)
            result.append(root.key)
            self.inorder(root.right, result)

