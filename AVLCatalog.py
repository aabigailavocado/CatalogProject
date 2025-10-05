
from AVLNode import AVLNode

class AVLCatalog:
    def __init__(self):
        self.root = None

    def insert(self, product):
        self.root = self._insert(self.root, product)

    def _insert(self, node, product):
        if not node:
            return AVLNode(product)
        if product.id < node.product.id:
            node.left = self._insert(node.left, product)

        else:
            node.right = self._insert(node.right, product)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and product.id < node.left.product.id:
            return self.rotate_right(node)
        if balance <-1 and product.id > node.right.product.id:
            return self.rotate_left(node)
        if balance > 1 and product.id > node.left.product.id:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance <-1 and product.id < node.right.product.id:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def traverse(self):
        result = []
        self._traverse(self.root, result)
        return result

    def _traverse(self, node, result):
        if node:
            self._traverse(node.left, result)
            result.append(node.product)
            self._traverse(node.right, result)

    def search(self, product_id=None, node=None):
        if node is None:
            return None

        if product_id == node.product.id:
            return node.product
        elif product_id < node.product.id:
            return self._search(node.left, product_id)
        else:
            return self._search(node.right, product_id)

    def remove_out_of_stock(self):
        out_of_stock = []
        self._collect_out_of_stock(self.root, out_of_stock)
        for product in out_of_stock:
            self.root = self._delete(self.root, product.id)

    def _collect_out_of_stock(self, node, result):
        if node:
            self._collect_out_of_stock(node.left, result)
            if node.product.quantity == 0:
                result.append(node.product)
            self._collect_out_of_stock(node.right, result)

    def _delete(self, node, product_id):
        if not node:
            return node
        if product_id < node.product.id:
            node.left = self._delete(node.left, product_id)
        elif product_id > node.product.id:
            node.right = self._delete(node.right, product_id)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self._min_value_node(node.right)
            node.product = temp.product
            node.right = self._delete(node.right, temp.product.id)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_left(node)

        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        y.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x


