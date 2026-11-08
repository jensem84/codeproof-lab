# Safe GitHub publication — Windows PowerShell

Nothing in this package has been published. Do not publish until you have personally reviewed every file and confirmed independent ownership.

1. Create a **new personal** GitHub repository named `codeproof-lab` (private initially), without initializing README/license remotely.
2. In PowerShell, from the extracted project folder, run:

```powershell
git init
git branch -M main
git status --short
git add .
git diff --cached --stat
git diff --cached --check
git commit -m "Initialize independent CodeProof Lab MVP"
git remote add origin https://github.com/YOUR-USERNAME/codeproof-lab.git
git remote -v
git push -u origin main
```

3. Confirm remote points to **your personal repository**, not an organization or RAAA repository, before pushing.
4. Keep private until reviewed: inspect Git history, secret scanning, licensing, and any company IP overlap. Change visibility only when you explicitly decide to.
5. Never paste tokens, credentials, or proprietary source into README, issues, commits, or AI chats.

## Optional preflight

```powershell
python -m pytest -q
python -m ruff check src tests
git status --short
```

Do not assert Alignerr eligibility before written approval. Do not sign a contributor agreement without examining pre-existing IP and transcript rights.
