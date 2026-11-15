# Mission 3 — Understand the operating system

## 1. Task / objective
The objective of this mission is to investigate core operating system (OS) concepts, including:
- Examining the current operating system version, active user identity, storage capacity, and system activity.
- Understanding how processes function and identifying Process IDs (PIDs).
- Distinguishing between absolute and relative paths, and interpreting Unix file permission flags (`r`, `w`, `x`).
- Explaining the fundamental responsibilities of modern operating systems.

---

## 2. Work completed

### Task 3.1 — Explore your operating system
*(Personal identifying details such as device names and exact usernames have been replaced with `[redacted]` in accordance with privacy rules.)*

| Information explored | What it tells you | Your observation (privacy-safe) |
|---|---|---|
| **Operating system / system details** | Identifies the OS product, version release, and underlying hardware architecture. | macOS version 27.2.1 (Darwin Kernel version 27.2.0, `arm64` architecture / Apple Silicon). |
| **Current account identity** | Identifies the current non-root user shell session and active security identity. | Active account: `[redacted]` |
| **Available and used storage** | Shows mounted file systems, overall partition capacity, space consumed, and remaining free space. | Root file system (`/`): Total Size ~926 GiB, Used ~13 GiB, Available ~800 GiB (~2% utilized). |
| **System activity snapshot** | Provides real-time metrics on processor workloads, memory usage, and active background daemons. | Multi-core CPU active, showing graphics compositor (`WindowServer`), browser processes, and IDE tasks running smoothly. |

---

### Task 3.2 — Understand processes
A snapshot of running processes was inspected using `ps aux`.

#### Concept Answers:
- **What is a process?**
  A process is an active, executing instance of a computer program loaded into system memory (RAM). It consists of executable machine code, dedicated memory segments (stack, heap, data), CPU register states, and OS resources such as open file handles.
- **What does the PID column represent?**
  PID stands for **Process Identifier**. It is a unique positive integer assigned by the operating system kernel to each active process when it is spawned. The OS and user utilize PIDs to track, manage, signal, or terminate individual processes.
- **Two examples of processes running on this computer:**
  1. `WindowServer` (PID ~607): The macOS system compositor daemon responsible for window management, screen rendering, and event routing.
  2. `Brave Browser` / `Google Chrome` (PID ~6354): An interactive user-facing application process handling web page rendering and browsing tabs.

---

### Task 3.3 — Understand paths and permissions

#### Absolute vs. Relative Paths
- **Difference:**
  - An **absolute path** specifies the full, unambiguous location of a file or folder starting from the root directory (`/`). It is independent of the current working directory.
  - A **relative path** specifies a location relative to the current working directory, using indicators such as `.` (current folder) or `..` (parent folder).
- **Examples from this assignment repository:**
  - *Absolute path:* `/Users/[redacted]/Desktop/digital-detective-8426/mission-03-operating-system`
  - *Relative path:* `../mission-02-terminal/terminal-practice/sample.txt` (or `./README.md`)

#### File Permissions Analysis
Inspecting `sample.txt` in the practice directory revealed:
```text
-rw-r--r--  1 [redacted]  staff  73 Nov 15 22:04 sample.txt
```
- **Permission Breakdown for Owner:**
  - Owner permissions: `rw-`
  - **Read (`r`):** Allowed. The owner can open and view file contents.
  - **Write (`w`):** Allowed. The owner can modify or overwrite the file.
  - **Execute (`x`):** Denied (`-`). The file is plain text and cannot be executed as a program.

| Permission | Meaning | Example |
|---|---|---|
| `r` — Read | Allows a file's contents to be read / viewed. | Opening a text file or reading source code. |
| `w` — Write | Allows a file to be modified, edited, or deleted. | Saving changes in a document or appending logs. |
| `x` — Execute | Allows a file to be executed as a program or script; on a folder, allows traversal. | Running a compiled executable or shell script (`./run.sh`). |

---

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
|---|---|---|
| **Process management** | Coordinates CPU time across concurrent tasks using preemptive multitasking and scheduling algorithms. | The OS pauses a background music player momentarily to allocate CPU cycles to a web browser tab. |
| **Memory management** | Allocates and tracks physical RAM addresses and virtual memory pages so programs do not corrupt each other's data. | Allocating 250 MB of RAM when opening an image editor and reclaiming it when the app closes. |
| **Device management** | Communicates with hardware peripherals through standardized software drivers and input/output controllers. | Translating raw USB keyboard electrical pulses into standardized character input streams. |
| **File management** | Organizes data into structured hierarchical directories, tracking file metadata, storage sectors, and access permissions. | Creating a folder hierarchy on an APFS/NTFS drive to store documents and finding them by filename. |
| **User interface / shell** | Provides a command-line shell (CLI) or graphical user interface (GUI) so humans can control the computer. | Rendering interactive desktop windows, dock icons, or running Zsh in Terminal. |
| **Security and permissions** | Enforces user access controls, authentication, sandboxing, and prevents unauthorized system tampering. | Requiring user confirmation or password authentication before installing software or reading protected files. |

---

## 3. Commands / tools used
- `sw_vers` & `uname -mrs`: Inspected macOS version details and Darwin kernel architecture.
- `whoami`: Verified current active user session identity.
- `df -h /`: Checked mounted disk storage capacity and utilization in human-readable gigabytes.
- `ps aux | head`: Inspected process tables, process IDs (PID), and resource utilization.
- `ls -l`: Inspected file permission bits, ownership, and modification timestamps.

---

## 4. My understanding
The operating system acts as the intermediary between hardware silicon and user applications. Without the OS, every program would have to implement its own hardware drivers and direct memory addressing. By managing processes, enforcing memory boundaries, abstracting storage into files, and restricting access via permission bits (`rwx`), the OS guarantees system stability, security, and usability.

---

## 5. Difficulties faced
No major difficulties. Redacting private device and user details while keeping accurate diagnostic observations was done carefully.

---

## 6. How I resolved them
Replaced sensitive personal identifiers with `[redacted]` placeholders to ensure complete privacy while preserving technical fidelity.

---

## 7. Evidence / files
- `mission-03-operating-system/README.md` (this report containing system diagnostics, process analysis, path/permission explanations, and OS responsibility table).

---

## 8. Commit details
- **Commit message:** `Document operating system and file management`
- **Push status:** Verified and pushed to remote GitHub repository `origin/master`.
