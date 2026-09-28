# lab04-Edamame
Lab 4 Group Work: Collaborating on a Shared GitHub Repository

### 2. Who Did What Table

| Member | GitHub Username | File |
|---|---|---|
| Han Htoo Aung | Erics12487254 | test_shared.py |
| Kaung Myat Tun | Kaungmyattun8 | test_withdraw.py |
| Lwin Oo | lwinDoubleOmega | bank.py |
| Lwin Oo | lwinDoubleOmega | conftest.py |
| Lwin Oo | lwinDoubleOmega | .gitignore |
| Ngyein Chan Ko | Reka1X | test_teardown.py |
| Wathan Htat | callmefrost27-dotcom | test_deposit.py |

### 3. Our Merge Conflits
the following is the conflict we had when we tried to push. 

### Conflict History

| Conflict | Reason |
|---|---|
| Conflict 1 | Concurrent edits to the placeholder line and the new member table row. |
| Conflict 2 | Group header formatting conflicted with the pytest execution instructions. |
| Conflict 3 | Documentation lines conflicted with the 4th member's row and withdraw test information. |
| Conflict 4 | Local conflict explanations conflicted with the 5th member's row and shared fixture test information. |

### 4. Git Contribution Summary

| Contributions | Name |
|---:|---|
| 10 | Lwin Oo |
| 8 | Ngyein Chan Ko |
| 4 | Erics12487254 |
| 4 | Wathan Htat |
| 3 | Kaungmyattun8 |

### 5. Reflection Questions

1. Why was your push rejected, and how did you fix it?
Our push was rejected because the remote repository had changes that were not in our local branch. We fixed it by pulling the changes with git pull --rebase and then pushing again.

2. Why could Git not resolve the README conflict automatically?
Git could not resolve the conflict because different team members changed the same parts of README.md. We had to manually review the changes and decide what content to keep.

3. What is the difference between committing and pushing?
Committing saves our changes to the local Git repository, while pushing uploads the committed changes to the remote GitHub repository.

4. How do fixtures reduce duplicated setup code in tests?
Fixtures provide reusable setup code that can be used by multiple tests. This avoids writing the same setup code repeatedly for each test.