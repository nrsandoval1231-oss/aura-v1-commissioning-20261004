# Aura disposable live proof

Synthetic greeting example used only to exercise Aura's live build, tests,
independent validation, pull request, merge, and authoritative confirmation.

`greet(name)` returns a greeting, such as `greet("Ada") == "Hi, Ada."`.
`multiply(a, b)` returns the product of its arguments, such as
`multiply(3, 4) == 12`. Negative numbers and zero are supported.

Run the unittest suite from the repository directory in PowerShell using the
configured Python executable:

```powershell
& "C:/Users/nrsan/.codex/worktrees/aura-adaptive-v1/Aura/.venv/Scripts/python.exe" -B -m unittest -v
```
