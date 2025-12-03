# AI Ethics Assignment - Fairness Audit with COMPAS

## Description
This repository contains a practical audit of the COMPAS recidivism dataset using IBM's AI Fairness 360 toolkit. The goal is to identify bias in AI predictions and demonstrate mitigation strategies.

## Folder Structure

AI-Ethics-Assignment/

├── notebooks/

│ └── COMPAS_Bias_Audit.ipynb

├── src/

│ └── fairness_audit.py

├── data/

│ └── compas_dataset.csv

├── diagrams/

│ └── bias_visualizations.txt

└── README.md


## Tools & Libraries
- Python 3.x
- pandas, matplotlib
- AI Fairness 360

## Instructions
1. Place `compas_dataset.csv` in the `data/` folder.
2. Run the audit script: `python src/fairness_audit.py`
3. Open Jupyter notebook for visualizations and step-by-step analysis: `notebooks/COMPAS_Bias_Audit.ipynb`

## Key Metrics
- Disparate Impact
- Equal Opportunity Difference

## Ethical Principles Applied
- Justice: Fair distribution of outcomes
- Non-maleficence: Avoiding harm to unprivileged groups
- Transparency & Explainability: Clear reporting of bias metrics

## Author
Nazarine Wasonga

