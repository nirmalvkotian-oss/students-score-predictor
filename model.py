import numpy as np
from sklearn.linear_model import LinearRegression

def train():
    # Sample data: Hours studied vs. Exam score
    X = np.array([[1], [2], [3], [4], [5], [6], [7]])
    y = np.array([35, 45, 60, 65, 75, 85, 92])
    
    # Train the model
    model = LinearRegression()
    model.fit(X, y)
    
    return model
