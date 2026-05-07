# Contributing to DSA

First off — **thank you for taking the time to contribute!** 🎉  
Every contribution, big or small, helps this become a better resource for everyone learning DSA.

---

## Table of Contents

- [Getting Started](#getting-started)
- [What Can I Contribute?](#what-can-i-contribute)
- [Folder Structure](#folder-structure)
- [Code Style Guidelines](#code-style-guidelines)
- [How to Submit a PR](#how-to-submit-a-pr)
- [Commit Message Format](#commit-message-format)
- [Issue Guidelines](#issue-guidelines)
- [Don'ts](#donts)

---

## Getting Started

1. **Fork** this repository
2. **Clone** your fork locally
   ```bash
   git clone https://github.com/your-username/DSA.git
   cd DSA
   ```
3. Create a **new branch** for your contribution
   ```bash
   git checkout -b add/pattern-name
   ```
4. Make your changes, then push and open a **Pull Request**

---

## What Can I Contribute?

| Type | Examples |
|------|---------|
| 🆕 New Pattern | Add a new DSA pattern with explanation + code |
| 🐛 Bug Fix | Fix incorrect logic, wrong output, or broken code |
| 💡 Better Solution | Improve TC/SC of an existing solution |
| 📝 Documentation | Improve README, add comments, fix typos |

---

## Folder Structure

Please follow the existing structure when adding new content:

```
DSA/
├── recursion/
│   ├── recursion.md          ← pattern explanation + TC/SC
│   ├── N-Queens.py
│   ├── rat_in_a_maze.py
│   └── ...
├── arrays/
│   ├── arrays.md
│   ├── merge_sorted.py
│   └── ...
└── ...
```

Every pattern folder **must** have:
- A `README.md` explaining the pattern with at least one example
- At least one working code file
- TC and SC mentioned either in comments or in `README.md`

---

## Code Style Guidelines

### General Rules

- Write **clean, readable code** — prioritize clarity over cleverness
- Add **comments** to explain non-obvious logic
- Always mention **Time Complexity** and **Space Complexity** at the bottom of the code
- Use **meaningful variable names** (`left`, `right` over `l`, `r`)
- No hardcoded test inputs inside solution functions

### Python

```python

def max_sum_subarray(arr: list[int], k: int) -> int:
    # your clean code here
    pass

# TC: O(n) 
# SC: O(1)
```

- Follow [PEP 8](https://peps.python.org/pep-0008/)
- Use type hints wherever possible
- Use snake_case for functions and variables


## How to Submit a PR

1. Make sure your branch is **up to date** with `main`
   ```bash
   git fetch origin
   git rebase origin/main
   ```
2. Run your code locally and verify the output is **correct**
3. Push your branch
   ```bash
   git push origin add/sliding-window-max
   ```
4. Open a Pull Request and fill out the **PR template**
5. Wait for a review — we usually respond within **1–2 weeks**

### PR Checklist

Before submitting, make sure:

- [ ] Code runs without errors
- [ ] TC and SC are mentioned
- [ ] Follows the folder structure
- [ ] README.md updated if adding a new pattern
- [ ] No plagiarized code from LeetCode editorials or paid resources

---

## Commit Message Format

Use clear and consistent commit messages:

```
<type>/<short-description>

Types:
  add      → new pattern or solution
  fix      → bug fix
  improve  → better TC/SC or refactor
  docs     → documentation changes
  test     → adding test cases
```

### Examples

```
add/sliding-window-longest-substring
fix/binary-search-off-by-one
improve/dp-knapsack-space-optimized
docs/update-two-pointer-readme
```

---

## Issue Guidelines

When opening an issue, please use the right label:

| Label | When to use |
|-------|------------|
| `bug` | Something is broken or gives wrong output |
| `enhancement` | Suggest a new pattern or improvement |
| `discussion` | Ask about a pattern or approach |
| `help wanted` | You're stuck and need guidance |

Always include:
- What you expected vs what actually happened
- The input/output if it's a bug
- Language and environment if relevant

---

## Don'ts

- ❌ Don't copy solutions directly from LeetCode editorial or GeeksforGeeks without rewriting and crediting
- ❌ Don't submit AI-generated code without understanding and verifying it
- ❌ Don't add solutions without TC/SC analysis
- ❌ Don't open a PR without testing your code first
- ❌ Don't change unrelated files in your PR

---

## Questions?

Open a [GitHub Discussion](../../discussions) or drop a comment on any relevant issue. We're happy to help!

Happy coding! 🚀  
*— Maintained with ❤️ under the [MIT License](./LICENSE)*