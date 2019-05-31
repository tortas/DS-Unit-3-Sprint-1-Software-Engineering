#!/usr/bin/env python

import unittest
import random

class Product:

    def __init__(self, name):
        self.name = name
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        self.identifier = random.randint(1000000,9999999)

    def stealability(self):
        ratio = self.price / self.weight
        if ratio < 0.5:
            return 'Not so stealable...'
        elif 0.5 <= ratio < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        x = self.flammability * self.weight
        if x < 10:
            return '...fizzle.'
        elif 10 <= x < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'

class BoxingGlove(Product):
    
    def __init__(self, name):
        super().__init__(name)
        self.weight = 10

    def explode(self):
        return "...it's a glove"
    
    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        elif 5 <= self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
