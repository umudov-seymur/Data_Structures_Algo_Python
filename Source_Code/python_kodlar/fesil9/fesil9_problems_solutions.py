from queue import Queue

class Node:
    def __init__(self, data):
        # root node
        self.data = data
        # Sol övlad(left child)
        self.left = None
        # Sağ övlad(right child)
        self.right = None

    def get_data(self):
        return self.data

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right


class BinaryTreeExercises:

    def __init__(self):
        self.root = None
        self.max_data = 0.0

    def create_tree(self, val):
        # Ağacın özünü burda yaradırıq.
        if self.root is None:
            # Birinci elementi root element edirik
            self.root = Node(data=val)

        else:
            # Root-u hazırkı node edirik
            current = self.root

            while True:
                # Əgər verilmiş qiymət hal-hazırkı qiymətdən kiçikdirsə,
                # Onu sol node edirik
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(data=val)
                        break;
                # Əgər verilmiş qiymət hal-hazırkı qiymətdən böyükdürsə,
                # Onu sağ node edirik
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(data=val)
                else:
                    break

    def find_max_recursive(self, node):
        if not node:
            return self.max_data

        if node.get_data() > self.max_data:
            self.max_data = node.get_data()

        self.find_max_recursive(node.left)
        self.find_max_recursive(node.right)

        return self.max_data

    def find_max_level_order_traversal(self, node):
        if node is not None:
            q = Queue()
            q.put(node) # root node-u daxil edirik.

            while not q.empty():
                node = q.get() # Dequeue FIFO
                # növbədən çıxartdıqdan sonra müqayisə edirik.
                if node.get_data() > self.max_data:
                    self.max_data = node.get_data()

                if node.left is not None:
                    q.put(node.left)

                if node.right is not None:
                    q.put(node.right)

        return self.max_data

    def find_data_recursive(self, node, data):
        if node is None:
            return 0

        if node.get_data() == data:
            return 1
        elif data < node.get_data():
            return self.find_data_recursive(node.left, data)
        else:
            return self.find_data_recursive(node.right, data)

    def find_data_level_order_traversal(self, node, data):
        if node is not None:
            q = Queue()
            q.put(node) # root node-u daxil edirik.

            while not q.empty():
                node = q.get() # Dequeue FIFO
                # növbədən çıxartdıqdan sonra yoxlayırıq.
                if node.get_data() == data:
                    return 1
                if node.left is not None:
                    q.put(node.left)

                if node.right is not None:
                    q.put(node.right)
        # 0 qayıdırsa, deməli data Ağacda yoxdur.
        return 0

    def insert_in_binary_using_tree_level_order(self, node, data):
        new_node = Node(data)
        if node is None:
            node = new_node # Ağac boşdursa, yeni node-u root node edirik.
            return node

        q = Queue()
        q.put(node) # Root node-u növbəyə daxil edirik.

        while not q.empty():
            node = q.get() # Dequeue FIFO
            # növbədən çıxartdıqdan sonra yoxlayırıq.
            if node.get_data() == data:
                return "Already in tree"
            if node.left is not None:
                q.put(node.left)
            else:
                # Əgər hal-hazırkı node-un datasından kiçikdirsə
                if new_node.get_data() < node.get_data():
                    node.left = new_node
                    return "Inserted as left node"

            if node.right is not None:
                q.put(node.right)
            else:
                # Əgər hal-hazırkı node-un datasından böyükdürsə
                if new_node.get_data() > node.get_data():
                    node.right = new_node
                    return "Inserted as right node"

    def find_tree_size_recursive(self, node):
        if node is None:
            return 0

        return self.find_tree_size_recursive(node.left) + self.find_tree_size_recursive(node.right) + 1

    def find_tree_size_iterative(self, node):
        if node is None:
            return 0

        q = Queue()
        q.put(node) # Root node-u növbəyə daxil edirik.
        count = 0

        while not q.empty():
            node = q.get()
            count = count + 1
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)

        return count

    def level_order_traversal_in_reverse(self, node):
        if node is None:
            return 0
        
        q = Queue()
        s = [] # LIFO üçün istifadə edəcəyimiz list
        q.put(node) # root node-u daxil edirik.

        while not q.empty():
            node = q.get() # Dequeue FIFO
            s.append(node.get_data()) # LIFO

            if node.left is not None:
                q.put(node.left)

            if node.right is not None:
                q.put(node.right)
        
        while(s):
            print(s.pop(), end=' ')


if __name__ == "__main__":
    tree = BinaryTreeExercises()
    arr = [8, 3, 1, 6, 4, 7, 10, 14, 13]
    for i in arr:
        tree.create_tree(i)
    print("find_max_recursive() -> ", end='')
    print(tree.find_max_recursive(tree.root))
    print("find_max_level_order_traversal() -> ", end='')
    print(tree.find_max_level_order_traversal(tree.root))
    print("find_data_recursive() search 88 -> ", end='')
    print(tree.find_data_recursive(tree.root, 88))
    print("find_data_recursive() search 14 -> ", end='')
    print(tree.find_data_recursive(tree.root, 14))
    print("find_data_level_order_traversal() search 88 -> ", end='')
    print(tree.find_data_level_order_traversal(tree.root, 88))
    print("find_data_level_order_traversal() search 14 -> ", end='')
    print(tree.find_data_level_order_traversal(tree.root, 14))
    print("insert_in_binary_using_tree_level_order(tree.root, 21) -> ", end='')
    print(tree.insert_in_binary_using_tree_level_order(tree.root, 21))
    print("find_tree_size_recursive() -> ", end='')
    print(tree.find_tree_size_recursive(tree.root))
    print("find_tree_size_iterative() -> ", end='')
    print(tree.find_tree_size_iterative(tree.root))
    print("level_order_traversal_in_reverse() -> ", end='')
    tree.level_order_traversal_in_reverse(tree.root)
