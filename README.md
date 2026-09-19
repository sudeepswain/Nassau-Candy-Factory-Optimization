# Nassau Candy Factory Reallocation & Shipping Optimization

## 📌 Project Overview

This project develops a **machine learning and decision-intelligence system** to identify potential factory reallocation opportunities for Nassau Candy Distributor.

The central business question is:

> **What should we change to improve shipping performance while considering profitability and factory distance?**

The project combines historical shipping data, machine learning, scenario simulation, and business rules to identify products that may benefit from being reassigned from their current factory to an alternative factory.

---

## 🎯 Business Objectives

The system is designed to:

* Predict shipping outcomes under different factory configurations.
* Evaluate alternative factory assignments for products.
* Identify products with potential lead-time improvements.
* Consider profitability and factory-to-factory distance.
* Apply evidence safeguards before making operational recommendations.
* Provide an executive-level recommendation framework.

---

## 📊 Dataset

The project uses the Nassau Candy Distributor dataset.

### Dataset characteristics

* **Records:** 10,194
* **Original variables:** 18
* **Products:** 15
* **Factories:** 5

The original dataset contains information related to:

* Orders
* Products
* Order and ship dates
* Shipping modes
* Customer locations
* Sales
* Units
* Gross profit
* Cost

> **Note:** The original CSV dataset is not included in this public repository.

---

## 🔍 Analytical Approach

The project follows a decision-intelligence workflow:

```text
Historical Data
      ↓
Data Preparation
      ↓
Lead-Time Analysis
      ↓
Machine Learning
      ↓
Factory Scenario Simulation
      ↓
Product-Level Analysis
      ↓
Business Scoring
      ↓
Evidence Safeguards
      ↓
Final Recommendations
```

---

## 🧹 Data Preparation

The analysis includes:

* Date parsing and validation.
* Calculation of observed order-to-ship lead time.
* Feature engineering from order dates.
* Product, factory, region, shipping mode, and division features.
* Preparation of machine-learning features.
* Factory-distance calculations using the project factory information.

The observed lead time is calculated as:

**Lead Time = Ship Date − Order Date**

The dataset contains unusually long observed lead times, so these values are preserved rather than treated as conventional transportation transit times.

---

## 🤖 Machine Learning

Three regression models were evaluated:

| Model             |    MAE |   RMSE |     R² |
| ----------------- | -----: | -----: | -----: |
| Linear Regression | 212.67 | 264.27 |  0.012 |
| Random Forest     | 218.28 | 269.50 | -0.027 |
| Gradient Boosting | 214.61 | 260.27 |  0.042 |

**Gradient Boosting** was selected for scenario simulation because it produced the lowest RMSE among the tested models.

### Model performance

* **MAE:** 214.61 days
* **RMSE:** 260.27 days
* **R²:** 0.042

The relatively low R² means the model explains only a small portion of the observed lead-time variation. Therefore, scenario results are treated as **screening opportunities rather than guaranteed operational outcomes**.

---

## 🔄 Factory Scenario Simulation

Each observed product/order line was evaluated against alternative factories.

The scenario analysis generated:

**40,776 scenario records**

These scenarios compare:

* Current factory
* Alternative factory
* Predicted current lead time
* Predicted alternative lead time
* Potential lead-time improvement
* Product-level sales and profit
* Factory-to-factory distance

The scenario unit is the **dataset line item**, rather than the unique Order ID, because a single order can contain multiple product lines.

---

## 📈 Recommendation Framework

The project evaluates each product/factory combination using three main considerations:

### 1. Lead-Time Improvement

Measures the modeled reduction in lead time when moving a product to an alternative factory.

### 2. Profitability

Considers the total gross profit associated with the product/factory combination.

### 3. Factory Distance

Considers the distance between the current and alternative factories.

The analytical score uses the following weights:

```text
Optimization Score =
    50% Lead-Time Score
  + 30% Profit Score
  - 20% Distance Score
```

These weights are **business assumptions used for the project**, not an objectively optimal weighting.

---

## 🛡️ Evidence Safeguard

To avoid treating small samples as operationally proven recommendations, recommendations are classified using the number of observed orders.

| Evidence        | Orders | Interpretation           |
| --------------- | -----: | ------------------------ |
| HIGHER EVIDENCE |   100+ | Larger observed sample   |
| MEDIUM EVIDENCE |  30–99 | Moderate observed sample |
| LOW EVIDENCE    |    <30 | Requires validation      |

Positive opportunities with fewer than 30 observed orders are classified as:

**VALIDATE FIRST**

This means they should be investigated further before any operational change.

---

## 💡 Final Recommendations

The final analysis covers all **15 products**.

| Recommendation | Products |
| -------------- | -------: |
| MOVE CANDIDATE |        8 |
| VALIDATE FIRST |        5 |
| NO CHANGE      |        2 |

### MOVE CANDIDATE products

The products classified as MOVE CANDIDATE are:

* Kazookles
* Wonka Gum
* Wonka Bar - Fudge Mallows
* Wonka Bar -Scrumdiddlyumptious
* Wonka Bar - Nutty Crunch Surprise
* Wonka Bar - Milk Chocolate
* Lickable Wallpaper
* Wonka Bar - Triple Dazzle Caramel

These should be interpreted as **modeled opportunities for further operational evaluation**, not guaranteed improvements.

---

## 🏭 Factory Movement Opportunities

The analysis identified four factory movement patterns among the MOVE CANDIDATE products:

1. **Lot's O' Nuts → Wicked Choccy's**
2. **Wicked Choccy's → The Other Factory**
3. **Secret Factory → Wicked Choccy's**
4. **The Other Factory → Wicked Choccy's**

The largest modeled opportunity was:

### Lot's O' Nuts → Wicked Choccy's

* **Products:** 3
* **Orders:** 5,692
* **Potential modeled order-days reduced:** 60,824.73
* **Average modeled lead-time improvement:** 0.80%

---

## 📊 Overall Business Impact

For the MOVE CANDIDATE products:

* **Products:** 8
* **Orders covered:** 10,154
* **Potential modeled order-days reduced:** 82,263.98
* **Modeled average reduction:** 8.10 days per order
* **Associated sales:** 141,356.15
* **Associated gross profit:** 93,158.07

These values represent **potential modeled impact**, not guaranteed savings or operational results.

---

## ⚠️ Limitations

Several limitations should be considered before implementing the recommendations.

### Model limitations

The Gradient Boosting model achieved an R² of approximately **0.042**, indicating limited explanatory power.

Therefore:

* Predictions should not be interpreted as highly accurate forecasts.
* Scenario results should be treated as screening tools.
* Operational decisions should be validated using additional business data.

### Data limitations

The dataset contains unusually long order-to-ship intervals.

The analysis therefore preserves these values as observed lead times rather than assuming they represent conventional transportation transit times.

### Scenario limitations

The factory reassignment analysis is based on modeled counterfactual scenarios.

A predicted improvement does not prove that physically moving production will produce the same result.

### Business constraints not fully modeled

Future versions could incorporate:

* Factory production capacity
* Inventory availability
* Transportation costs
* Service-level requirements
* Customer priority
* Factory operating costs
* Product manufacturing constraints
* Minimum order quantities
* Actual production and transportation lead times

---

## 🚀 Future Improvements

Future versions of the system could include:

1. More operational data.
2. Factory capacity constraints.
3. Transportation costs.
4. Inventory and production constraints.
5. More advanced optimization techniques.
6. A formal mathematical optimization model.
7. A dashboard for scenario exploration.
8. A/B or pilot testing of selected factory reallocations.
9. Continuous monitoring of actual versus predicted performance.

---

## 📁 Repository Structure

```text
Nassau-Candy-Factory-Optimization/
│
├── README.md
├── requirements.txt
│
├── notebooks/
│   ├── README.md
│   └── Nassau_Candy_Factory_Optimization.ipynb
│
├── data/
│   └── README.md
│
├── outputs/
│   ├── README.md
│   └── Nassau_Candy_Final_Recommendations.csv
│
└── presentation/
    └── Nassau_Candy_Project_Presentation.pptx
```

---

## 🛠️ Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Google Colab
* GitHub

---

## 📌 Project Outcome

This project demonstrates how historical operational data can be transformed into a **decision-intelligence workflow**.

Instead of only describing historical shipping performance, the system evaluates:

> **What could happen if products were reassigned to different factories?**

The resulting framework combines machine learning, scenario analysis, business scoring, and evidence safeguards to identify potential factory reallocation opportunities for further validation.

---

## 👤 Project Deliverables

The repository contains:

* Google Colab analysis notebook
* Final recommendation output
* Project methodology
* Python dependency list
* Project presentation
* Executive-level recommendations

---

## ⚠️ Important Interpretation Note

The recommendations in this project are analytical outputs based on historical data and a predictive model.

They should be considered **decision-support recommendations**, not guaranteed operational outcomes.
