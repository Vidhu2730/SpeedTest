# Speed Net

A Python internet speed test app with download, upload, and ping metrics.

## Setup

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell blocks activation scripts, run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then open a new PowerShell window and activate the environment again.

## Run

Command-line speed test:

```powershell
python main.py
```

Desktop window speed test:

```powershell
python internet.py
```

Alternative desktop window entrypoint:

```powershell
python speed_test_app.py
```
