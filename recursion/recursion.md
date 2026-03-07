# Recursion

Recursion occurs when a function calls itself until a specified condition is met.

Every recursive function must have two main components:
1. ✅ **Base Case**: The stopping condition that prevents infinite recursion.
2. ✅ **Recursive Case**: The function calls itself with a smaller/simpler input.

```python
def factorial(n):
    if n == 0:          # Base case
        return 1
    return n * factorial(n - 1)   # Recursive case
```

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)` (due to the recursion stack)

---

## The Call Stack

Python uses a call stack. Each recursive call:
- Gets its own memory space
- Stores its local variables
- Waits until deeper calls return

Execution happens in two phases:
1. **Going down the stack:** Making function calls.
2. **Coming up the stack:** Returning values.

---

## Types

### 1️⃣ Direct Recursion
A function calls itself directly.
```python
def func(n):
    if n == 0:
        return
    func(n-1)
```

### 2️⃣ Indirect Recursion
Function `A` calls Function `B`, and Function `B` calls Function `A`.
```python
def A(n):
    if n > 0:
        B(n-1)

def B(n):
    if n > 0:
        A(n-1)
```

### 3️⃣ Linear Recursion
The function makes only one recursive call at a time.
- **Example:** Factorial
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)` 

### 4️⃣ Binary (Tree) Recursion
The function makes two or more recursive calls.
- **Example:** Fibonacci sequence
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
- **Time Complexity:** `O(2^n)`
- **Space Complexity:** `O(n)` 

### 5️⃣ Tail Recursion
Recursive call is the last operation in the function.
```python
def fact(n, acc=1):
    if n == 0:
        return acc
    return fact(n-1, acc*n)
```
> ⚠️ **Note:** Python does **NOT** optimize tail recursion.

### 6️⃣ Head Recursion
Recursive call happens first, then operations.
```python
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n-1)
    print(n)
```

---

## Recursion vs Iteration

| Feature | Recursion | Iteration |
|---------|-----------|-----------|
| **Mechanism** | Uses the call stack | Uses loops (`for`, `while`) |
| **Use Case** | Cleaner for tree/graph problems | More memory efficient |
| **Risk** | May cause stack overflow | No stack overflow risk |
| **Performance (Python)** | Slower | Faster |

---

## Applications of Recursion in DSA

- 🌳 **Tree Traversals:** Inorder, Preorder, Postorder
- 🔎 **DFS:** Depth First Search in Graphs/Trees
- 🔁 **Backtracking:** e.g., N-Queens, Sudoku Solver
- ⚡ **Divide and Conquer:** Breaking problems into smaller subproblems
- 🧠 **Dynamic Programming:** Top-down approach (Memoization)
- 📦 **Merge Sort**
- ⚡ **Quick Sort**
- 🔢 **Binary Search**

---

## Pros and Cons

### ✅ Advantages
- Code becomes short and clean
- Natural and intuitive for tree/graph problems
- Easy to implement divide-and-conquer algorithms

### ❌ Disadvantages
- Uses extra memory (stack space)
- Slower due to function call overhead
- Risk of stack overflow for deep recursion levels
- Hard to debug sometimes

---

The default recursion depth in Python is **≈ 1000**.

To check your current limit:
```python
import sys
print(sys.getrecursionlimit())
```

To increase:
```python
import sys
sys.setrecursionlimit(10**6)
```

**Is increasing the limit always safe?**
✅ Yes — but only at the Python interpreter level.
❗ It does **NOT** increase the actual C stack memory.

It does **NOT**:
- Increase the C stack size
- Increase system memory
- Prevent segmentation faults

Python runs on top of C. Every Python function call also consumes C stack memory, and that memory is controlled by the OS, not Python.

---

## 🌳 Recursion Tree
A recursion tree is a diagram that shows how recursive calls expand and branch during execution.
