# Credit Risk Classification with Neural Networks

## Overview

Developed a neural network model to predict loan repayment status (Paid, Current, Risky) using LendingClub’s dataset of ~2.3M loans. Engineered a robust preprocessing pipeline and achieved 96.69% accuracy and 94.87% macro F1-score, with a strong 0.8928 F1-score for the Risky class.

## Dataset

Source: LendingClub loan data (~2.3M samples).

Features: 59 after preprocessing (e.g., loan amount, FICO scores, debt-to-income ratio).

Classes: Paid (~47.7%), Current (~38.8%), Risky (~13.4%, combining Charged Off/Default and Delinquent).
## Challenges and Insights

Data Preprocessing: Handled NaN values and unmapped statuses with robust checks, ensuring data integrity for ~2.3M loans.

Pipeline Complexity: Engineered a custom preprocessing pipeline to manage 59 features, streamlining data preparation.


Insight: Combining domain knowledge, rigorous preprocessing, and weighted loss was critical for high performance on imbalanced data.

## Files

### data/:

how to load data.py: Script to load and preprocess LendingClub data.



data_cleaning.xlsx: Documentation of data cleaning variables.



data_information.xlsx: Summary of dataset features and characteristics.



### model/:

best_model.pth: Saved weights of the trained neural network model.



### notebook/:


credit_loan_classification.ipynb: Main notebook with preprocessing, training, and evaluation (achieving 96.69% accuracy).

credit_loan_optuna.ipynb: Experimental notebook with Optuna hyperparameter optimization.



### report/:

confusion_matrix.png: Visualization of test set predictions.
initial_report.htm.zip: Initial data analysis report before cleaning.
updated_report.html: Updated report after data cleaning.




### LICENSE: MIT License for the project.


## Future Work

Explore ensemble models (e.g., combining neural networks with Random Forest).

Incorporate temporal features (e.g., loan age) for dynamic risk prediction.
## Key Results
| Metric | Value | Significance |
|--------|-------|--------------|
| **Overall Accuracy** | 96.69% | Outperforms baseline models by >12% |
| **Minority Class Recall (risky_statuses)** | 90.19% | Captures 9/10 high-risk cases |
| **Weighted F1-Score** | 96.70% | Robust performance across classes |
| **Macro F1-Score** | 94.87% | Strong balance considering imbalance |

### Detailed Performance

````text
                precision    recall  f1-score   support

  paid_statuses     0.9936    0.9967    0.9951    215748
 current_status     0.9634    0.9529    0.9581    175664
 risky_statuses     0.8839    0.9019    0.8928     60722

      accuracy                         0.9669    452134
     macro avg     0.9469    0.9505    0.9487    452134
  weighted avg     0.9671    0.9669    0.9670    452134

    

