# Mission 1 — Know your computer

## 1. Task / objective
The objective of this mission is to understand fundamental computer concepts by:
- Tracing a real-world computer activity through the Input-Process-Output-Storage (IPOS) model.
- Identifying and classifying essential hardware components and software types (operating system, application, and utility software).
- Exploring everyday computer-based embedded systems found outside typical PCs and smartphones.

---

## 2. Work completed

### Task 1.1 — Trace one activity using IPOS
**Chosen activity:** Typing a report in a text editor and saving it to disk.

| Stage | What happens in your example? | Possible hardware / component |
|---|---|---|
| **Input** | The user presses keys on the keyboard to compose sentences, and clicks with the mouse to place the cursor. Keypress electrical signals are sent to the controller. | Keyboard, Mouse, Trackpad |
| **Processing** | The CPU fetches keycode inputs, decodes character mappings, executes word processing logic, and temporarily holds active document buffers in RAM. | CPU (Central Processing Unit), RAM (Main Memory) |
| **Output** | The graphics processor and display render characters instantly on screen so the user can visually review what has been typed. | Display / Monitor, GPU |
| **Storage** | When the user selects "Save", the file system writes the text stream permanently as data blocks onto non-volatile storage. | SSD (Solid State Drive), NVMe storage, or Cloud Storage |

**How the activity moves from input to output and storage:**
1. Keystrokes generate electrical scan codes via the input hardware.
2. The operating system kernel and CPU process these interrupt signals and update active data in fast, volatile memory (RAM).
3. The display pipeline immediately projects rendered visual glyphs onto the screen (output).
4. When saved, the stream of bits is transferred from volatile RAM through the storage bus into flash memory cells on the SSD (storage) for long-term retention.

---

### Task 1.2 — Identify hardware and software
A computer system requires both physical components (hardware) and instruction sets (software) to perform useful work.

| Item / software name | Hardware or software? | Software type (if applicable) | Purpose |
|---|---|---|---|
| Keyboard | Hardware | Not applicable | Captures physical keypresses to input textual data and keyboard shortcuts into the computer. |
| SSD (NVMe Solid State Drive) | Hardware | Not applicable | Provides persistent, high-speed, non-volatile storage for files, programs, and the OS. |
| CPU (Processor) | Hardware | Not applicable | Executes instructions, performs arithmetic and logic calculations, and coordinates hardware components. |
| Monitor / Display | Hardware | Not applicable | Displays graphical output, user interfaces, windows, and rendered video to the user. |
| macOS | Software | Operating System | Manages hardware resources, coordinates running processes, manages file systems, and provides user interfaces. |
| Google Chrome | Software | Application Software | Allows users to browse websites, access web services, stream media, and run web apps. |
| Visual Studio Code | Software | Application Software | Provides an integrated development environment (IDE) for writing, editing, and debugging code. |
| Time Machine / Disk Utility | Software | Utility Software | Performs system diagnostics, drive health management, and automated disk backups for system maintenance. |

---

### Task 1.3 — Computer systems around you
Beyond desktop laptops and smartphones, specialized microprocessors and computing systems are embedded everywhere in modern infrastructure:

| System | Main purpose | One input | One output |
|---|---|---|---|
| **Automated Teller Machine (ATM)** | Authenticates bank customers to disburse cash and manage financial transactions safely. | Card reader / PIN keypad | Cash dispenser / Transaction receipt printer |
| **Smart Traffic Signal Controller** | Dynamically regulates the flow of vehicular and pedestrian traffic to reduce congestion. | Under-road inductive loop sensor (or pedestrian push button) | Coloured signal lights (Green / Yellow / Red) |
| **Home Microwave Oven** | Regulates cooking duration, microwave magnetron power, and safety door interlocks. | Membrane touch keypad (duration and power level) | Digital countdown LED display / Completion buzzer |

---

## 3. Commands / tools used
- **Text Editor / Markdown Editor:** Used to create, format, and structure the mission report according to assignment specifications.
- **Terminal & Git:** Used to inspect status, stage files, and prepare version control commits.

---

## 4. My understanding
- **IPOS Model:** A computer is essentially an information processor. Every task follows the cycle of receiving raw data (Input), transforming it according to stored rules (Processing), presenting actionable results (Output), and keeping records for later use (Storage).
- **Hardware vs. Software:** Hardware provides physical execution capacity (circuits, silicon, buses, displays), whereas software provides dynamic instructions that guide hardware execution.
- **Software Categories:**
  - *Operating System:* The foundational layer that abstracts hardware and manages system calls.
  - *Application Software:* End-user software built to solve specific productivity or leisure tasks.
  - *Utility Software:* Diagnostic, maintenance, and security software that keeps the system stable and efficient.
- **Ubiquitous Computing:** Modern society relies heavily on dedicated embedded computing systems that perform specialized control loops reliably.

---

## 5. Difficulties faced
No major difficulties. Mapping the internal movement of data between RAM and SSD during text processing required visualizing the difference between volatile working memory and persistent flash storage.

---

## 6. How I resolved them
Reviewed the functional difference between system memory (RAM) and secondary storage (SSD) to describe the exact stages of the IPOS lifecycle accurately.

---

## 7. Evidence / files
- `mission-01-computer-basics/README.md` (this report containing completed IPOS table, hardware/software classifications, and embedded system analysis).

---

## 8. Commit details
- **Commit message:** `Complete computer basics and IPOS mission`
- **Push status:** Verified and pushed to remote GitHub repository `origin/master`.
