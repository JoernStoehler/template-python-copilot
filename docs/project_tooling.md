# Project Tooling

This document provides a concise overview of the tooling, configuration files, and libraries used in this project.

## Configuration Files

| File                      | Purpose                                           |
|---------------------------|---------------------------------------------------|
| `pyproject.toml`          | Project metadata and Poetry dependency management |
| `ruff.toml`               | Ruff linter and formatter configuration           |
| `.pre-commit-config.yaml` | Pre-commit hooks configuration                    |
| `.env`                    | Environment variables (not in version control)    |
| `.env.example`            | Template for environment variables                |
| `.gitignore`              | Files excluded from version control               |
| `.editorconfig`           | Editor formatting settings                        |
| `.vscode/settings.json`   | VS Code editor settings                           |
| `.vscode/extensions.json` | VS Code recommended extensions                    |
| `.github/workflows/ci.yml`| GitHub Actions CI configuration                   |

## Development Tools

### Package and Dependency Management
- Poetry v1.7+

### Code Quality
- Ruff v0.4+ (linting and formatting, 88 char line length, py312)
- pre-commit v3.7+
- nbstripout v0.6+

### Testing
- pytest v8.0+
- pytest-cov v4.1+
- pytest-xdist v3.5+

### Environment Management
- python-dotenv v1.1+

## Library Stack

### Numerical and Machine Learning
- JAX v0.4+
- JAXtyping v0.3+
- Flax v0.8+
- Optax v0.2+

### CLI and Configuration
- Typer v0.9+
- PyYAML v6.0+

### Data Processing
- Pandas v2.2+

### Visualization
- Matplotlib v3.8+

### Development Experience
- IPython v8.18+

## CI/CD
- GitHub Actions (linting, testing, coverage)

## How to Update Tooling

### Updating Dependencies

```bash
# View outdated dependencies
poetry show --outdated

# Update all dependencies
poetry update

# Update specific dependencies
poetry update package1 package2
```

### Updating Configuration

- **Ruff**: Update rules and settings in `ruff.toml`
- **Pre-commit**: Update hook versions in `.pre-commit-config.yaml`
- **Poetry**: Update dependencies in `pyproject.toml`

### Adding New Tools

1. Add the tool to Poetry dependencies:
   ```bash
   poetry add tool-name
   # or for dev dependencies:
   poetry add --group dev tool-name
   ```

2. Create a configuration file if needed
3. Update relevant documentation (this file and others)
4. Consider adding to pre-commit hooks if applicable
