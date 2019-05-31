#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_nondefault_stealability_explode(self):
        """Test stealability and explode functions of non-default Products"""
        prod = Product('Test Product')
        prod.price = 20
        prod.weight = 10
        prod.flammability = 1
        self.assertEqual(prod.stealability(), "Very stealable!")
        self.assertEqual(prod.explode(), "...boom!")

class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        """Test num_products default is 30"""
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        """Test generated names in default batch for legality"""
        products = generate_products()
        for prod in products:
            self.assertIn(prod.split()[0], ADJECTIVES)
            self.assertIn(prod.split()[1], NOUNS)


if __name__ == '__main__':
    unittest.main()
