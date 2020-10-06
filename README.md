# Check pipx outdates

## What it does
check what pipx installed top level packages are outdated.

Mostly educational/casual, for reference only.

Demostrates threading, asyncio with subprocess.

DO NOT USE IN PRODUCTION OR ANYTHING SERIOUS !

## Usage
Recommand run as module.
```
python3 -m check_pipx_oudates
# or
python3 -m check_pipx_oudates async
# or
python3 -m check_pipx_oudates thread
# or
python3 -m check_pipx_oudates sync
# or
python3 -m check_pipx_oudates help
```
Or just use the `run-{async,threads,sync}.py` script

## Personal Notes
How I run it:
```
# ~/.bashrc
alias check-pipx-outdates="cd ~/SCRIPTS/check_pipx_oudates/ ; py.exe -m check_pipx_oudates ; cd -"

```

## Todo
- Check injected packages as well
