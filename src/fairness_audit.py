import pandas as pd
from aif360.datasets import BinaryLabelDataset
from aif360.metrics import ClassificationMetric
from aif360.algorithms.preprocessing import Reweighing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv('../data/compas_dataset.csv')

# Example: select relevant columns
cols = ['age', 'sex', 'race', 'priors_count', 'c_charge_degree', 'two_year_recid']
df = df[cols]

# Convert to BinaryLabelDataset
dataset = BinaryLabelDataset(
    df=df,
    label_names=['two_year_recid'],
    protected_attribute_names=['race']
)

# Train-test split
train, test = dataset.split([0.7], shuffle=True)

# Apply reweighing to mitigate bias
RW = Reweighing(protected_attribute_names=['race'], privileged_groups=[{'race':1}], unprivileged_groups=[{'race':0}])
RW.fit(train)
train_transf = RW.transform(train)

# Train simple logistic regression
X_train = train_transf.features
y_train = train_transf.labels.ravel()
model = LogisticRegression(solver='liblinear')
model.fit(X_train, y_train)

# Evaluate fairness metrics
preds = model.predict(test.features)
test_pred_dataset = test.copy()
test_pred_dataset.labels = preds

metric = ClassificationMetric(test, test_pred_dataset,
                              unprivileged_groups=[{'race':0}],
                              privileged_groups=[{'race':1}])

print("Disparate Impact:", metric.disparate_impact())
print("Equal Opportunity Difference:", metric.equal_opportunity_difference())
