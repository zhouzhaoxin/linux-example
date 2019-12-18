class Tree:
    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val


Node8 = Tree(None, None, 8)
Node7 = Tree(None, None, 7)
Node6 = Tree(None, None, 6)
Node5 = Tree(Node7, Node8, 5)
Node4 = Tree(None, None, 4)
Node3 = Tree(Node5, Node6, 3)
Node2 = Tree(Node4, None, 2)
Node1 = Tree(Node2, Node3, 1)


def traverse(node: Tree):
    q = [node]
    while q:
        n = q.pop()

        print(n.val, end=" ")

        if n.left:
            q.insert(0, n.left)
        if n.right:
            q.insert(0, n.right)
    print()


def traverse_with_println(node: Tree):
    q = [node]
    last = node
    nlast = node
    while q:
        n = q.pop()

        print(n.val, end=" ")

        if n.left:
            q.insert(0, n.left)
            nlast = n.left
        if n.right:
            q.insert(0, n.right)
            nlast = n.right

        if last == n:
            print("")
            last = nlast


def traverse_pre(node: Tree):
    if not node:
        return

    traverse_pre(node.left)
    print(node.val, end=" ")
    traverse_pre(node.right)


def serialize(node: Tree):
    q = [node]
    s = ''
    while q:
        n = q.pop()
        if n:
            s += '{}!'.format(n.val)
        else:
            s += '#!'
            continue
        q.insert(0, n.left)
        q.insert(0, n.right)
    return s


def deserialize(ss: str):
    sl = ss.split("!")[:-1]
    root_node = Tree(None, None, sl[0])
    i = 1
    q = [root_node]
    while q:
        r = q.pop()
        if not r:
            continue
        r.left = Tree(None, None, sl[i]) if sl[i] != '#' else None
        r.right = Tree(None, None, sl[i + 1]) if sl[i + 1] != '#' else None

        i += 2

        q.insert(0, r.left)
        q.insert(0, r.right)
    traverse(root_node)


traverse(Node1)
traverse_with_println(Node1)
traverse_pre(Node1)
print()
serialized = serialize(Node1)
print(serialized)
deserialize(serialized)
