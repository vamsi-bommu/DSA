Recursion: When a function calls itself until a specified condition is met

Every recursive function must have:

✅ 1. Base Case :The stopping condition that prevents infinite recursion.

✅ 2. Recursive Case :The function calls itself with a smaller/simpler input.

def factorial(n):
    if n == 0:          # Base case
        return 1
    return n * factorial(n - 1)   # Recursive case

Time Complexity:O(n)

Space Complexity:O(n) (due to recursion stack)


Python uses a call stack.

Each recursive call:

Gets its own memory space

Stores local variables

Waits until deeper calls return

Execution happens in two phases:

Going down the stack (function calls)

Coming up the stack (returning values)


Types :

1️⃣ Direct Recursion

A function calls itself directly.

def func(n):
    if n == 0:
        return
    func(n-1)
2️⃣ Indirect Recursion

Function A calls Function B, and B calls A.

def A(n):
    if n > 0:
        B(n-1)

def B(n):
    if n > 0:
        A(n-1)
3️⃣ Linear Recursion

Function makes only one recursive call.

Example: Factorial

Time complexity → O(n)

4️⃣ Binary (Tree) Recursion

Function makes two or more recursive calls.

Example: Fibonacci

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

Time complexity → O(2^n)

5️⃣ Tail Recursion

Recursive call is the last operation in the function.

def fact(n, acc=1):
    if n == 0:
        return acc
    return fact(n-1, acc*n)

⚠ Python does NOT optimize tail recursion.

6️⃣ Head Recursion

Recursive call happens first, then operations.

def print_numbers(n):
    if n == 0:
        return
    print_numbers(n-1)
    print(n)


Recursion vs Iteration

Uses call stack  	        Uses loops
Cleaner for tree problems	More memory efficient
May cause stack overflow	No stack overflow risk
Slower in Python          	Faster


Applications of Recursion in DSA:

                        🌳 Tree Traversals (Inorder, Preorder, Postorder)

                        🔎 DFS (Depth First Search)

                        🔁 Backtracking

                        ⚡ Divide and Conquer

                        🧠 Dynamic Programming (Top-down)

                        📦 Merge Sort

                        ⚡ Quick Sort

                        🔢 Binary Search


Advantages of Recursion:

                        ✅ Code becomes short and clean
                        ✅ Natural for tree/graph problems
                        ✅ Easy to implement divide-and-conquer

Disadvantages of Recursion:

                        ❌ Uses extra memory (stack)
                        ❌ Slower due to function call overhead
                        ❌ Risk of stack overflow
                        ❌ Hard to debug sometimes


Default recursion depth ≈ 1000

import sys
print(sys.getrecursionlimit())

To increase:
sys.setrecursionlimit(10**6)

        ✅ Yes — but only at the Python interpreter level.
        ❗ It does NOT increase the actual C stack memory.

        It does NOT:

        Increase C stack size

        Increase system memory

        Prevent segmentation faults

        Python runs on top of C.

        Every Python function call also consumes C stack memory.

        That memory is controlled by the OS, not Python.