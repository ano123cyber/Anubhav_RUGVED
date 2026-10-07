import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 1. LOAD THE DATASET
df = pd.read_csv("co2(1).csv")
print("First 5 rows:")
print(df.head())
print("\nShape of dataset:")
print(df.shape)
print("\nColumn names:")
print(df.columns)
print("\nDataset information:")
df.info()
print("\nStatistical summary:")
print(df.describe())


# 2. DATA CLEANING

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows before cleaning:")
print(df.duplicated().sum())

text_columns = df.select_dtypes(include="object").columns

for column in text_columns:
    df[column] = df[column].str.lower().str.strip()

df = df.drop_duplicates()

print("\nShape after cleaning:")
print(df.shape)

print("\nDuplicate rows after cleaning:")
print(df.duplicated().sum())

# 3. BASIC EDA
co2 = df["CO2 Emissions(g/km)"]
print("\nCO2 Emissions Statistics:")
print("Mean:", np.mean(co2))
print("Minimum:", np.min(co2))
print("Maximum:", np.max(co2))

# 4. HISTOGRAM OF CO2 EMISSIONS
plt.figure(figsize=(8, 5))
plt.hist(co2, bins=30)
plt.xlabel("CO2 Emissions (g/km)")
plt.ylabel("Number of Vehicles")
plt.title("Distribution of CO2 Emissions")
plt.show()


# 5. CORRELATION

correlation = df.corr(numeric_only=True)

print("\nCorrelation Matrix:")
print(correlation)


# 6. LINEAR REGRESSION
#     Engine Size -> CO2 Emissions

X = df["Engine Size(L)"].values
Y = df["CO2 Emissions(g/km)"].values

X_mean = np.mean(X)
Y_mean = np.mean(Y)

slope = np.sum((X - X_mean) * (Y - Y_mean)) / \
        np.sum((X - X_mean) ** 2)

intercept = Y_mean - slope * X_mean

print("\nLinear Regression:")
print("Slope:", slope)
print("Intercept:", intercept)

Y_pred = slope * X + intercept


# 7. LINEAR REGRESSION GRAPH

sort_index = np.argsort(X)

X_sorted = X[sort_index]
Y_pred_sorted = Y_pred[sort_index]

plt.figure(figsize=(8, 5))

plt.scatter(X, Y, alpha=0.5, label="Actual Data")

plt.plot(
    X_sorted,
    Y_pred_sorted,
    linewidth=2,
    label="Regression Line"
)

plt.xlabel("Engine Size (L)")
plt.ylabel("CO2 Emissions (g/km)")
plt.title("Linear Regression: Engine Size vs CO2 Emissions")

plt.legend()

plt.show()


# 8. LINEAR REGRESSION EVALUATION

MAE = np.mean(np.abs(Y - Y_pred))

MSE = np.mean((Y - Y_pred) ** 2)

RMSE = np.sqrt(MSE)

SS_total = np.sum((Y - Y_mean) ** 2)

SS_residual = np.sum((Y - Y_pred) ** 2)

R2 = 1 - (SS_residual / SS_total)

print("\nLinear Regression Evaluation:")
print("MAE:", MAE)
print("MSE:", MSE)
print("RMSE:", RMSE)
print("R2 Score:", R2)


# 9. LOGISTIC REGRESSION
# CO2 emissions are continuous, so we create:
# 0 = Low CO2
# 1 = High CO2
# using the median CO2 value as the threshold.

threshold = df["CO2 Emissions(g/km)"].median()
df["High_CO2"] = (
    df["CO2 Emissions(g/km)"] > threshold
).astype(int)
print("\nCO2 Classification Threshold:")
print("Median CO2:", threshold)
print("\nClass distribution:")
print(df["High_CO2"].value_counts())

# 10. PREPARE DATA FOR LOGISTIC REGRESSION

X_logistic = df["Engine Size(L)"].values
Y_logistic = df["High_CO2"].values
X_mean = np.mean(X_logistic)
X_std = np.std(X_logistic)

X_scaled = (X_logistic - X_mean) / X_std


# 11. SIGMOID FUNCTION

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 12. LOGISTIC REGRESSION USING GRADIENT DESCENT

logistic_slope = 0
logistic_intercept = 0

learning_rate = 0.01
iterations = 1000

for i in range(iterations):

    z = logistic_slope * X_scaled + logistic_intercept

    probability = sigmoid(z)

    slope_gradient = np.mean(
        (probability - Y_logistic) * X_scaled
    )

    intercept_gradient = np.mean(
        probability - Y_logistic
    )

    logistic_slope = (
        logistic_slope -
        learning_rate * slope_gradient
    )

    logistic_intercept = (
        logistic_intercept -
        learning_rate * intercept_gradient
    )


print("\nLogistic Regression:")
print("Slope:", logistic_slope)
print("Intercept:", logistic_intercept)

# 13. LOGISTIC REGRESSION PREDICTIONS

probability = sigmoid(
    logistic_slope * X_scaled +
    logistic_intercept
)

prediction = (probability >= 0.5).astype(int)


# 14. LOGISTIC REGRESSION ACCURACY

accuracy = np.mean(
    prediction == Y_logistic
)

print("\nLogistic Regression Accuracy:")
print(accuracy)


# 15. LOGISTIC REGRESSION GRAPH

sort_index = np.argsort(X_logistic)

X_sorted = X_logistic[sort_index]
probability_sorted = probability[sort_index]

plt.figure(figsize=(8, 5))

plt.scatter(
    X_logistic,
    Y_logistic,
    alpha=0.4,
    label="Actual Classes"
)

plt.plot(
    X_sorted,
    probability_sorted,
    linewidth=2,
    label="Logistic Regression"
)

plt.xlabel("Engine Size (L)")
plt.ylabel("Probability / Class")
plt.title("Logistic Regression: Engine Size vs High CO2")

plt.legend()

plt.show()


# 16. CONFUSION MATRIX

TP = np.sum(
    (Y_logistic == 1) &
    (prediction == 1)
)

TN = np.sum(
    (Y_logistic == 0) &
    (prediction == 0)
)

FP = np.sum(
    (Y_logistic == 0) &
    (prediction == 1)
)

FN = np.sum(
    (Y_logistic == 1) &
    (prediction == 0)
)

confusion_matrix = np.array([
    [TN, FP],
    [FN, TP]
])

print("\nConfusion Matrix:")
print(confusion_matrix)

# 17. FINAL RESULTS

print("\n================ FINAL RESULTS ================")

print("\nLINEAR REGRESSION")
print("Slope:", slope)
print("Intercept:", intercept)
print("MAE:", MAE)
print("MSE:", MSE)
print("RMSE:", RMSE)
print("R2 Score:", R2)

print("\nLOGISTIC REGRESSION")
print("Slope:", logistic_slope)
print("Intercept:", logistic_intercept)
print("Accuracy:", accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix)