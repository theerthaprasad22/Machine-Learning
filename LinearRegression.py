w = 0  # Initial weight (slope)
b = 0  # Initial bias (intercept)
lr = 0.001  # Learning rate

# Area of houses
x = [10, 20, 30, 40, 50]

# Price of houses in lakhs
y = [30, 60, 100, 130, 160]


# Prediction function (y = wx + b)
def predict(x, w, b):
    return w * x + b


# Training using simple Gradient Descent
for _ in range(1000):
    for i in range(len(x)):
        y_hat = predict(x[i], w, b)  # Predicted value
        error = y_hat - y[i]  # Error calculation

        # Update weight and bias
        w = w - lr * error * x[i]
        b = b - lr * error

# Taking user input
s = int(input("Enter the area of the plot: "))

# Predicting price
predicted = predict(s, w, b)

print(predicted, "Lakhs")