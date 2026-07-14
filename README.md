# Death Counter

A simple Python utility to keep track of a death count (or any counter) using keyboard hotkeys. Whenever you press `k`, the counter in `DeathCount.txt` increments by 1.

This is extremely useful for stream overlays (e.g., OBS Studio) where you can read `DeathCount.txt` as a text source to display your live death count during gaming streams.

## Features

- **Global Hotkey listener**: Works even when the command line or script window is not focused.
- **Persistent Storage**: Counts are saved in a simple text file (`DeathCount.txt`) which is updated in real time.
- **OBS Integration Ready**: Simply add a text source in OBS and point it to the `DeathCount.txt` file.

## Requirements

The script uses the `keyboard` Python module.

To install it:

```bash
pip install keyboard
```

> [!IMPORTANT]
> On Linux, the `keyboard` library requires root privileges (run with `sudo`) to listen to system-level key events. On Windows, it runs without privileges.

## Usage

1. Initialize or set your initial count in `DeathCount.txt` (defaults to `1` if not created).
2. Run the script:
   ```bash
   python deathCount.py
   ```
3. Press `k` to increment the death count.
