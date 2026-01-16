# Algorithmic Thinking for Statistical Code

**Language**: Theory
**Time Estimate**: 3-4 hours
**Notion Source**: [Link](https://www.notion.so/2dc342cf7cc88040aa44c1326ebbf73c)

## Learning Objectives

By the end of this lesson, you should be able to:

- [ ] Math to Computation Translation
- [ ] Estimators as Reductions
- [ ] Simulation as Pipelines
- [ ] Data Representation and Memory Intuition
- [ ] Invariants and Correctness Conditions
- [ ] Numerical Robustness and Stability
- [ ] Performance Workflow

## Sections

### Core Mental Models

How to translate mathematical notation into efficient, correct code.

### Statistical Algorithm Patterns

Common patterns in statistical computing:
- Streaming/online algorithms
- Divide-and-conquer
- Dynamic programming
- Monte Carlo methods

### Tradeoff Playbook

When to choose:
- Accuracy vs speed
- Memory vs computation
- Simplicity vs optimization

### Micro-Drills

Quick exercises to build intuition.

### Oral Defense Add-On

Preparation for oral defense questions.

## Exercises

### Foundational

| ID | Title | Description |
|----|-------|-------------|
| F1 | Log-sum-exp stable computation | Implement numerically stable log-sum-exp |
| F2 | Running mean and variance (Welford) | Implement Welford's online algorithm |
| F3 | Discrete distribution sampling | Sample from a discrete distribution |

### Proficiency

| ID | Title | Description |
|----|-------|-------------|
| P1 | Pairwise Euclidean distances without loops | Vectorized pairwise distance computation |
| P2 | Reservoir sampling | Implement reservoir sampling for streams |
| P3 | Solve Ax=b without explicit inversion | Use decomposition instead of inversion |

### Mastery

| ID | Title | Description |
|----|-------|-------------|
| M1 | Kahan summation | Implement compensated summation |
| M2 | Stable softmax | Numerically stable softmax implementation |
| M3 | Iterative refinement for ill-conditioned systems | Improve solutions to ill-conditioned systems |
| M4 | Alias method for O(1) sampling | Implement Walker's alias method |

## Next Steps

Proceed to [Day 1: Functions, Modules, and Idiomatic Python](../../week1/day-01/README.md).
