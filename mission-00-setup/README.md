# Mission 0 — Create your GitHub workspace

## 1. Task / objective
Create a correctly named local project folder and public GitHub repository (`digital-detective-8564`), verify that Python 3 and Git are installed, prepare the required mission folder structure, write the root `README.md` and Mission 0 `README.md`, and push the initial setup commit to GitHub.

## 2. Work completed
- **Repository name:** `digital-detective-8564` (using the assignment name + last four digits of my USN `8564`).
- **Tools checked and versions:**
  - Python 3: `Python 3.13.15`
  - Git: `git version 2.54.0 (Apple Git-157)`
- **Folders and files created:**
  - `README.md` (root project overview and mission index)
  - `mission-00-setup/README.md`
  - `mission-01-computer-basics/README.md`
  - `mission-02-terminal/README.md`
  - `mission-03-operating-system/README.md`
  - `mission-04-programs/README.md`
  - `mission-05-numbers-data/README.md` and `mission-05-numbers-data/number_converter.py`
  - `mission-06-git-github/README.md`
  - `mission-07-networking/README.md`
  - `mission-08-final-report/README.md`
  - `evidence/.gitkeep`
- Initialised Git in the local project folder, created the public repository `digital-detective-8564` on GitHub, and pushed the initial commit.

## 3. Commands / tools used
- `python3 --version` — Checked the installed Python 3 version.
- `git --version` — Checked the installed Git version.
- `mkdir` / file creation — Created the project directory, mission folders, and initial placeholder files.
- `git init -b main` — Initialised a new Git repository using `main` as the default branch.
- `git add` and `git commit` — Staged and recorded the initial folder structure and setup files.
- `gh repo create digital-detective-8564 --public --source=. --remote=origin --push` — Created the public GitHub repository and pushed the `main` branch.

## 4. My understanding
A **repository** is a project folder tracked by a version control system (Git) that stores both the project files and the complete history of changes made to them. Hosting the repository on GitHub makes that tracked history available online so it can be reviewed, shared, and backed up.

Organising the folder structure by mission keeps each topic separate and tidy from the beginning. Instead of mixing unrelated notes, scripts, and outputs in the root directory, each mission has its own dedicated folder and `README.md`, which makes progress easier to follow and check.

## 5. Difficulties faced
No major difficulties. I had to make sure not to create a separate default `README.md` on GitHub while creating the remote repository so it would not conflict with the local `README.md`.

## 6. How I resolved them
I prepared the local `README.md` and mission folders first, then created an empty public repository on GitHub and pushed the local `main` branch directly.

## 7. Evidence / files
- [../README.md](../README.md)
- [README.md](README.md)
- Empty starter files for Missions 1–8 and `evidence/.gitkeep`

## 8. Commit details
- **Commit message:** `Set up Digital Detective mission structure`
- **Status:** Committed on `main` and pushed to GitHub (`https://github.com/rohan-bm/digital-detective-8564`).
