## Error 1
### Duplicate file 
Date: 7/21/26
Task: Create a file C:\Dev\Projects\coding-year-one\labs\02_shift_greeting.py
Expected: C:\Dev\Projects\coding-year-one\labs\02_shift_greeting.py
Actual/error: C:\Users\User\labs\02_shift_greeting.py
Root cause: Current directory was set to C:\Users\User causing it to createa duplicate file under User
Fix: Change the current directory to C:\Dev\Projects\coding-year-one
Prevention: Check that the PowerShell prompt ends in coding-year-one before using a relative path; use pwd if uncertain.
pwd = pwd means print working directory. The working directory is the same as the current directory.
In PowerShell, pwd is a short alias for Get-Location. It displays your current location but does not change it: