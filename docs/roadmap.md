# Project Roadmap: Reproducing Wiese et al. (2024) - Paper 2409.18760

## 1. Goal

The primary goal is to reproduce the key findings of the Wiese et al. (2024) paper. This involves implementing the described data-driven agent-based model (ABM), calibrating it using the specified Bayesian methods, and validating its out-of-sample forecasting performance against the IIASA and AR(1) benchmarks for a selection of OECD countries, using the provided project infrastructure.

## 2. Guiding Principles

- **Modularity:** Build components corresponding to agents, markets, and mechanisms described in the paper, leveraging the existing project structure.
- **Test-Driven Development:** Implement comprehensive tests (unit, integration, stochastic, end-to-end) at each stage.
- **Fail-Fast & Incremental Complexity:** Start with a minimal viable model and incrementally add features and complexity, testing thoroughly at each step.
- **Leverage Existing Infrastructure:** Utilize the specified Python, JAX, Poetry, Ruff, and pytest stack.

## 3. Key Model Components (Based on Wiese et al. 2024)

- **Agents:** Individuals, Households, Firms, Banks, Central Bank, Government, Rest of the World (RoW). [See Overview](paper/0_overview_agents_markets.md)
- **Markets:** Goods, Labour, Credit, Housing. [See Overview](paper/0_overview_agents_markets.md), [See Market Clearing](paper/5_markets_clearing.md)
- **Key Mechanisms:** Housing market dynamics, enhanced credit market, realistic synthetic populations, specific behavioral rules, stock-flow consistency. [See Agent Details](paper/1_firms.md), [See Household/Individual Details](paper/2_households_individuals.md), [See Bank Details](paper/3_banks.md)
- **Calibration:** Approximate Bayesian Inference (NPE/NRE). [See Calibration Details](paper/7_calibration_validation.md)
- **Data:** OECD, IMF, World Bank, BIS, ECB HFCS, Compustat. [See Overview](paper/0_overview_agents_markets.md)

## 4. Milestones

### M0: Basic Infrastructure & Core Components (Foundation)

- **Goal:** Set up the core data structures, base classes for agents and markets, a minimal simulation loop, and basic data loading for one agent type. Ensure JAX integration works.
- **Features:**
  - Define base `Agent` and `Market` classes (`src/core/`).
  - Implement basic `Firm` agent class structure (`src/core/`). [See Firm Details](paper/1_firms.md)
  - Implement `GoodsMarket` placeholder (`src/core/`). [See Market Clearing](paper/5_markets_clearing.md)
  - Implement basic simulation scheduler (`src/core/`).
  - Implement initial data loading for Firms (`src/data/`).
  - Set up basic JAX kernel structure (`src/core/kernels/`).
- **Testing Focus:** Unit tests for base classes, Firm structure, data loading utility. Basic JAX function test.
- **Uncertainties:** Complexity of initial JAX setup within the project structure.

### M1: Single Market Simulation (Goods Market)

- **Goal:** Implement a functioning Goods Market with `Firm` and `RestOfTheWorld` agents, including basic production, pricing, inventory, and matching logic. Test basic stock-flow consistency.
- **Features:**
  - Implement simplified `Firm` production & pricing (`src/core/kernels/`). [See Firm Details](paper/1_firms.md)
  - Implement `RestOfTheWorld` agent (`src/core/`). [See RoW Details](paper/8_rest_of_world.md)
  - Implement `GoodsMarket` clearing logic (`src/core/kernels/`). [See Market Clearing](paper/5_markets_clearing.md)
  - Implement `Firm` inventory/stock tracking (`src/core/kernels/`). [See Firm Details](paper/1_firms.md)
- **Testing Focus:** Unit tests for Firm updates, RoW logic, GoodsMarket clearing. Stochastic tests for basic market price/quantity dynamics. Stock-flow consistency checks.
- **Uncertainties:** Efficiency of the first JAX-based market clearing implementation.

### M2: Multi-Agent, Multi-Market Simulation (Adding Households, Labour Market)

- **Goal:** Integrate `Household` and `Individual` agents, implement the `LabourMarket`, and establish interactions between the Goods and Labour markets.
- **Features:**
  - Implement `Individual` & `Household` agent classes (`src/core/`). [See Household/Individual Details](paper/2_households_individuals.md)
  - Implement data loading for Households/Individuals (`src/data/`).
  - Implement `LabourMarket` class & clearing logic (`src/core/kernels/`). [See Market Clearing](paper/5_markets_clearing.md)
  - Link Labour Market outcomes (employment, wages) to Firm capacity & Household income (`src/core/kernels/`).
  - Implement basic Household consumption affecting Goods Market demand (`src/core/kernels/`). [See Household/Individual Details](paper/2_households_individuals.md)
  - Refine Firm production based on labour inputs (`src/core/kernels/`). [See Firm Details](paper/1_firms.md)
- **Testing Focus:** Unit tests for Household/Individual updates, LabourMarket. Integration tests for Goods+Labour market interactions (e.g., wage changes affecting consumption).
- **Uncertainties:** Managing agent heterogeneity efficiently in JAX. Complexity of inter-market feedback loops.

### M3: Financial Layer (Banks, Credit Market)

- **Goal:** Introduce `Bank` agents and the `CreditMarket`, enabling basic Firm and Household lending and defaults.
- **Features:**
  - Implement `Bank` agent class (`src/core/`). [See Bank Details](paper/3_banks.md)
  - Implement data loading for Banks (`src/data/`).
  - Implement `CreditMarket` class & clearing logic (`src/core/kernels/`). [See Market Clearing](paper/5_markets_clearing.md)
  - Implement Firm & Household loan demand (`src/core/kernels/`). [See Firm Details](paper/1_firms.md), [See Household/Individual Details](paper/2_households_individuals.md)
  - Implement loan issuance, repayment, interest calculations, and basic default mechanics affecting balance sheets (`src/core/kernels/`). [See Bank Details](paper/3_banks.md)
  - Implement basic Firm & Bank bankruptcy logic (`src/core/kernels/`). [See Firm Details](paper/1_firms.md), [See Bank Details](paper/3_banks.md)
- **Testing Focus:** Unit tests for Bank updates, CreditMarket logic, loan functions. Integration tests involving defaults and their impact on other agents/markets.
- **Uncertainties:** Stability of default cascades. Complexity of implementing bank lending rules accurately.

### M4: Advanced Features (Housing Market, Government, Full Behavioral Rules)

- **Goal:** Complete the model by adding the `HousingMarket`, `Government`, `CentralBank`, and implementing the detailed behavioral rules from the paper.
- **Features:**
  - Implement `HousingMarket` class & clearing (`src/core/kernels/`). [See Market Clearing](paper/5_markets_clearing.md)
  - Implement Household housing decisions & mortgage integration (`src/core/kernels/`). [See Household/Individual Details](paper/2_households_individuals.md)
  - Implement `Government` agent (taxes, benefits, consumption) (`src/core/`). [See CB/Gov Details](paper/4_central_bank_government.md)
  - Implement `CentralBank` agent (Taylor rule) (`src/core/`). [See CB/Gov Details](paper/4_central_bank_government.md)
  - Refine _all_ agent behavioral rules to match paper specifications (`src/core/kernels/`). [See Agent Details](paper/1_firms.md), [See Household/Individual Details](paper/2_households_individuals.md), [See Bank Details](paper/3_banks.md), [See Expectations](paper/6_expectations.md)
  - Implement full data initialization pipeline (`src/data/`).
- **Testing Focus:** Unit tests for new agents/market. Comprehensive integration tests for all components. End-to-end simulation runs for short periods, checking for plausible outputs.
- **Uncertainties:** Interaction complexity between all markets (esp. housing/credit). Data availability/consistency for all required variables across countries. Stability of the housing market sub-model.

### M5: Calibration & Validation (Single Country)

- **Goal:** Implement the NPE/NRE calibration pipeline and replicate the paper's forecasting validation for one key country (e.g., Austria).
- **Features:**
  - Implement NPE/NRE framework (`src/calibrate/`). [See Calibration Details](paper/7_calibration_validation.md)
  - Define priors for the 7 key parameters (`configs/`, `src/calibrate/`). [See Calibration Details](paper/7_calibration_validation.md)
  - Implement simulation execution for calibration data generation (`scripts/`, `src/cli`).
  - Implement summary statistics calculation (`src/calibrate/` or `src/utils/`).
  - Run calibration for Austria.
  - Implement AR(1) benchmark model (`src/calibrate/` or separate module).
  - Implement or obtain results for the IIASA benchmark model (**Dependency:** Requires access/reimplementation). [See Calibration Details](paper/7_calibration_validation.md)
  - Perform out-of-sample forecasting runs (`scripts/`, `src/cli`).
  - Calculate RMSE & Bayes Factors; compare with paper results (`notebooks/` or `scripts/`). [See Calibration Details](paper/7_calibration_validation.md)
- **Testing Focus:** Validation tests comparing generated forecasts & metrics against the paper's results for Austria. Stochastic tests for calibration robustness.
- **Uncertainties:** Calibration runtime and convergence. Reproducibility of IIASA results. Stability and accuracy of NPE/NRE implementation. Feasibility of Bayes Factor calculation.

### M6: Scalability & Generalization

- **Goal:** Ensure the model can be run, calibrated, and validated for multiple OECD countries efficiently.
- **Features:**
  - Refactor data loading & configuration for multi-country support (`src/data/`, `configs/`, `scripts/download.py`).
  - Optimize JAX kernels (`jit`, `vmap`, `pmap`) for performance (`src/core/kernels/`).
  - Run calibration & validation for a larger set of OECD countries.
  - Analyze cross-country results and compare with paper (`notebooks/`). [See Calibration Details](paper/7_calibration_validation.md)
- **Testing Focus:** Performance benchmarks. Cross-country result validation against paper appendices.
- **Uncertainties:** Computational resources required. Potential data gaps or model instability specific to certain countries.

## 5. Potential Challenges & Mitigations

- **Model Complexity:** The ABM has many interacting parts. Mitigation: Strict modularity, comprehensive testing at each milestone, incremental feature addition using the detailed markdown files.
- **Data Management:** Acquiring, cleaning, and integrating data for 38 countries is demanding. Mitigation: Robust data loading scripts (`src/data/`), start with one country, automate downloads, document data sources clearly.
- **Calibration Intensity:** Bayesian methods (NPE/NRE) are computationally heavy. Mitigation: Efficient JAX implementation (`src/calibrate/`, `src/core/kernels/`), leverage parallelization, potentially start with smaller agent populations for initial calibration tests. Acknowledge potential prior sensitivity.
- **JAX Learning Curve:** Requires specific coding practices. Mitigation: Ensure team familiarity, utilize type hinting (`jaxtyping`), test JAX components early (M0/M1).
- **IIASA Benchmark Replication:** May require reimplementation based on paper descriptions if original code is unavailable. Mitigation: Allocate specific time for understanding and implementing the IIASA model structure and rules as a separate task if needed. Treat as a potential risk/dependency.

## 6. Review Points

Please review this updated roadmap and the accompanying detail files. Key points for review remain:

- **Feasibility & Granularity:** Is the breakdown suitable for development?
- **Prioritization & Testing:** Is the focus clear?
- **Dependencies/Risks:** Are key risks (IIASA replication, calibration, data) appropriately highlighted?
- **Assumptions:** Are there unstated or risky assumptions?
