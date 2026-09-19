# Factory Reallocation & Shipping Optimization Recommendation System

## Nassau Candy Distributor

A machine-learning and decision-intelligence project designed to identify potential factory reassignment opportunities and evaluate their modeled impact on order-to-ship lead time.

---

## Business Problem

Leadership's central question is:

> What should we change to improve performance?

Traditional descriptive analysis can explain what happened, but leadership also needs to understand what could happen if factory assignments were changed.

This project therefore develops a scenario-based decision-intelligence framework to:

- Predict shipping outcomes under different factory configurations.
- Simulate alternative factory assignments.
- Identify products that may benefit from reassignment.
- Consider lead-time improvement, profitability, and factory distance.
- Apply an evidence safeguard before recommending operational changes.

---

## Project Objectives

The system was designed to:

1. Analyze historical order and shipping data.
2. Calculate observed order-to-ship lead time.
3. Build machine-learning models to predict lead-time outcomes.
4. Simulate alternative factory assignments.
5. Compare current and alternative factory scenarios.
6. Rank potential opportunities using business criteria.
7. Classify products into actionable recommendation categories.
8. Summarize factory-level movement opportunities.

---

## Dataset

The analysis used a project-provided Nassau Candy Distributor dataset containing:

- 10,194 order-line records
- 18 original variables
- 15 products
- 5 factories in the scenario framework

Key variables include:

- Order Date
- Ship Date
- Product Name
- Sales
- Units
- Gross Profit
- Cost
- Region
- Division
- Ship Mode
- Factory assignment

The original dataset is not included in this public repository.

---

## Methodology

The project follows this workflow:

```text
Raw Data
   ↓
Data Preparation
   ↓
Lead-Time Analysis
   ↓
Feature Engineering
   ↓
Machine Learning
   ↓
Alternative Factory Scenario Simulation
   ↓
Product-Level Evaluation
   ↓
Business Scoring
   ↓
Evidence Safeguard
   ↓
Factory Movement Recommendations
   ↓
Business Impact Analysis
