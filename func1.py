def f1(a):
    return 28.3495231 * a

def f2(a):
    return (5 / 9) * (a – 32)

def f3(a, b):
    for rabbits in range(a + 1):
        chickens = numheads - rabbits
        if (2 * chickens + 4 * rabbits) == b:
            return chickens, rabbits
    return None

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def f4(numbers):
    return [num for num in numbers if is_prime(num)]

from itertools import permutations

def f5(s):
    return [''.join(p) for p in permutations(s)]

def f6(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

def f7(nums):
    code = [0, 0, 7]
    index = 0
    for num in nums:
        if num == code[index]:
            index += 1
            if index == len(code):
                return True
    return False

import math

def f8(radius):
    return (4/3) * math.pi * (radius**3)

def f9(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

import random

def f10():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guesses = 0

    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break