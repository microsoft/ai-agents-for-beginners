---
description: 'Cherrypick a file deleted from the given commit between branches using Git.'
mode: 'agent'
---

# Cherry-picking a File Between Branches Using Git

Your goal is to cherry-pick a specific file deleted from a given commit between branches in a Git repository. Use the Git command line interface to accomplish this task.

## Inputs

- **Commit Hash**: $COMMIT - The hash of the commit from which to cherry-pick the file.
- **File Path**: $FILE_PATH - The path of the file to be cherry-picked.

If you don't have the commit hash or file path, please ask the user for these details.

## Instructions

1. **Identify the Commit**: Determine the commit hash from which you want to cherry-pick the file.
2. **Cherry-pick the File**: Use the `git checkout` command to cherry-pick the specific file from the identified commit. If the file doesn't exist in the given commit, find the closest commit where the file exists.
3. **Commit the Changes**: Ask the user to stage and commit the changes to finalize the cherry-pick.