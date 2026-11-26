# Mission 3 — Understand the operating system

## 1. Task / objective
Explore the operating system environment, active user identity (redacted), available disk storage, running processes and PIDs, absolute vs. relative file paths, file permissions, and core responsibilities of an operating system.

## 2. Work completed

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** (`sw_vers`, `uname -sm`) | Identifies the OS name, version, build, kernel, and CPU architecture. | `macOS 27.2.1` (Build `26B131`), kernel `Darwin`, architecture `arm64`. |
| **Current account identity** (`whoami`) | Shows which user account owns the current Terminal session and determines file access rights. | Active user account is `[redacted]` (standard non-root user). |
| **Available and used storage** (`df -h /`) | Shows total disk capacity, used space, and remaining free space on mounted storage volumes. | Root volume `/dev/disk3s1s1` has `926Gi` total capacity and `816Gi` available. |
| **System activity snapshot** (`ps -eo pid,pcpu,pmem,comm`) | Lists currently running programs along with their PID, CPU %, memory %, and executable path. | Saw background system processes such as `launchd` (PID `1`, `0.3%` CPU) and `logd` (PID `339`, `0.8%` CPU). |

---

### Task 3.2 — Understand processes
- **What is a process?**
  A process is an active instance of a program currently loaded into memory and running on the computer, complete with its own memory space and system resources.
- **What does the PID column represent?**
  `PID` stands for **Process Identifier**, a unique number assigned by the operating system to track and manage each running process (for example, `1` for `/sbin/launchd`).
- **Two examples of processes running on my computer:**
  1. `launchd` (PID `1`) — macOS background service manager that starts and supervises system services.
  2. `logd` (PID `339`) or an open application such as `Terminal` / a web browser — handles system logging or user applications.

---

### Task 3.3 — Understand paths and permissions
- **Absolute path vs. relative path:**
  An **absolute path** starts from the root directory `/` and specifies the exact location of a file or folder regardless of where you currently are in the Terminal. A **relative path** describes the location starting from your current working directory.
  - **Absolute path example (privacy-safe):** `/Users/[redacted]/.../digital-detective-8564/terminal-practice/notes.txt`
  - **Relative path example (from inside `digital-detective-8564`):** `terminal-practice/notes.txt` (or `../terminal-practice/notes.txt` when inside `mission-03-operating-system/`).
- **File permissions inspection (`ls -l terminal-practice/notes.txt`):**
  The listing showed `-rw-r--r--@`.
  - The leading `-` means it is a regular file.
  - The next three characters `rw-` belong to the **owner**:
    - `r` (Read): **Yes** — the owner can open and read the file.
    - `w` (Write): **Yes** — the owner can modify or save changes to the file.
    - `-` (Execute): **No** — execute permission is not set, because it is a plain text file rather than a runnable program or script.

| Permission | Meaning | Example |
| :--- | :--- | :--- |
| `r` — Read | Allows a file's contents to be read. | Opening `notes.txt` with `cat`. |
| `w` — Write | Allows a file to be changed. | Appending a line to `notes.txt`. |
| `x` — Execute | Allows a file to be run; on a directory, allows access/traversal. | Running a script or entering a folder with `cd`. |

---

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | Starts, schedules, pauses, and terminates running programs so multiple tasks can share the CPU smoothly. | Assigning CPU time to both a web browser and background `logd` using PIDs. |
| **Memory management** | Allocates RAM to active programs, keeps each program's memory isolated, and frees memory when programs close. | Giving RAM to a text editor while preventing it from overwriting another app's data. |
| **Device management** | Communicates with hardware peripherals through drivers so apps can use them without knowing low-level hardware details. | Handling keyboard typing, trackpad movement, and screen rendering. |
| **File management** | Organises data into folders and files on storage drives and tracks file paths, sizes, and timestamps. | Storing `notes.txt` inside `terminal-practice/` on the SSD. |
| **User interface / shell** | Provides a way for users to interact with the computer visually (GUI) or via text commands (CLI). | Using macOS Finder windows or typing commands in `zsh` inside Terminal. |
| **Security and permissions** | Controls which users and programs can read, write, or execute files and restricts administrative actions. | Enforcing `rw-r--r--` so only the owner can edit `notes.txt` while blocking unauthorized access. |

## 3. Commands / tools used
- `sw_vers` and `uname -sm` — Inspected macOS version, kernel, and CPU architecture.
- `whoami` — Checked the active user identity (output redacted in documentation).
- `df -h /` — Checked disk size, used space, and available storage in human-readable units.
- `ps -eo pid,pcpu,pmem,comm` — Displayed running processes with PID, CPU usage, memory usage, and command name.
- `cd` and `pwd` — Practised navigating between the repository root and subfolder paths.
- `ls -l` — Viewed detailed file permissions for `terminal-practice/notes.txt`.

## 4. My understanding
The operating system acts as the coordinator between user applications and physical hardware. Through process scheduling (tracked by PIDs), hierarchical paths (absolute and relative), and permission bits (`r`, `w`, `x`), the OS keeps multiple programs running safely without interfering with each other's memory or files.

## 5. Difficulties faced
No major difficulties. I needed to make sure no personal details such as my account username or machine name were copied into the documentation or evidence file.

## 6. How I resolved them
Replaced personal username details with `[redacted]` in the saved output and tables while keeping the real command structure and observations accurate.

## 7. Evidence / files
- [README.md](README.md) — Mission 3 notes, observations, and OS responsibility tables.
- [../evidence/mission-03-os-output.txt](../evidence/mission-03-os-output.txt) — Privacy-safe OS and process output.

## 8. Commit details
- **Commit message:** `Document operating system and file management`
- **Status:** Committed on `main` and pushed to GitHub.
