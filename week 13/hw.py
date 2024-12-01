import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
 
data = { 
    "Weekly Hours Exercised (X)": [1, 2, 3, 4, 5], 
    "Weekly Savings (Y)($)": [10, 20, 30, 40, 50] 
} 
 
df = pd.DataFrame(data) 
X = df["Weekly Hours Exercised (X)"].values 
Y = df["Weekly Savings (Y)($)"].values 
 
def prediction(beta_0, beta_1, X): 
    return beta_0 + beta_1 * X 
 
def cost(Y_pred, Y_actual): 
    return np.mean((Y_pred - Y_actual) ** 2) 
 
def gradient(X, Y, beta_0, beta_1, alpha, iterations): 
    n = len(Y) 
    for _ in range(iterations): 
        Y_pred = prediction(beta_0, beta_1, X) 
        d_beta_0 = -2 * np.sum(Y - Y_pred) / n 
        d_beta_1 = -2 * np.sum((Y - Y_pred) * X) / n 
        beta_0 -= alpha * d_beta_0 
        beta_1 -= alpha * d_beta_1 
    return beta_0, beta_1 
beta_0, beta_1 = gradient(X, Y, 0, 1, 0.01, 500) 
 
savings_6 = prediction(beta_0, beta_1, 6) 
savings_10 = prediction(beta_0, beta_1, 10) 
 
print(f"Predicted savings for 6 hours: ${savings_6:.2f}") 
print(f"Predicted savings for 10 hours: ${savings_10:.2f}") 
 
plt.scatter(X, Y, color='red', label='Data Points') 
line = [prediction(beta_0, beta_1, x) for x in X] 
plt.plot(X, line, color='darkgreen', label='Regression Line') 
plt.xlabel('Weekly Hours Exercised') 
plt.ylabel('Weekly Savings ($)') 
plt.title('Simple Linear Regression') 
plt.legend() 
plt.show()
