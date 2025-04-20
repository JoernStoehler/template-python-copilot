# Template Python Copilot

A github template for python projects, intended to be used with github copilot.

## Quickstart

```bash
git clone git@github.com:JoernStoehler/template-python-copilot.git
cd template-python-copilot

poetry install
pre-commit install
pre-commit run --all-files
```

## Dev Tools And Config

- `.gitignore` preconfigured for python
- `poetry`, `pyproject.toml` for dependency management
- `ruff` for linting and formatting
- `pytest` for unit, integration and end-to-end testing
- `pytest-cov` for code coverage
- `pre-commit`, `.pre-commit-config.yaml` for pre-commit hooks with `--fix` enabled
- `python-dotenv`, `.env`, `.env.example` for environment variables
- `nbstripout` for version control of jupyter notebooks

## Library Stack

- Numerical
  - `jax`
  - `jaxtyping`: type hints for jax
  - `flax`, `optax`: neural network libraries
- CLI and config
  - `python-dotenv`: `.env` support
  - `typer`: CLI
  - `pyyaml`: YAML files
- Visualization
  - `matplotlib`
- Notebooks
  - `ipython`

## Folder structure

```bash
.
├── .vscode/            # vscode settings
│   ├── settings.json
│   └── extensions.json # recommended extensions
├── .github/
│   ├── workflows/
│   │   └── ci.yml
│   └── copilot-instructions.md # automatic custom prompt
├── .gitignore
├── .pre-commit-config.yaml
├── .env
├── .env.example
├── pyproject.toml
├── .venv/ # ignored
├── README.md
├── docs/
│   ├── index.md        # docs/ overview
│   ├── codestyle.md    # code style guide
│   ├── changelog.md    # changelog
│   ├── roadmap.md      # roadmap
│   ├── project.md      # project overview
│   ├── commit.md       # small change checklist
│   └── pullrequest.md  # large change checklist
├── data/               # data files
│   ├── raw/            # raw data
│   ├── processed/      # processed data
│   └── saved/          # saved data
├── src/                # source code
│   ├── __init__.py
│   └── main.py
├── tests/              # test code
│   ├── __init__.py
│   └── test_main.py
├── scripts/            # throwaway scripts
│   └── script.py
└── notebooks/          # jupyter notebooks
    └── notebook.ipynb
```

## Copilot Prompts

- `copilot-instructions.md`: overwritten default prompt, includes a selection of other `.md` files.
- `docs/`: forlder for copilot-consumable documentation, includes:
  - `index.md`: overview of the docs folder, so copilot can find the other files
  - `codestyle.md`: opinionated code style guide
  - `changelog.md`: changelog for cross-session context
  - `roadmap.md`: roadmap for guidance
  - `project.md`: project and folder overview for guidance, instead of README.md
  - `commit.md`: checklist for small changes that are directly committable
  - `pullrequest.md`: checklist for large changes that require a pull request

## Pre-commit hooks

We run `pre-commit` hooks on every commit, including linting and formatting, with `--fix` enabled. After fixes, you need to `git add` and `git commit` again.
This catches many issues from vibe coding early.

## Debugging with Copilot

Claude Sonnet 3.7 tends to use overcomplicated non-standard fixes. If a problem isn't solved after the first try, usually from the second try onwards the code will be ruined.

Instead ask for weblinks to official documentation, search via chatgpt (o4-mini) or google for the solution, copy the page back to copilot and ask it to apply the suggested solution.

Frequent error with Vscode UI: copilot edits a file, but the disk state isn't updated yet until you press "Keep". Various commands like "git add" or "ruff" don't see the changes yet. This especially confuses Claude Sonnet 3.7, as the copilot isn't aware of the disk state.
If you forgot to "Keep" before running a CLI command, just abort and explain:

```markdown
Sorry, I had forgotten to save the file changes before running the command. I saved the file now, please rerun the command and continue.
```
