# lab04-Edamame
Lab 4 Group Work: Collaborating on a Shared GitHub Repository

### Who Did What Table

| Member | GitHub Username | File |
|---|---|---|
| Han Htoo Aung | Erics12487254 | test_shared.py |
| Kaung Myat Tun | Kaungmyattun8 | test_withdraw.py |
| Lwin Oo | lwinDoubleOmega | bank.py |
| Lwin Oo | lwinDoubleOmega | conftest.py |
| Lwin Oo | lwinDoubleOmega | .gitignore |
| Ngyein Chan Ko | Reka1X | test_teardown.py |
| Wathan Htat | callmefrost27-dotcom | test_deposit.py |

### Our Merge Conflits
the following is the conflict we had when we tried to push. 

### Conflict History

| Conflict | Reason |
|---|---|
| Conflict 1 | Concurrent edits to the placeholder line and the new member table row. |
| Conflict 2 | Group header formatting conflicted with the pytest execution instructions. |
| Conflict 3 | Documentation lines conflicted with the 4th member's row and withdraw test information. |
| Conflict 4 | Local conflict explanations conflicted with the 5th member's row and shared fixture test information. |

### Git Contribution Summary

| Contributions | Name |
|---:|---|
| 10 | Lwin Oo |
| 8 | Ngyein Chan Ko |
| 4 | Erics12487254 |
| 4 | Wathan Htat |
| 3 | Kaungmyattun8 |

### Reflection Questions

### 1. Why was your push rejected, and how did you fix it?

Our push was rejected because the remote repository contained changes that were not in our local branch. We fixed the issue by running `git pull --rebase` to integrate the remote changes before pushing again.

---

### 2. Why could Git not resolve the README conflict automatically?

Git could not resolve the conflict because different team members edited the same section of `README.md`. We had to review the conflicting changes manually and decide which content to keep.

---

### 3. What is the difference between committing and pushing?

- **Committing** saves a snapshot of our changes in the local Git repository.
- **Pushing** uploads those committed changes to the remote GitHub repository.

---

### 4. How do fixtures reduce duplicated setup code in tests?

Fixtures provide reusable setup code that can be shared across multiple tests. This prevents us from repeating the same setup steps in every test and makes the test files cleaner and easier to maintain.