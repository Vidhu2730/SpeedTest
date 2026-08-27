# Speed Net

A Python internet speed test app with both a command-line mode and a Kivy desktop GUI. It checks download speed, upload speed, and ping metrics.

## What it includes

- `main.py`: command-line speed test
- `internet.py`: desktop GUI speed test
- `speed_test_app.py`: alternate desktop GUI entrypoint
- `speed_core.py`: shared speed-test logic

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
