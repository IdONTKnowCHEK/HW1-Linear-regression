# 3. streamlit or flask web, 框架 deployment


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import streamlit as st

# Function to generate synthetic data
def generate_data(a=1, b=0, num_points=100, noise=1.0):
    X = np.random.rand(num_points, 1) * 10
    y = a * X + b + np.random.randn(num_points, 1) * noise
    return X, y

# Streamlit inputs for parameters
st.title("Simple Linear Regression Model")
a = st.sidebar.slider("Slope (a)", min_value=-10.0, max_value=10.0, value=1.0)
b = st.sidebar.slider("Intercept (b)", min_value=-10.0, max_value=10.0, value=0.0)
num_points = st.sidebar.slider("Number of points", min_value=10, max_value=500, value=100)
noise = st.sidebar.slider("Noise level", min_value=0.0, max_value=10.0, value=1.0)

# Generate synthetic data based on user inputs
X, y = generate_data(a=a, b=b, num_points=num_points, noise=noise)

# Convert to DataFrame for display
data = pd.DataFrame(np.hstack([X, y]), columns=['X', 'y'])

# Display data
st.write("Generated Data")
st.write(data.head())

# Plot data
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='blue')
plt.title(f'Synthetic Data: y = {a} * x + {b} + noise')
plt.xlabel('X')
plt.ylabel('y')
st.pyplot(plt)

# Step 3: Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Predictions and Evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Display model evaluation metrics
st.write(f"Mean Squared Error: {mse}")
st.write(f"R² Score: {r2}")

# Step 6: Prediction
new_value = st.sidebar.number_input("Predict for X =", value=5.0)
predicted_value = model.predict(np.array([[new_value]]))
st.write(f"Predicted y for X = {new_value}: {predicted_value[0][0]}")
