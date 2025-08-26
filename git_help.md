# Safely Using Git

---

## `Less` Navigation

Before we begin, it's helpful to know how to navigate the output of commands that use `less` (like `git log`). There are a few key commands:
* `Space`: Move down one page
* `b`: Move up one page
* `q`: Quit and return to the command line
* `/search_term`: Search for a term (press `n` to go to the next occurrence)

To permanently turn of the `less` pager for Git commands, you can run:
```bash
git config --global core.pager cat
```


## The Golden Rule: Always Check First

Before you run a command that makes changes, get a clear picture of your repository's state.

* `git status`: This is your best friend and the **safest command in Git**. It's purely informational. It tells you which branch you're on, if you have uncommitted changes, and whether you're ahead of or behind the remote branch. Run it often!
* `git diff`: Shows the exact changes you've made to your files that haven't been staged yet.
    - Note: If you have a lot of changes, `git diff` can produce a lot of output. You can limit it to specific files by running `git diff <file>`.
* `git diff --staged`: Shows the changes you've staged (added) and are ready to be committed.

---

## A Safe Daily Workflow

Here are the essential commands for your day-to-day work, broken down by what they do.

### 1. Syncing with Your Team (Safely)

Before you start writing code, you want the latest changes from the remote repository.

* **The Safe Way:**
    1.  `git fetch`: This command **downloads** all the new changes from the remote (`origin`) but **does not** touch your local files or your current branch. It's like getting the latest newspaper delivered but not reading it yet. It's 100% safe.
    2.  `git status`: After a fetch, `git status` will tell you if your local branch is behind the remote one (e.g., `Your branch is behind 'origin/main' by 3 commits`).
    3.  `git merge`: If you're behind, run this to apply the downloaded changes to your local branch. This is the point where you might have to resolve merge conflicts.

* **The Common Way (Slightly Less Control):**
    * `git pull`: This command is actually a combination of `git fetch` and `git merge` in one step. It's very common, but it immediately tries to merge the changes, which can sometimes be surprising. Using `fetch` first gives you a chance to see what's coming before you merge it.

### 2. Saving Your Work

As you finish a piece of work, you'll save it with commits.

1.  `git add <file>` or `git add .`: This command takes your changes from the working directory and puts them into the **staging area**. Think of the staging area as a box where you place all the changes you want to include in your next snapshot (commit). Using `.` adds all modified files in the current directory and subdirectories.
2.  `git commit -m "Your descriptive message"`: This takes everything in the staging area and saves it as a permanent snapshot with the message you provide. The `-m` flag lets you write the message directly in the command. If you omit it, Git will open your default text editor to write a longer message.

### 3. Sharing Your Work

Once you have one or more local commits, you can share them with your team.

* `git push`: This **uploads** your committed changes to the remote repository (e.g., GitHub, GitLab). If other people have pushed changes since your last pull, Git will reject your push and tell you to pull first. This is a crucial safety feature that prevents you from accidentally overwriting a teammate's work.

---

## How to Undo Mistakes ⏪

It's common to need to undo something. Here are the safe ways to do it.

* **To unstage a file:** If you used `git add` on a file by mistake but want to keep the changes.
    ```bash
    git restore --staged <file>
    ```

* **To discard local changes:** If you want to completely throw away changes in a file and revert it to how it was after your last commit. ⚠️ **This is destructive**, so be sure you don't need the changes.
    ```bash
    git restore <file>
    ```

* **To undo your last commit:** If you just committed something but want to undo it. The `--soft` flag undoes the commit but leaves your changes staged, ready for you to re-commit.
    ```bash
    git reset --soft HEAD~1
    ```

By sticking to this workflow and always using `git status` to check your bearings, you'll be using the command line safely and efficiently.


# Overview of Terminology

* Fetch: This command retrieves updates from a remote repository but does not merge them into your current branch. It allows you to see what changes are available without applying them.

* Merge: This command integrates changes from one branch into another. Typically, you would merge a feature branch into the main branch once development is complete.

* Pull: This command is a combination of fetch and merge. It retrieves updates from a remote repository and automatically merges them into your current branch. Essentially, it’s how you get the latest changes and incorporate them into your work.

* Push: This command uploads your local changes to a remote repository. When you push, you’re sending your commits from your local branch to a branch in the remote repository, making your changes available to others.

* Stash: This command temporarily saves changes in your working directory that you aren’t ready to commit yet. It allows you to revert your working directory to a clean state while preserving your changes for later use.

* Commit: This command saves your changes to the local repository. Each commit is a snapshot of your project at a specific point in time and includes a message describing the changes made.

* Branch: A branch is a separate line of development in your project. It allows you to work on features or fixes without affecting the main codebase until you’re ready to merge them back in.

* Rebase: This command allows you to move or combine a sequence of commits to a new base commit. It’s often used to keep a clean project history by linearizing the commit history.

* Clone: This command creates a local copy of a remote repository, including all its files, history, and branches. It’s how you start working on an existing project.

* Remote: This refers to a version of your repository that is hosted on the internet or another network. Commonly, this is where you push and pull changes.

* Checkout: This command switches your working directory to a different branch or commit. It allows you to work on different features or versions of your project.

* Diff: This command shows the differences between various versions of files or branches. It’s useful for reviewing changes before committing or merging.