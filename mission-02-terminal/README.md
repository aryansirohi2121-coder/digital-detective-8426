# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
The goal of this mission is to develop practical fluency in the command-line interface (CLI) by:
- Practising foundational terminal navigation and file manipulation commands.
- Managing practice files safely using redirection (`>` vs `>>`), file copying, and renaming.
- Understanding command flags/options and using Unix pipelines (`|`) to connect commands.
- Investigating package managers and documenting how package management works on macOS.

---

## 2. Work completed

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
|---|---|---|
| **Current-directory display** (`pwd`) | Prints the full absolute path of the current working directory to standard output. | Displayed the active path: `.../digital-detective-8426/mission-02-terminal/terminal-practice` |
| **Directory listing** (`ls`) | Lists names of non-hidden files and folders contained in the target directory. | Displayed filenames cleanly in standard layout: `sample.txt`, `sample_archive.txt` |
| **Detailed listing** (`ls -l`) | Displays entries in a long list format showing file permissions, owner, group, size in bytes, and timestamp. | Showed columns with permissions (e.g. `-rw-r--r--`), ownership, byte sizes, and timestamps. |
| **Change directory** (`cd ..`) | Moves navigation up one level in the folder hierarchy to the parent directory. | Path changed from subfolder up to parent folder. |
| **Create directory** (`mkdir`) | Creates one or more new directories at the specified path. | Created the target directory `terminal-practice` without errors. |
| **Create empty file** (`touch`) | Creates a new zero-byte file if it does not exist, or updates its access/modification timestamps if it does. | Created `sample.txt` with an initial size of 0 bytes. |
| **Copy file** (`cp`) | Duplicates an existing file to a target destination with a new name or location. | Made a duplicate `sample_backup.txt` retaining the exact same contents. |
| **Move / rename file** (`mv`) | Relocates or renames a file or directory from source to destination. | Renamed `sample_backup.txt` to `sample_archive.txt`; the old filename ceased to exist. |
| **Display file contents** (`cat`) | Concatenates and prints the contents of one or more files directly into the terminal window. | Printed the stored text lines directly to standard output. |

---

### Task 2.2 — Practise file changes safely
A practice folder named `terminal-practice` was created inside the mission area.

1. **Step 1:** Created a new file and wrote the first line using overwrite redirection:
   ```bash
   echo "Line 1: Exploring Terminal operations." > sample.txt
   ```
2. **Step 2:** Appended a second line without removing the first line using append redirection:
   ```bash
   echo "Line 2: Appending content safely." >> sample.txt
   ```
3. **Step 3:** Displayed contents using `cat sample.txt` to confirm both lines were present:
   ```text
   Line 1: Exploring Terminal operations.
   Line 2: Appending content safely.
   ```
4. **Step 4:** Created a backup copy and renamed it:
   ```bash
   cp sample.txt sample_backup.txt
   mv sample_backup.txt sample_archive.txt
   ```

#### Concept Answers:
- **Difference between replacing a file's contents and adding text to the end:**
  - Using the single chevron `>` (overwrite redirection) creates a new file or completely replaces/truncates any existing contents with new output.
  - Using double chevrons `>>` (append redirection) preserves existing data and appends new content directly to the end of the file.
- **Difference between copying a file and moving a file:**
  - `cp` (copy) duplicates the data so that two independent instances exist at different paths or filenames.
  - `mv` (move/rename) updates the file's path or name in the file system table without creating a duplicate; the original name/location disappears.
- **What information does the current-directory display provide?**
  - `pwd` shows the exact absolute path from the root directory (`/`) to the current directory, eliminating ambiguity about where commands will execute and where relative paths will resolve.
- **Why is a directory-listing operation useful?**
  - `ls` gives immediate situational awareness: it reveals what files and subdirectories exist, their exact spellings, and with options like `-la`, allows verification of permissions, hidden files, and modification dates.

---

### Task 2.3 — Understand flags and pipes
- **Comparing standard listing (`ls`) vs. detailed listing with flags (`ls -lah`):**
  - `ls`: Shows only file and folder names in standard columns, ignoring hidden dotfiles.
  - `ls -lah`:
    - `-l` switches to long format with permissions, link counts, owners, file size, and timestamp.
    - `-a` includes all hidden files and folders starting with a dot (`.` and `..`).
    - `-h` formats byte sizes into human-readable units (e.g., KB, MB, GB).
- **Understanding the Pipe (`|`):**
  - Command tested: `ls -la | head -n 5`
  - **What the pipe does:** The pipe character connects the standard output (`stdout`) of the command on its left directly into the standard input (`stdin`) of the command on its right, without creating any temporary files on disk.
  - **Contribution of each side:**
    - *Left side (`ls -la`):* Produces a comprehensive list of all directory contents and writes it to stdout.
    - *Right side (`head -n 5`):* Accepts that incoming stream and filters it to output only the first 5 lines to the screen.

---

### Task 2.4 — Understand package managers
- **Homebrew on macOS:**
  - Homebrew version checked: `Homebrew 7.0.12`
  - Packages checked: Tested via `brew list` (showing installed packages such as `ca-certificates`, `cairo`, `cowsay`, etc.).
- **Why package managers are useful:**
  A package manager automates the discovery, installation, dependency resolution, upgrading, and uninstallation of software packages from verified central repositories. Instead of manually downloading archives, verifying checksums, compiling source code, and hunting down missing library dependencies, a single command allows the package manager to fetch and configure the software reliably while keeping track of all installed dependencies.

---

## 3. Commands / tools used
- `pwd`: Print Working Directory.
- `ls`, `ls -l`, `ls -lah`: List directory contents with various flags.
- `cd`: Change Directory.
- `mkdir`: Make Directory.
- `touch`: Create empty file or update timestamps.
- `echo` with `>` and `>>`: Write and append text streams.
- `cat`: Concatenate and print file contents.
- `cp`: Copy files.
- `mv`: Move / rename files.
- `head`: Filter first N lines of an incoming text stream.
- `brew --version`, `brew list`: Inspect package manager status without installing/removing software.

---

## 4. My understanding
The command line provides direct, scriptable, and precise control over the operating system. Understanding the difference between stream truncation (`>`) and appending (`>>`) prevents accidental data loss. Furthermore, the Unix philosophy of combining small, focused tools using pipelines (`|`) enables sophisticated text filtering and data processing right from the shell.

---

## 5. Difficulties faced
No major difficulties. Ensured that practice file manipulations remained confined to the dedicated `terminal-practice` folder so as not to clutter the repository root.

---

## 6. How I resolved them
Not applicable.

---

## 7. Evidence / files
- `mission-02-terminal/README.md`
- `mission-02-terminal/terminal-practice/sample.txt`
- `mission-02-terminal/terminal-practice/sample_archive.txt`

---

## 8. Commit details
- **Commit message:** `Complete Terminal and file management mission`
- **Push status:** Verified and pushed to remote GitHub repository `origin/master`.
