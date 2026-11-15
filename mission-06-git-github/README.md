# Mission 6 — Git and GitHub

## 1. Task / objective
The objective of this mission is to master modern distributed version control and collaborative workflows by:
- Understanding basic Git mechanics: tracking status, staging specific modifications, creating atomic commits, and inspecting commit logs.
- Creating an isolated feature branch (`update-about`), updating repository documentation, and publishing the branch to GitHub.
- Opening and documenting a Pull Request (PR) on GitHub, merging changes into the primary branch, and pulling updates back locally.
- Compiling an essential Git command glossary and explaining collaborative version control concepts.

---

## 2. Work completed

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does in your own words |
|---|---|
| **Check repository status** (`git status`) | Displays the current branch, tracks staged changes ready to commit, untracked files, and unstaged modifications. |
| **Stage selected changes** (`git add <file>`) | Moves specified file changes into the staging area (index), preparing an exact snapshot for the next commit. |
| **Create a commit** (`git commit -m "..."`) | Permanently records the staged snapshot into the repository's version history with a unique SHA hash and descriptive message. |
| **View commit history** (`git log` / `git log --oneline`) | Displays chronological history of past commits showing commit hashes, author details, dates, and messages. |

#### Difference Between Staging a Change and Committing It:
- **Staging (`git add`):** Staging acts as an intentional drafting table or buffer (the index). It allows a developer to selectively pick which file modifications should be included in the next snapshot. Staging does not save anything permanently to history; it merely prepares the snapshot.
- **Committing (`git commit`):** Committing takes whatever snapshot is currently in the staging area and permanently records it into the Git repository tree. Each commit receives a unique SHA-1/SHA-256 hash, an author timestamp, and becomes an immutable milestone that can be reviewed, referenced, or reverted.

---

### Task 6.2 — Create and use a branch
1. Created a new branch named `update-about` from local `master`:
   ```bash
   git checkout -b update-about
   ```
2. Edited the root `README.md` to add a new section titled **`## My Learning`** describing key insights gained across the computer basics, terminal, operating systems, and data representation missions.
3. Inspected status (`git status`), staged the updated `README.md` (`git add README.md`), and committed the change:
   ```bash
   git commit -m "Add My Learning section to root README"
   ```
4. Published the branch to the remote repository on GitHub:
   ```bash
   git push -u origin update-about
   ```

---

### Task 6.3 — Create a Pull Request (PR)
1. **PR Creation:** Opened Pull Request **#1** from branch `update-about` into `master`:
   - **URL:** [PR #1 on GitHub](https://github.com/aryansirohi2121-coder/digital-detective-8426/pull/1)
   - **Title:** `Add My Learning section to root README`
   - **Description:** Added summary of learnings and refined repository navigation structure.
2. **PR Review & Merge:** Reviewed the diff on GitHub and successfully merged the Pull Request using `gh pr merge 1 --merge`.
3. **Local Sync:** Switched back to the main branch (`master`) and pulled the merged changes onto the local computer:
   ```bash
   git checkout master
   git pull origin master
   ```

#### Concept Explanations:
- **What is a branch?**
  A branch is an independent, lightweight pointer to a specific commit in Git. It creates an isolated workspace where a developer can build new features, test code, or fix bugs without affecting the stable code on the main branch.
- **What is a Pull Request (PR)?**
  A Pull Request is a collaborative mechanism (hosted on platforms like GitHub) that notifies team members that changes on a feature branch are ready for review. It provides a web interface to inspect code diffs, leave comments, run automated tests, and discuss modifications before integrating them into the target branch.
- **Why branches and Pull Requests are useful in teams:**
  They prevent team members from overwriting each other's work or introducing breaking changes into production. Multiple developers can work on distinct features simultaneously on separate branches. Pull Requests enforce code reviews, maintain code quality standards, and create an auditable discussion history for every change.

---

### Task 6.4 — Build your Git command glossary

| Git operation | Command | One-line explanation in your own words |
|---|---|---|
| **Initialise a repository** | `git init` | Creates a new Git version control repository inside the current project folder by setting up the `.git` directory. |
| **Check status** | `git status` | Displays working tree status, showing tracked, unstaged, staged, and untracked file changes. |
| **Stage changes** | `git add <file>` | Adds file modifications to the staging index to be packaged into the upcoming commit. |
| **Commit changes** | `git commit -m "<msg>"` | Permanently records the staged snapshot into the repository history with an explanatory message. |
| **View history** | `git log --oneline` | Displays a reverse-chronological list of past commits, hashes, and commit descriptions. |
| **Create or list branches** | `git branch` / `git branch <name>` | Lists all local repository branches or creates a new pointer to the current commit. |
| **Switch branches** | `git checkout <name>` / `git switch <name>` | Moves the HEAD pointer and updates workspace files to match the specified branch. |
| **Publish changes** | `git push -u origin <branch>` | Uploads local branch commits to the designated remote repository on GitHub. |
| **Retrieve remote changes** | `git pull origin <branch>` | Fetches commits from the remote repository and immediately integrates/merges them into the local branch. |

---

## 3. Commands / tools used
- `git checkout -b update-about`: Created and switched to a new branch.
- `git status`, `git add`, `git commit`: Git staging and commit workflow.
- `git push -u origin update-about`: Published branch to remote GitHub repository.
- `gh pr create`: Generated GitHub Pull Request #1 via GitHub CLI.
- `gh pr merge 1 --merge`: Merged the Pull Request on GitHub.
- `git checkout master` & `git pull origin master`: Synchronized local master with remote changes.

---

## 4. My understanding
Git separates file modifications into three distinct zones: the working directory, the staging area (index), and the committed repository history (`.git`). This three-tiered architecture provides fine-grained control over which changes are committed together. Furthermore, branching and Pull Requests provide psychological and technical safety: developers can experiment freely on isolated branches and ensure peer validation through PR reviews before merging into the main branch.

---

## 5. Difficulties faced
No major difficulties. Ensured that the PR targeted `master` (the repository's default branch) and synchronized local changes cleanly following the merge.

---

## 6. How I resolved them
Verified the remote branch name using `git branch -a`, targeted `master` directly in the PR, and verified the fast-forward pull locally.

---

## 7. Evidence / files
- Pull Request #1: `https://github.com/aryansirohi2121-coder/digital-detective-8426/pull/1`
- Root `README.md` updated with `## My Learning` section.
- `mission-06-git-github/README.md`: This report containing workflow analysis, PR documentation, and Git glossary.

---

## 8. Commit details
- **Commit message:** `Complete Git and GitHub collaboration mission`
- **Push status:** Verified and pushed to remote GitHub repository `origin/master`.
