#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for _ in range(num_products):
        name = str(sample(ADJECTIVES,1)) + ' ' + str(sample(NOUNS,1))
        prod = Product(name)
        prod.price = randint(5,100)
        prod.weight = randint(5,100)
        prod.flammability = uniform(0.0,2.5)
        products.append(prod)
    return products


def inventory_report(products):
    price, weight, flam = 0, 0, 0
    for prod in products:
        price += prod.price
        weight += prod.weight
        flam += prod.flammability
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names: ", len(products))
    print("Average price: ", price/len(products))
    print("Average weight: ", weight/len(products))
    print("Average flammability: ", flam/len(products))


if __name__ == '__main__':
    inventory_report(generate_products())
