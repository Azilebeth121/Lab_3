import math

class Obj:
    def __init__(self,s):
        self.s = s
    def getString(self):
        print(self.s)
    def printSelf(self):
        print(self.s.upper())

class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
     def __init__(self,a,b):
         self.a = a
         self.b = b
     def area(self):
         return self.a * self.b
class Square(Shape):
     def __init__(self,a):
         self.a = a
     def area(self):
         return self.a * self.a

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, a, b):
        self.x = a
        self.y = b

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough")
        else:
            self.balance -= amount
            print(f"Withdraw {amount}. Left{self.balance}")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
a = Obj("dfghjk")
a.printSelf()



