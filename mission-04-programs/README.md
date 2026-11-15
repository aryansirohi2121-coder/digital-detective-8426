# Mission 4 — How programs run

## 1. Task / objective
The objective of this mission is to understand how computer programs are executed by:
- Writing and running a simple Python program (`hello.py`) via the terminal using the Python 3 interpreter.
- Comparing how compilers and interpreters process source code into executable instructions.
- Explaining the trade-offs, advantages, and operational stages of compiled vs. interpreted languages.

---

## 2. Work completed

### Task 4.1 — Create and run a Python program
- Created `hello.py` inside `mission-04-programs/` containing:
  ```python
  print("Hello from Python")
  ```
- Executed the script from the command line:
  ```bash
  python3 hello.py
  ```
- **Observed output:**
  ```text
  Hello from Python
  ```

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
|---|---|---|
| **When translation / execution happens** | Translation happens entirely upfront during a separate compilation phase before execution begins. | Translation occurs on-the-fly line-by-line (or via bytecode VM instructions) directly at runtime. |
| **Typical output** | Produces a standalone binary executable file containing native machine code (e.g. `.exe` or ELF/Mach-O binary). | Does not produce a standalone machine-code binary; executes instructions directly in memory within the interpreter runtime. |
| **One example** | C, C++, Rust, or Go | Python, Ruby, JavaScript (Node.js) |
| **One advantage** | Maximum execution speed and CPU optimization because native instructions run directly on hardware with no runtime translation overhead. | Rapid development, fast iterative testing, and effortless cross-platform portability without needing platform-specific recompilation. |

#### Detailed Explanation:
A compiler translates the entire high-level source code into native machine language in advance, producing a standalone executable file that the CPU can execute directly without the compiler present. In contrast, an interpreter reads and processes source instructions dynamically at runtime, translating and executing commands on the fly. As shown in the comparison table, compiled languages (like C or Rust) offer superior raw execution speed and compile-time type safety, whereas interpreted languages (like Python) enable faster prototyping and interactive execution without requiring a separate compilation step.

---

## 3. Commands / tools used
- `python3`: Used to run `hello.py` and invoke the CPython runtime.
- Text Editor: Used to author `hello.py` and document findings in `README.md`.

---

## 4. My understanding
Computers cannot directly understand high-level programming syntax like `print()` or `if/else`; the CPU only executes raw binary machine code instructions. Compilers bridge this gap by transforming code into machine instructions ahead of time, while interpreters perform translation during execution. Many modern environments (including Python with its `.pyc` bytecode files and Java with the JVM) adopt a hybrid approach by compiling source code into portable intermediate bytecode that an efficient virtual machine interprets at runtime.

---

## 5. Difficulties faced
No major difficulties. Running Python 3 from the terminal worked cleanly.

---

## 6. How I resolved them
Not applicable.

---

## 7. Evidence / files
- `mission-04-programs/hello.py`: Python source code printing "Hello from Python".
- `mission-04-programs/README.md`: This mission report containing compiler vs. interpreter analysis.

---

## 8. Commit details
- **Commit message:** `Compare compilers and interpreters`
- **Push status:** Verified and pushed to remote GitHub repository `origin/master`.
