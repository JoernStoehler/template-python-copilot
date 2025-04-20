# Pull Request Guidelines

This document outlines the process for submitting and reviewing larger changes through pull requests.

## When to Use a Pull Request

Create a pull request when:

- Implementing a significant new feature
- Making architectural changes
- Refactoring large portions of code
- Changing core functionality
- Introducing breaking changes

For smaller changes, a direct commit to the main branch may be sufficient. See [commit guidelines](commit.md) for those cases.

## Creating a Pull Request

### 1. Prepare Your Changes

- Create a new branch from the main branch with a descriptive name:

  ```bash
  git checkout -b feature/descriptive-name
  ```

- Make your changes in small, logical commits (see [commit guidelines](commit.md))
- Keep your PR focused on a single objective

### 2. Test Your Changes

Before submitting a PR, ensure:

- All tests pass:
  ```bash
  pytest -xvs
  ```
- Code is properly formatted and linted:
  ```bash
  ruff format src tests scripts
  ruff check src tests scripts
  ```
- Pre-commit hooks pass:
  ```bash
  pre-commit run --all-files
  ```
- New functionality has appropriate tests

### 3. Update Documentation

Update the following as appropriate:

- Add new tests for your changes
- Update docstrings for modified functions and classes
- Update CHANGELOG.md with a summary of changes
- Update roadmap.md if completing planned features
- Add or update any relevant examples

### 4. Submit Your Pull Request

- Push your branch to the remote repository:
  ```bash
  git push -u origin feature/descriptive-name
  ```
- Create a pull request on GitHub
- Fill out the PR template with:
  - Clear description of changes
  - References to related issues
  - Any breaking changes
  - Testing instructions

## PR Description Template

```markdown
## Description

Brief description of the changes

## Related Issues

Fixes #123
Related to #456

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing Instructions

1. Step-by-step instructions to test the changes

## Checklist

- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
```

## Review Process

### For Reviewers

When reviewing a PR:

1. Check that it follows coding standards in [codestyle.md](codestyle.md)
2. Verify all tests pass and cover the new functionality
3. Ensure documentation is updated appropriately
4. Test the functionality if possible
5. Provide constructive feedback

### For PR Authors

When your PR is being reviewed:

1. Respond to feedback promptly
2. Make requested changes in new commits
3. Explain your reasoning when disagreeing with feedback
4. Rebase and squash commits before final merge if requested

## After Approval

Once approved:

1. Rebase on the latest main branch if needed
2. Merge your PR (or let the reviewer do it)
3. Delete the feature branch when no longer needed
