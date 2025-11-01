# BankAppProject

This repository contains a small Flask application. The `app.py` module was adjusted so that `auto_push.auto_push()` is only executed when running the module directly. This prevents side-effects during import (for tests, tooling, and WSGI servers).

## Setup (Windows PowerShell)

1. Create a virtual environment (if you don't already have one):

```powershell
python -m venv venv
```

2. Activate the venv:

```powershell
# PowerShell
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Run the app:

```powershell
# This will run auto_push.auto_push() as a side-effect
python app.py
```

5. Run tests:

```powershell
# uses unittest discovery
python -m unittest discover -v
```

## Notes

- If you run `import app` from other modules, `auto_push.auto_push()` will not run (it's guarded by `if __name__ == '__main__'`).
- `requirements.txt` contains pinned versions detected in the current environment. Update as needed.
