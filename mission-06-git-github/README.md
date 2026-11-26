# Mission 6 — Git and GitHub

## 1. Task / objective
Understand the basic Git staging and committing workflow, create and publish a feature branch (`update-about`) that adds a "My Learning" section to the root `README.md`, open a Pull Request on GitHub into `main`, document branch/PR concepts, and build a personal Git command glossary.

## 2. Work completed

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status** (`git status`) | Shows which branch I am on and lists modified, untracked, or staged files waiting to be committed. |
| **Stage selected changes** (`git add <file>`) | Places specific file edits into the staging area so I can choose exactly what goes into the next snapshot. |
| **Create a commit** (`git commit -m "..."`) | Permanently records the staged changes as a new version in the local repository history with a descriptive message. |
| **View commit history** (`git log --oneline`) | Displays past commits in chronological order along with their commit hashes and messages. |

**Difference between staging (`git add`) and committing (`git commit`):**
Staging (`git add`) prepares and selects which edits should belong to the next snapshot without saving a permanent history entry yet—allowing me to review or include only specific files. Committing (`git commit`) takes everything currently in the staging area and saves it as a permanent, labelled milestone in Git's commit history.

---

### Task 6.2 & Task 6.3 — Create a branch and open a Pull Request
1. Created and switched to a new branch named `update-about` (`git switch -c update-about`).
2. Edited the root `README.md` to add a `## My Learning` section describing three takeaways from Missions 1–5.
3. Checked `git status`, staged `README.md`, committed on `update-about` (`Add My Learning section to root README`), and pushed the branch (`git push -u origin update-about`).
4. Opened **Pull Request #1** on GitHub from `update-about` into `main`:
   - **PR URL:** https://github.com/rohan-bm/digital-detective-8564/pull/1
   - **PR Status:** **Open (not merged)** — Per the assignment rule (*"Merge the PR only if your instructor has asked you to complete the merge"*), the PR has been left open and visible on GitHub for instructor review. Once merged, running `git switch main && git pull origin main` will bring the merged change to local `main`.
5. Switched back to the local `main` branch (`git switch main`) to document and commit Mission 6 cleanly.

**What a branch and a Pull Request are, and why they help collaboration:**
A **branch** is an independent line of development inside a repository that lets someone edit or test changes without altering the stable `main` branch. A **Pull Request (PR)** is a request on GitHub asking to merge changes from one branch into another while showing the exact diff so teammates or reviewers can inspect, comment on, and approve changes before they become part of `main`. Together, branches and PRs let multiple people work simultaneously on different tasks without overwriting each other's work.

---

### Task 6.4 — Git command glossary

| Operation | Command | One-line explanation in your own words |
| :--- | :--- | :--- |
| Initialise a repository | `git init` | Turns the current folder into a new Git repository by creating its tracking metadata. |
| Check status | `git status` | Reports the active branch and which files are untracked, modified, or staged. |
| Stage changes | `git add <file>` | Adds chosen file changes to the staging area in preparation for the next commit. |
| Commit changes | `git commit -m "..."` | Saves all staged changes as a new permanent snapshot in the repository history. |
| View history | `git log` | Lists earlier commits with their IDs, authors, timestamps, and commit messages. |
| Create or list branches | `git branch` | Lists existing branches or creates a new branch pointer at the current commit. |
| Switch branches | `git switch <branch>` | Changes the active branch and updates the working directory files to match it. |
| Publish changes | `git push` | Uploads local commits and branches to a remote repository such as GitHub. |
| Retrieve remote changes | `git pull` | Downloads commits from a remote branch and integrates them into the current local branch. |

## 3. Commands / tools used
- `git status`, `git add`, `git commit`, `git log --oneline` — Practised and verified the core Git staging and commit workflow.
- `git switch -c update-about` / `git switch main` — Created a feature branch and switched between branches.
- `git push -u origin update-about` — Published the `update-about` branch to GitHub.
- `gh pr create` — Opened Pull Request #1 from `update-about` into `main` on GitHub.
- `git branch -a` — Verified local and remote branches.

## 4. My understanding
Version control separates work into deliberate steps: editing in the working directory, selecting changes in the staging area (`git add`), recording milestones (`git commit`), and sharing via branches and Pull Requests (`git push` + PR). This workflow protects `main` from broken edits and makes teamwork organised and reviewable.

## 5. Difficulties faced
No major difficulties. I needed to check carefully whether the Pull Request should be merged immediately or left open for review.

## 6. How I resolved them
Followed the assignment guideline to leave the Pull Request open unless instructed to merge, documented its exact URL and `Open` status here, and switched back to `main` before committing Mission 6.

## 7. Evidence / files
- [README.md](README.md) — Git workflow explanations, branch/PR status, and command glossary.
- [../evidence/mission-06-git-output.txt](../evidence/mission-06-git-output.txt) — Privacy-safe Git branch, commit, and PR log.
- GitHub Branch `update-about` and Pull Request #1: https://github.com/rohan-bm/digital-detective-8564/pull/1

## 8. Commit details
- **Commit message:** `Complete Git and GitHub collaboration mission`
- **Status:** Committed on `main` and pushed to GitHub.
