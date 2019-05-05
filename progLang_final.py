#Kareem Soliman
#CSC 11300 Afternoon
#12/20/17
#Final Exam

# 1) [32 points]
# A king has 1000 soldiers, and some of these soldiers form a circular form to play a game[1].
# In this cycle, the game starts from a certain soldier that is user defined, each soldier kills the soldier
# standing on his left. The game continues until there is only soldier is left. Write the Python3 object
# oriented code to find the soldier that survives. The number of participating soldiers (max=1000) and the
# initial position that the game starts at, are user defined.

class Josephus:
    def __init__(self, n, i):
        self.n   = n
        self.i   = i
        self.arr = []

    def __CircularForm(self, n, i):
        from collections import deque
        for k in range(i, n + 1):
            self.arr.insert(k, k)
        for j in range(1, i):
            self.arr.insert(len(self.arr) + 1, j)
        self.circle = deque(self.arr)

    def survivor(self):
        self.__CircularForm(self.n, self.i)
        while(len(self.circle) > 1):
            self.circle.rotate(-2)
            self.circle.remove(self.circle[len(self.circle) - 1])
        self.survivor = self.circle
        print("Soldier number {} is the survivor of the game".format(self.survivor[0]))

def main():

    n = int(input("Enter number of soldiers (MAX = 1000) in the game: "))
    i = int(input("Enter the soldier number (MAX = 1000) to begin the game: "))

    if (0 < n < 1001 and 0 < i < 1001):
        j = Josephus(n, i)
        j.survivor()

    else:
        print("A number entered is not within range!")
        
# 2) [32 points]
# (32 points) Suppose you have a coin and you flip it 10000 times. Write a python program to count the number
# of consecutive wins and consecutive losses. Hint: You can pick heads or tails in the beginning but since you
# need to keep track of both, wins and losses, this might not be necessary.

def Tracker(coin_face):
    import random
    MAX  = [0,0]
    win  = 0
    loss = 0
    for i in range(10000):
        choice = random.choice(['h', 't'])
        if (choice == coin_face):
            win = win + 1
            if (loss > MAX[1]):
                MAX[1] = loss
            loss = 0
        if (choice != coin_face):
            loss = loss + 1
            if (win > MAX[0]):
                MAX[0] = win
            win = 0
    if (win > MAX[0]):
        MAX[0] = win
    if (loss > MAX[1]):
        MAX[1] = loss
    print("You had a max of {} consecutive wins and a max of {} consecutive losses".format(MAX[0],MAX[1]))

def main():
    coin_face = input("Enter h or t: ")
    if (coin_face in ['h', 't']):
        Tracker(coin_face)
    else:
        print("The letter entered is not valid!")

# 3) [6 points]
# What is the purpose of the following Python3 functions? Note: One, general description for function3a and function3b is enough.

## function1) Finds repeat elements succeeding the current element, prints that repeat element, then removes the repeat element from l, which is what a[] is
## function2) Finds elements shared by s1 and s2 and appends it to l, which in turn is returned in set form
## function3a,3b) 3A prints the l and [x] then [x] and l respectively. 3B prints l in reverse order 

# 4) [20 points]
# Write a Python3 code to generate all of the subsets of a given set. Hint: Use the list data structure to represent the set, and the output subsets.

def SubsetsOf(Set):
    subsets = [{}]
    for i in Set:
        for j in subsets:
            subsets = subsets + [list(j) + [i]]
    return subsets
    
# 5) [4 points]
# Define the 4 features of the object oriented programming and explain them, use examples as we did in class.

## Encapsulation: The practice of hiding design details (variables and functions) to make a program clearer, easily defined, and prevents inintended alterations to certan variables
## Example) setValue(10){__value = 10}, a function that sets a private variable 
## Modularity: Ability to make stand-alone objects so they can be reused.
## Example) the math package, import math
## Inheritance: The ability to create new objects by inheriting characteristics of another existing class, along with additional, more class specifc functions
## Example) class car <-- class ford. ford inherits all of cars characteristics such as engine size, chasis size, etc along with ford specific functions and variables
## Polymorphism: The ability for objects to define a single function differently to appropriately serve that object
## Example) class animal/animal.move() <-- class fish/animal.move(), class frog/animal.move()... although fish and frog both inherit the move function, fish's animal.move() will print "the fish swims" and frog's animal.move() will print "the frog jumps" 

# 6) [6 points]
# Which of the python functions used for viewing the names of the functions and variables? Can we use these (hint: there are 2 of these functions)
# functions to view the names/documentation for all built-in functions? If not, why? And what can be the alternate way of viewing the documentation
# for all built-in functions?

## dir and global function is used, but not for all built in functions as python many built in functions and returns user created functions. Alternate way of viewing documantation for all built in functions is using dir(__builtins__) 

