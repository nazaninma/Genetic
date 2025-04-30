# Genetic
# Genetic Programming Project 

This repository contains the implementation of a Genetic Programming (GP) system developed for the "Artificial Intelligence and Expert Systems" course. The main objective is to approximate mathematical functions using symbolic regression via genetic programming techniques.

## 🧠 Project Objective

Use Genetic Programming to evolve symbolic expressions (trees) that approximate a target mathematical function based on a given set of input-output training points.

---

## 📁 Project Structure

- `main.py`: Core implementation of the GP system.
- `data/`: Includes training and testing datasets (if applicable).


---

## 🔧 Key Components

- **Operators**: Binary (`+`, `-`, `*`, `/`, `^`) and Unary (`sin`, `cos`, `sqrt`)
- **Fitness Function**: Mean Squared Error (MSE) between predicted and true outputs.
- **Accuracy Metric**:  
  \[
  \text{Accuracy Percentage} = \left(1 - \frac{\text{MSE}}{\text{Variance of True Outputs}}\right) \times 100
  \]
- **Initialization**: Random tree generation with function and terminal sets.
- **Selection**: Based on fitness proportion.
- **Crossover & Mutation**: Tree-based genetic operators.
- **Termination**: Based on maximum generations or satisfactory fitness.

---

## 🧪 Experiments

Three separate test cases were executed:
1. Simple quadratic function (e.g., \( y = x^2 \))
2. Piecewise function using conditional logic
3. Multi-variable symbolic expressions (for dimensionality > 1)

Each experiment includes:
- Function details
- Graph of the best individual per generation
- MSE and accuracy metrics

---

## 📊 Visualization

Plots generated include:
- Fitness over generations
- Evolved expression tree structures (optional)
- Comparison between true vs predicted outputs

---

## 📌 Requirements

- Python 3.7+
- `numpy`
- `matplotlib`

To install dependencies and Run:
```bash
pip install -r requirements.txt
python main.py


