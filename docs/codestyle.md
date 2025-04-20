# Code Style Guide

This document outlines the coding standards and conventions used in this project to ensure consistency and maintainability.

## Python Style

We follow a consistent Python coding style based on standard practices and enforced through Ruff:

### General Principles

- Code readability is a top priority
- Explicit is better than implicit
- Simple is better than complex
- Flat is better than nested

### Formatting

- Line length: 88 characters max
- Indentation: 4 spaces (no tabs)
- Use double quotes (`"`) for strings by default
- Line breaks occur before binary operators
- Use trailing commas in multi-line structures

### Naming Conventions

- `snake_case` for functions, methods, and variables
- `PascalCase` for classes
- `UPPER_CASE` for constants
- Avoid single-letter variable names except in cases like mathematical formulas or simple loops

Examples:

```python
# Good
def calculate_interest_rate(principal, time_period, risk_factor):
    return principal * ANNUAL_RATE * time_period * risk_factor

# Avoid
def calcRate(p, t, r):
    return p * ar * t * r
```

### Imports

Imports are grouped and sorted automatically by Ruff in this order:

1. Standard library imports
2. Related third-party imports
3. Local application imports

```python
# Standard library
import os
import sys
from pathlib import Path

# Third-party
import numpy as np
import jax
import jax.numpy as jnp
import jax.random

# Local
from src.core import agents
from src.utils import metrics
```

### JAX-specific Guidelines

- Always use `jnp` instead of `np` in computation code
- Prefer JAX transformations over manual loops
- Use explicit typing with jaxtyping to annotate both types and shapes:

  ```python
  from jaxtyping import Float, Int, Bool, Array, PyTree

  def update_state(state: Float[Array, "n_agents"], params: dict) -> Float[Array, "n_agents"]:
      return jnp.where(state > 0, state + params["delta"], state)
  ```

- Use explicit typing for intermediate variables where the shape might be unclear:

  ```python
  def process_agent_data(data: Float[Array, "n_agents features"]) -> Float[Array, "n_agents"]:
      # Using type annotation for clarity on intermediate calculation
      weights: Float[Array, "features"] = jnp.array([0.1, 0.2, 0.7])
      return jnp.dot(data, weights)
  ```

- Use JAX's PRNG system consistently:
  ```python
  def initialize_agents(key: jax.random.PRNGKey, n_agents: int) -> tuple[Float[Array, "n_agents 2"], Float[Array, "n_agents"]]:
      key1, key2 = jax.random.split(key)
      positions: Float[Array, "n_agents 2"] = jax.random.uniform(key1, (n_agents, 2))
      values: Float[Array, "n_agents"] = jax.random.normal(key2, (n_agents,))
      return positions, values
  ```

## Documentation

### Docstrings

Use Google-style docstrings for all public functions, classes, and methods:

```python
def calculate_welfare(income: jax.Array, consumption: jax.Array, beta: float) -> float:
    """Calculates welfare based on income and consumption.

    Args:
        income: Array of agent incomes
        consumption: Array of agent consumption values
        beta: Discount factor

    Returns:
        Aggregate welfare value

    Raises:
        ValueError: If income or consumption arrays have different shapes
    """
    if income.shape != consumption.shape:
        raise ValueError("Income and consumption must have the same shape")

    utility = jnp.log(consumption)
    return jnp.sum(utility) + beta * jnp.sum(jnp.log(income))
```

### Comments

- Use comments to explain "why", not "what"
- Keep comments up-to-date with code changes
- Consider whether a comment could be made unnecessary with clearer code

## Testing

- Every module should have corresponding tests
- Test both success paths and edge cases
- Use descriptive test names that explain the behavior being tested:

  ```python
  def test_market_clearing_reaches_equilibrium():
      # Test code

  def test_market_clearing_handles_zero_supply():
      # Test code
  ```

## Best Practices

### Data Structures

- Use typed dataclasses for complex data structures:
  ```python
  @dataclass
  class Agent:
      id: int
      wealth: float
      productivity: float
      employed: bool = False
  ```

### Error Handling

- Use specific exception types
- Provide clear error messages
- Fail fast: validate inputs early

### Performance

- Profile before optimizing
- Vectorize operations using JAX
- Use `jit`, `vmap`, and `pmap` for performance-critical code:

  ```python
  @jax.jit
  def update_all_agents(agents, environment):
      return agents.map(lambda a: update_agent(a, environment))
  ```

- Use `@partial(jax.vmap)` instead of writing functions with batched inputs:
  ```python
  @partial(jax.vmap, in_axes=(0, None))
  def update_agent(agent: Agent, environment: Environment) -> Agent:
      # Update logic
      return agent
  ```

## Project-Specific Conventions

### Economic Variables

- Use consistent naming for economic variables across modules:
  - `w`: wage
  - `p`: price
  - `r`: interest rate
  - `y`: output/income
  - `c`: consumption

### File Organization

- One class per file for major components
- Group related functions in thematic modules
- Keep internal implementation details in `_private.py` modules
