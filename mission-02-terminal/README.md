# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
Use the command-line interface (Terminal) inside the assignment repository to inspect folders, practise creating, copying, moving, and updating files safely inside a `terminal-practice` folder, explore flags and pipes, and inspect Homebrew without modifying installed packages.

## 2. Work completed

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| Current-directory display (`pwd`) | Prints the full path of the folder I am currently working in. | Displayed the full path ending in `/digital-detective-8564`. |
| Directory listing (`ls`) | Lists visible files and folders in the current directory. | Listed `README.md`, `evidence`, and all `mission-00` through `mission-08` folders. |
| Detailed listing (`ls -l`) | Shows permissions, link count, owner, group, file size in bytes, modified timestamp, and name. | Showed permissions like `drwxr-xr-x@` for directories and `-rw-r--r--@` for `README.md` (`2231` bytes). |
| Change directory (`cd ..` / `cd <folder>`) | Moves the working location up to the parent folder or into a named subfolder. | Running `cd ..` moved one level up; running `cd terminal-practice` entered the practice folder. |
| Create directory (`mkdir`) | Creates a new empty folder at the specified path. | Created the `terminal-practice` folder inside the repository. |
| Create empty file (`touch`) | Creates a new zero-byte file if it does not exist, or updates its timestamp. | Created `sample.txt` with size `0B` inside `terminal-practice`. |
| Copy file (`cp`) | Duplicates an existing file to a new file name or location while keeping the original. | Copied `notes.txt` to `notes-backup.txt`; both files existed with identical contents (`67B`). |
| Move / rename file (`mv`) | Moves a file to another location or renames it without leaving a duplicate behind. | Renamed `notes-backup.txt` to `notes-archive.txt`; `notes-backup.txt` was replaced by the new name. |
| Display file contents (`cat`) | Reads and prints the text inside a file directly to the Terminal screen. | Printed both lines stored inside `notes.txt`. |

---

### Task 2.2 — Practise file changes safely
Inside `terminal-practice/`:
1. Created `notes.txt` and added the first line using `echo "First line added safely." > notes.txt`.
2. Appended a second line using `echo "Second line appended without overwriting." >> notes.txt`.
3. Verified both lines with `cat notes.txt`.
4. Created a backup copy (`cp notes.txt notes-backup.txt`) and renamed it (`mv notes-backup.txt notes-archive.txt`).

**Questions and answers:**
- **What is the difference between replacing a file's contents and adding text to the end?**
  Using `>` replaces (overwrites) the entire contents of the file with the new output, whereas `>>` appends the new text to the end of the file while keeping everything already inside it.
- **What is the difference between copying a file and moving a file?**
  Copying (`cp`) creates an independent second copy so both the original and the copy exist; moving/renaming (`mv`) transfers or renames the existing file so only one file remains at the new path or name.
- **What information does the current-directory display provide?**
  `pwd` shows the exact absolute path from the root directory `/` down to the folder where commands are currently being executed.
- **Why is a directory-listing operation useful?**
  `ls` lets you confirm which files and subfolders exist in a folder before opening, editing, copying, or deleting anything, helping prevent mistakes.

---

### Task 2.3 — Understand flags and pipes
- **Comparing `ls` and `ls -lah`:**
  Normal `ls` only displays visible file and folder names in columns. Adding the flags `-l` (long detailed format), `-a` (all files including hidden entries starting with `.` such as `.` , `..`, and `.git`), and `-h` (human-readable sizes like `67B` or `160B` instead of raw byte integers) reveals permissions, hidden items, timestamps, and easier-to-read file sizes.
- **Pipe (`ls -la | head -n 5`):**
  The pipe symbol `|` connects the standard output of the command on the left directly into the standard input of the command on the right. Here, `ls -la` generates the full detailed directory listing including hidden files, and `head -n 5` receives that stream and outputs only the first 5 lines.

---

### Task 2.4 — Understand package managers
- Checked Homebrew safely without installing or uninstalling anything:
  - `brew --version` reported `Homebrew 7.0.9`.
  - `brew list --formula` listed installed command-line formulas managed by Homebrew (including `ca-certificates`, `ffmpeg`, `gh`, `openssl@4`, etc.).
- **Why package managers are useful:**
  A package manager automates finding, downloading, installing, updating, and removing software from trusted repositories while handling required dependencies automatically. This saves time compared to manually searching for installers and keeps installed tools up to date and consistent across the system.

## 3. Commands / tools used
- `pwd` — Displayed current working directory path.
- `ls`, `ls -l`, `ls -lah` — Listed files with different detail, visibility, and size-formatting options.
- `cd` — Navigated between the repository root and `terminal-practice`.
- `mkdir` — Created the `terminal-practice` directory.
- `touch` — Created an empty file (`sample.txt`).
- `echo` with `>` and `>>` — Created and appended lines to `notes.txt`.
- `cat` — Displayed the text inside `notes.txt`.
- `cp` and `mv` — Created and renamed a backup copy of `notes.txt`.
- `|` and `head -n 5` — Piped detailed listing output to show only the first 5 lines.
- `brew --version` and `brew list --formula` — Inspected Homebrew version and managed packages safely.

## 4. My understanding
The Terminal gives fast, exact control over files and directories using short commands, options (flags), redirection (`>`, `>>`), and pipes (`|`). Working inside a dedicated practice directory and checking `pwd` and `ls` before modifying files keeps operations safe and predictable.

## 5. Difficulties faced
No major difficulties. I stayed careful to use `>>` rather than `>` for the second line so the first line would not be overwritten, and I redacted my local username from saved output.

## 6. How I resolved them
Verified the contents of `notes.txt` immediately with `cat` after each step and replaced local username strings with `[redacted]` before saving evidence.

## 7. Evidence / files
- [README.md](README.md) — Mission 2 tables, answers, and explanations.
- [../terminal-practice/notes.txt](../terminal-practice/notes.txt) — Two-line practice text file.
- [../terminal-practice/notes-archive.txt](../terminal-practice/notes-archive.txt) — Renamed backup copy.
- [../terminal-practice/sample.txt](../terminal-practice/sample.txt) — Empty practice file.
- [../evidence/mission-02-terminal-output.txt](../evidence/mission-02-terminal-output.txt) — Privacy-safe Terminal command output.

## 8. Commit details
- **Commit message:** `Complete Terminal and file management mission`
- **Status:** Committed on `main` and pushed to GitHub.
