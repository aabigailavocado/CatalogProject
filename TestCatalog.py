"""
This is a test class for the Catalog classes
"""
import time
from random import random

from AVLCatalog import AVLCatalog
from BSTCatalog import BSTCatalog
from Product import Product

catalog = BSTCatalog()
catalog.insert(Product(1, "Sunscreen", 19.99, 10))
catalog.insert(Product(2, "Eyeliner", 14.99, 10))
catalog.insert(Product(3, "Lip Balm", 3.99, 8))
catalog.insert(Product(4, "Highlighter", 7.99, 12))
catalog.insert(Product(5, "Face Wash", 21.99, 0)) #out of stock
catalog.insert(Product(6, "Hair Brush", 6.99, 7))
catalog.insert(Product(7, "Blush", 12.99, 3))
catalog.insert(Product(8, "Moisturizer", 5.99, 0)) #out of stock


print("\nSorted Product List: ")
for product in catalog.traverse():
    print(product)
result = catalog.search(2)
print("\nSearch Result for product ID #2: ", result)

#tst to remove out of stock products
print("\n")
print("Before Removal of Out of Stock Products, the Catalog has: ")

for product in catalog.traverse():
    print(product)
print("\n")

catalog.remove_out_of_stock()
print("\n")
print("After Removal of Out of Stock Products, the Remaining Products are: ")

for product in catalog.traverse():
    print(product)


def compare_bst_avl_search():
    product_ids = list(range(1, 10001))
    random.shuffle(product_ids)
    products = [Product(id, f"Product {id}", random.randint(1, 100), random.randint(1, 100)) for id in product_ids]
    search_products = random.sample(product_ids, 1000)

    bst_catalog = BSTCatalog()
    avl_catalog = AVLCatalog()

    for product in products:
        bst_catalog.insert(product)
        avl_catalog.insert(product)

    start = time.time()
    for product_id in search_products:
        bst_catalog.search(product_id)
    bst_time = time.time() - start

    start = time.time()
    for product_id in search_products:
        avl_catalog.search(product_id)
    avl_time = time.time() - start

    print(f"BST Search Time: {bst_time:.2f} seconds")
    print(f"AVL Search Time: {avl_time:.2f} seconds")

if __name__ == '__main__':
    compare_bst_avl_search()
