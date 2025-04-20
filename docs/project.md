# Project Structure and Tooling

This document provides a simple overview of the project structure, development workflow, and tooling for new developers joining the project.

## Project Structure

The project follows a clean, standard Python package layout:

```
paper-2409.18760-econ/
├── configs/             # Configuration files for simulations
├── data/                # Data storage directory
│   ├── private/         # Private data (not committed)
│   └── public/          # Public datasets
├── docs/                # Documentation
├── notebooks/           # Jupyter notebooks
├── scripts/             # Domain-specific utility scripts
├── src/                 # Source code package
│   ├── calibrate/       # Calibration modules
│   ├── core/            # Core simulation modules
│   │   └── kernels/     # JAX computation kernels
│   ├── data/            # Data processing modules
│   │   └── download/    # Data downloader modules
│   └── utils/           # Utility modules
└── tests/               # Test directory
    ├── e2e/             # End-to-end tests
    ├── stochastic/      # Stochastic simulation tests
    └── unit/            # Unit tests
```

## Development Environment

This project uses Poetry for dependency management and packaging.

### Setting Up

1. Install Poetry (if not already installed):

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies:

   ```bash
   poetry install
   ```

3. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Development Workflow

### Code Quality

- **Formatting code**:

  ```bash
  ruff format src tests scripts
  ```

- **Linting code**:

  ```bash
  ruff check src tests scripts
  ```

- **Running tests**:

  ```bash
  pytest
  ```

- **Running tests with coverage**:

  ```bash
  pytest --cov=src
  ```

- **Running tests in parallel** (faster):
  ```bash
  pytest -xvs -n auto
  ```

### Data Management

- **Download economic data**:
  ```bash
  python -m src.data.download.oecd --country AUT --start 1990
  ```

### Cleaning

- **Clean build artifacts**:
  ```bash
  rm -rf build/ dist/ .pytest_cache/ .ruff_cache/ .coverage htmlcov/
  find . -type d -name "__pycache__" -exec rm -rf {} +
  find . -type d -name "*.egg-info" -exec rm -rf {} +
  find . -type d -name ".eggs" -exec rm -rf {} +
  ```

### Running the Application

- **Run the simulation**:
  ```bash
  python -m src.cli simulate configs/aut.yaml --steps 100 --seed 42
  ```

## Code Quality Tools

The project uses modern Python tooling to maintain code quality:

### Formatting and Linting

- **Ruff**: All-in-one Python linter and formatter (replaces Black)
  - Enforces code style (PEP 8)
  - Manages import sorting
  - Finds code issues and bugs
  - Line length of 88 characters

### Testing

- **pytest**: Testing framework with coverage reporting
- Test markers:
  - `perf`: Performance benchmark tests
  - `calib`: Calibration benchmark tests (skipped by default)

### Pre-commit Hooks

The following checks run automatically before each commit:

- Basic file hygiene (trailing whitespace, EOF)
- YAML/TOML validation
- Notebook output stripping
- Ruff formatting and linting
- Debug statement detection

## Continuous Integration

CI is implemented with GitHub Actions and runs on pushes to main and pull requests:

1. **Linting**: Runs Ruff checks
2. **CPU Testing**: Runs unit, stochastic, and e2e tests (excluding calibration)
3. **GPU Smoke Test**: Tests that the simulation runs on GPU

## Safe Committing Practices

To ensure high-quality commits:

1. Make focused changes addressing a single issue or feature
2. Run tests locally before committing:
   ```bash
   pytest
   ```
3. Let pre-commit hooks run to catch formatting and linting issues
4. Use descriptive commit messages
5. For large changes, create a pull request and request a review

## Working with Notebooks

Notebook outputs are automatically stripped before committing using nbstripout to keep the repository clean and avoid unnecessary diffs.
