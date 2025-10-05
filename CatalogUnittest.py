import unittest

from BSTCatalog import BSTCatalog
from Product import Product
from TestCatalog import catalog


class CatalogUnittest(unittest.TestCase):
    def setUp(self):

        self.catalog = BSTCatalog()
        self.catalog.insert(Product(4, "Highlighter", 7.99, 12))
        self.catalog.insert(Product(5, "Face Wash", 21.99, 0))  # out of stock
        self.catalog.insert(Product(6, "Hair Brush", 6.99, 7))
        self.catalog.insert(Product(7, "Blush", 12.99, 3))
        self.catalog.insert(Product(1, "Sunscreen", 19.99, 10))
        self.catalog.insert(Product(2, "Eyeliner", 14.99, 10))
        self.catalog.insert(Product(3, "Lip Balm", 3.99, 8))
        self.catalog.insert(Product(8, "Moisturizer", 5.99, 0))  # out of stock

    def test_traverse(self):
        products = catalog.traverse()
        ids = [p.id for p in products]
        self.assertEqual(ids, sorted(ids))

    def test_search(self):
        product = catalog.search(2)
        self.assertIsNotNone(product)
        self.assertEqual(product.name, "Eyeliner")
        self.assertEqual(product.price, 14.99)

    def test_remove_out_of_stock(self):
        catalog.remove_out_of_stock()
        products = catalog.traverse()
        out_of_stock_ids = [5, 8]

        remaining_ids = [p.id for p in products]
        for id in out_of_stock_ids:
            self.assertNotIn(id, remaining_ids)
        self.assertEqual(len(products), 6)

if __name__ == '__main__':
    unittest.main()
