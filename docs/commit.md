# Commit Guidelines

This document provides guidelines for making effective commits to the project.

## Commit Philosophy

Good commits are:

- **Focused**: Address one thing at a time
- **Complete**: Leave the codebase in a working state
- **Clear**: Have descriptive messages that explain the change
- **Tested**: Include tests for new or modified functionality

## When to Commit

Commit your changes whenever you've completed a logical unit of work, such as:

- Adding or fixing a feature
- Refactoring a piece of code
- Updating documentation
- Fixing a bug

Commit early and often, rather than making large, monolithic changes.

## Commit Message Guidelines

Follow this format for commit messages:

```
<type>: <short summary>

<optional detailed description>
```

Types include:

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting changes
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `perf`: Performance improvements
- `test`: Adding missing tests
- `chore`: Changes to the build process or auxiliary tools

Examples:

```
feat: add market clearing algorithm to goods market

fix: correct wage calculation in labor market
```

## Files to Update with Commits

In addition to your code changes, consider updating these files:

1. **docs/changelog.md**:

   - Update when adding significant features, fixing bugs, or making breaking changes
   - Add a bullet point under the "Unreleased" section

2. **docs/roadmap.md**:

   - Update when completing milestones or changing project direction
   - Mark completed items or adjust timelines

3. **docs/project.md**:
   - Update only when changing project structure or development workflows

Do NOT update these files for routine commits (small bugfixes, minor refactorings).

## Pre-Commit Checklist

Before committing changes:

1. **Run tests**:

   ```bash
   pytest
   ```

2. **Check formatting and linting**:

   ```bash
   ruff format src tests scripts
   ruff check src tests scripts
   ```

3. **Ensure your code passes pre-commit hooks**:

   ```bash
   pre-commit run --all-files
   ```

4. **Verify your changes work as expected**:
   - For features: verify functionality works
   - For bug fixes: verify the issue is resolved
   - For refactoring: verify no functionality has changed

## After Committing

After making your commit:

1. Pull latest changes from the main branch
2. Resolve any conflicts
3. Push your changes
4. For larger changes, consider [creating a pull request](pullrequest.md)
