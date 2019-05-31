import unittest
import random

class Product:

    def __init__(self):
        self.name = ""
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        self.identifier = random.randint(1000000,9999999)