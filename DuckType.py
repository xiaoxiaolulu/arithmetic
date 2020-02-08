"""
Duck Typing
"""


class Person:

    @staticmethod
    def quack():
        print("quack quack I am a person but I can pretend I am a duck")

    @staticmethod
    def walk():
        print("walk walk I am a person, but I can pretend I walk like a duck")


class Duck:

    @staticmethod
    def quack():
        print("Quack, Quack, I am a duck")

    @staticmethod
    def walk():
        print("Walk Walk I am a duck")


# NON - Duck typing
def duck_test(thing):
    if isinstance(thing, Duck):
        thing.quack()
        thing.walk()


# class Duck:
#
#     @staticmethod
#     def fly():
#         print("I am a duck and I am flying")
#
#     @staticmethod
#     def quack():
#         print("Quack, Quack, I am a duck")
#
#     @staticmethod
#     def walk():
#         print("Walk Walk I am a duck")
#
#
# class Airplane:
#
#     @staticmethod
#     def fly():
#         print("I am a Airplane and I can fly")
#
#
# class Dog:
#
#     @staticmethod
#     def walk():
#         print("I am a dog and I can walk")
#
#
# for thing in Duck(), Airplane(), Dog():
#     thing.fly()  # AttributeError: 'Dog' object has no attribute 'fly'

