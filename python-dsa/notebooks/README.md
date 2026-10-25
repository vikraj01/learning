# Python notebooks

Each notebook is one lesson: an explanation, code you run yourself, then tasks and a quiz that checks your answers.

| # | Notebook | You'll be able to |
| --- | --- | --- |
| 1 | `01-run-python.ipynb` | run code, print things, read an error |

Answers are in `solutions/`. Try each task yourself first.

## Start the notebooks

### The first time only

1. Install **uv**. It's a tool that installs Python and everything the notebooks need, so you don't have to do it by hand.

   On Linux or Mac, in a terminal:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   On Windows, in PowerShell:

   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

   Close the terminal and open a new one, so it finds `uv`.

2. Get this repo, if you don't have it yet:

   ```bash
   git clone https://github.com/vikraj01/learning.git
   ```

### Every time

Go into the repo folder and start Jupyter:

```bash
cd learning
make notebooks
```

No `make` on your laptop? This does the same thing:

```bash
uv run jupyter lab --notebook-dir=python-dsa/notebooks
```

The first time it downloads a few things, so give it a minute. Then your browser opens with the list of notebooks on the left. Double-click `01-run-python.ipynb` to open it.

Keep the terminal open while you work. Closing it stops Jupyter.

### When you're done

1. Save with **Ctrl + S**.
2. In the terminal, press **Ctrl + C**, then type `y` and press Enter.

## Getting new notebooks

When new notebooks are added, get them with:

```bash
git pull
```
