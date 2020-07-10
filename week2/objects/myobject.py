#!/usr/bin/python3

class Me():
    def __init__(self, first, last, height, weight, age):
        self.first = first
        self.last = last
        self.height = height
        self.weight = weight
        self.age = age
    # def __str__(self):

    def loose_weight(self):
        return self.weight - 5

new_me = Me("Michael", "Lennerblom", "5.6", 150, 43)

print(new_me.loose_weight())

