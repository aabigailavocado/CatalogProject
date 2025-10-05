"""
This class represents a catalog of products in a BST tree
Basic methods: insert, search, delete, traverse

"""
from BSTNode import BSTNode


class BSTCatalog:
    def __init__(self):
        self.root = None

    def insert(self, product):
        self.root = self._insert(self.root, product)

    def _insert(self, node, product):
        if node is None:
            return BSTNode(product)
        if product.id < node.product.id:
            node.left = self._insert(node.left, product)
        else:
            node.right = self._insert(node.right, product)
        return node

    def search(self, product_id):
        return self._search(self.root, product_id)

    def _search(self, node, product_id):
        if node is None:
            return None
        if product_id == node.product.id:
            return node.product
        elif product_id < node.product.id:
            return self._search(node.left, product_id)
        else:
            return self._search(node.right, product_id)

    def traverse(self):
        result = []
        self._traverse(self.root, result)
        return result

    def _traverse(self, node, result):
        if node is not None:
            self._traverse(node.left, result)
            result.append(node.product)
            self._traverse(node.right, result)


    def delete(self, product_id):
        self.root = self._delete(self.root, product_id)

    def _delete(self, node, product_id):
        if node is None:
            return None

        if product_id < node.product.id:
            node.left = self._delete(node.left, product_id)
        elif product_id > node.product.id:
            node.right = self._delete(node.right, product_id)

        #if the node to delete is found
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            #if the node has 2 children
            else:
                successor = self._min_value_node(node.right)
                node.product = successor.product
                node.right = self._delete(node.right, successor.product.id)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left

        return current

    def remove_out_of_stock(self):
        out_of_stock_products = []
        self._collect_out_of_stock_products(self.root, out_of_stock_products,)

        if not out_of_stock_products:
            print("no out-of-stock products found")

        else:
            print("out of stock products: ")
            for product in out_of_stock_products:
                print(product)
                self.delete(product.id)

    def _collect_out_of_stock_products(self, node, out_of_stock_products):
        if node is None:
            return
        self._collect_out_of_stock_products(node.left, out_of_stock_products)

        if node.product.quantity == 0:
            out_of_stock_products.append(node.product)

        self._collect_out_of_stock_products(node.right, out_of_stock_products)







