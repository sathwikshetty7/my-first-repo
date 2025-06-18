#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# main.py

# This is a simple Python program to demonstrate Git tracking.

def greet_user(name):
    """
    Greets the user with a simple message.
    """
    print(f"Hello, {name}! Welcome to Git and GitHub training.")

def add_numbers(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b

def main():
    # Ask for user input
    name = input("Enter your name: ")
    greet_user(name)
    
    # Demonstrate a basic function
    num1 = 5
    num2 = 10
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}.")

if __name__ == "__main__":
    main()

