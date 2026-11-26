# Mission 4 — How programs run

## 1. Task / objective
Create and run a one-line Python program (`hello.py`) from Terminal, and compare how compilers and interpreters translate and execute code.

## 2. Work completed

### Task 4.1 — Create and run a Python program
- Created `hello.py` inside `mission-04-programs/` with the single line:
  ```python
  print("Hello from Python")
  ```
- Executed `python3 hello.py` in Terminal and observed the output:
  ```text
  Hello from Python
  ```

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translates the whole source-code file before the program runs. | Reads, translates, and executes instructions line by line at runtime. |
| **Typical output** | Produces a separate executable binary or compiled output file (e.g., machine code). | Runs the program directly without needing a standalone machine-code executable beforehand. |
| **One example** | C (`gcc` / `clang`) or C++ (`g++`). | Python (`python3`) or Ruby. |
| **One advantage** | Compiled programs usually execute faster because translation is already done beforehand. | Easier to test and debug quickly because changes run immediately without a separate build step. |

**Explanation in my own words:**
As shown in the comparison table, the main difference between a compiler and an interpreter is when translation happens and what output is produced. A compiler translates the entire source program ahead of time into a separate executable file (such as machine code in C or C++), which makes repeated runs fast. An interpreter, like Python (`python3`), executes instructions at runtime without a manual compilation step beforehand, which makes testing and quick edits very convenient. (Many real-world language runtimes, including CPython, also use internal bytecode behind the scenes while still giving developers an interpreted workflow.)

## 3. Commands / tools used
- Text editor — Created `hello.py`.
- `python3 hello.py` — Ran the Python script using Python 3 (`Python 3.13.15`) and verified the output.

## 4. My understanding
Source code written by humans must be translated into instructions the computer's CPU can carry out. Compiled workflows pay the translation cost once up front to produce fast executables, while interpreted workflows run code immediately at runtime, making them great for learning, scripting, and rapid prototyping.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- [hello.py](hello.py) — One-line Python script printing `Hello from Python`.
- [README.md](README.md) — Execution observation and compiler vs. interpreter comparison.

## 8. Commit details
- **Commit message:** `Compare compilers and interpreters`
- **Status:** Committed on `main` and pushed to GitHub.
