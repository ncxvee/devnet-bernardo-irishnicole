"""
Module 2 — Activity: Functions
Student: Irish Nicole M. Bernardo
Date: September 26, 2026

============================================
WHAT DID YOU BUILD? 
============================================

I built a Milk Tea Order System named 
"PyTEA". It shows a menu of available milk 
tea flavors and sizes. It allows the user to 
choose a flavor, size, and quantity.

The program uses functions to create the 
order and calculate the total price.

============================================
KEY VOCABULARY
============================================

Function - A function is a reusable block of
code that performs a specific task. Instead 
of rewriting code again and again, we can 
use a function whenever we need that task.

Parameter - A parameter is a variable in a
function that receives a value when the
function is called.

Argument - An argument is the actual value
of the parameter when we call the function.

Return - A return is the value that a function
gives back after performing its task. The 
difference between return and print() is that 
print() only displays something, but return 
allows the result to be stored or used 
somewhere else in the program.

============================================
YOUR SCRIPT
============================================
"""

print (" -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+- ")
print ("|         - PyTEA Menu -        |")
print (" ------------------------------- ")
print ("|  Milk Tea Flavor:             |")
print ("|  1. Chocolate                 |")
print ("|  2. Okinawa                   |")
print ("|  3. Matcha                    |")
print (" ------------------------------- ")
print ("|  Milk Tea Size:               |")
print ("|  Small  - PHP 100             |")
print ("|  Medium - PHP 120             |")
print ("|  Large  - PHP 150             |")
print (" -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+- ")

print ()
flavor = input ("Milk Tea Flavor: ")
size = input ("Milk Tea Size: ")
quantity = int (input("Quantity: "))
print ()

def create_order (flavor, size, quantity):
    if size == "Small":
        price = 100
    elif size == "Medium":
        price = 120
    elif size == "Large":
        price = 150
        
    total = price * quantity
    
    return f"{quantity} {size} {flavor} Milktea - PHP {total}"
    
order = create_order (flavor, size, quantity)
print ("ORDER:", order)

"""
============================================
A MISTAKE I MADE 
============================================

I wanted to put an else statement in my 
conditions so that when the user enters the 
wrong size, it would say "Wrong Size!". 
I used print("Wrong Size!"), but it was not 
working the way I expected, so I did not 
continue using it.

I also noticed that the other inputs will 
still accept another word or a wrong spelling. 
For example, the flavor input can accept a 
word  that is not on the menu. The quantity 
is different though because I used int(), 
so entering a string instead of a number 
causes an error.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================

This program connects to real-world ordering 
systems because coffee shops use programs to 
record customer orders, calculate prices, and 
organize information. 

My Milk Tea Order System, PyTEA, is a simple 
version of that idea. 

Functions can also be useful in other programs 
where the same task needs to be done multiple 
times, such as calculating grades, 
recording attendance, or creating a receipt.

============================================
"""