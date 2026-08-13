# run cmd
# python3 index.py

# Data Engineering
# Python 30-Day Roadmap
#
# Day 1-2: Python setup, IDE, Hello World, variables, data types
# Day 3-4: Input/output, basic operators, string manipulation
# Day 5-6: Lists, tuples, sets, dictionaries
# Day 7-8: Conditional statements (if, elif, else)
# Day 9-10: Loops (for, while), break, continue
# Day 11-12: Functions, arguments, return values
# Day 13-14: Scope, lambda, map, filter, reduce
# Day 15-16: Modules, packages, pip, virtual environments
# Day 17-18: File handling (read/write), exceptions
# Day 19-20: List comprehensions, dictionary comprehensions
# Day 21-22: Classes, objects, OOP basics
# Day 23-24: Inheritance, polymorphism, encapsulation
# Day 25-26: Standard libraries (os, sys, datetime, random)
# Day 27: Working with APIs (requests), JSON
# Day 28: Basic data visualization (matplotlib)
# Day 29: Simple project (calculator, to-do app, etc.)
# Day 30: Review, practice, explore next steps (web, data science, automation)

# access specifiers and modifiers

# check Leadcode to solve python questions
print("Hello kamal")

import sys

print("Python version of the editor:", sys.version)


#Python v.0.0.9 relese Feb 20 1991
# python uses below
# Automation (read, write, insert)
# Seduling
# Data processing (data validation, data testing, etc..)
# software development (web)
# Input/output things

# 1.procejerals
# 2.oops (concepts)
# 3.Functions
# Methods

# frameworks (flask, numwork, etc...)
# opensource -> pip install flask

# high level language -> programming languages (python, java, c,etc..)
# lowlevel language -> computer languages ( 0, 1)

# compiler
# source code (high level) --> compiler --> machine code (low level)

#python
# source code (high level) (I/P) --> compiler (compiler time) (o/p) --> inter mediate code (byte code)(i/p) --> pvm (run time)
# machine code (low level)
# Input program, output program,
#pvm (python virtual machine) --> platform indipentant (read byte code to send machine code)

# pycham or vscode use community edition opensource

# check file compiler code below
# /Volumes/work/kamal/python  --> python3 hello.py
# python -m py_compile hello.py

# PEP -> Python Enhancement Proposal (Style guide for python code writing conventions and best practices)
# indentation (4 spaces)
# variable_name = "Kamal"  # snake_case
# ClassName = "Kamal"      # PascalCase
# CONSTANT_NAME = "Kamal"  # UPPER_SNAKE_CASE

# type Casting
# inputs
# code comments
# code comments are ignored by the interpreter
# string handling or manipulation


# Instance (object) =>  calss and static method

# Higher order functions (HOF) is a function that either takes one or more functions as arguments or returns a function as its result. HOFs are a fundamental concept in functional programming and are widely used in Python.  Used to make code mote flexible and reusable, and dynamic. They allow you to abstract away common patterns of computation and create more concise and expressive code.

# Example of a higher-order function that takes another function as an argument:
def apply_function(func, value):
    return func(value)

# impure and pure function
# lamda Function
# closure
# partial applied function
# Composed Function
# callback Function
# recursive function
# generator function
# test Case
# scheduling (automation is different dont confuse)
# 1. cron or (while loop)
# 2. Airflow use (Docker or windows subsystem for linux) wsl --install
# 3. ETL Python(Airflow), (wrapper.sh, etl-script.py, python-dag.py) using pandas
# 4.Streamlit

# Streamlit is python library to create web apps for data projects without needing HTML, Css or Javascript. it truns your python scripts into interactive web apps just by running a script.
# python -m streamlit run python/streamlit_app.py
# What can you build streanlit?
# Data dashboard, Ml model apps (PDF chat), Image/Video tools, Chatbots, resume Analyzers, SQL explorers

# tkinter is the standard GUI (Graphical User Interface) Library for pythin. It lets you build windows, buttons, labels, text boxes and more - just like apps with a user interface. (Eg windows calculator app, timer)
    # 1. Built-in with python (no need to install separately)
    # 2. Good for building simple desktop applications
    # 3. Cross-platform (works on windows, macOS, Linux)

# what is matplotlib?
# matplotlib is a library in python used to create static, animated and interactive plots.
# The main module: pyplot - provides fuctions to make plots just like MATLAB.

# last video time: 10:12