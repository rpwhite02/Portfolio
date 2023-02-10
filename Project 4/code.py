import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales = pd.read_csv('home_data.csv') 

# Selects 1% of the data
sales = sales.sample(frac=0.01) 


# All of the features of interest
selected_inputs = [
    'bedrooms', 
    'bathrooms',
    'sqft_living', 
    'sqft_lot', 
    'floors', 
    'waterfront', 
    'view', 
    'condition', 
    'grade',
    'sqft_above',
    'sqft_basement',
    'yr_built', 
    'yr_renovated'
]

# Compute the square and sqrt of each feature
all_features = []
for data_input in selected_inputs:
    square_feat = data_input + '_square'
    sqrt_feat = data_input + '_sqrt'
    sales[square_feat] = sales[data_input] * sales[data_input]
    sales[sqrt_feat] = sales[data_input] ** 0.5
    all_features.extend([data_input, square_feat, sqrt_feat])
    
# Split the data into features and price
price = sales['price']
sales = sales[all_features]


from sklearn.model_selection import train_test_split

train_and_validation_sales, test_sales, train_and_validation_price, test_price = \
    train_test_split(sales, price, test_size=0.2)
train_sales, validation_sales, train_price, validation_price = \
    train_test_split(train_and_validation_sales, train_and_validation_price, test_size=.125) # .10 (validation) of .80 (train + validation)


# Standardize the data so that we can meet the assumptions of the Ridge and LASSO models
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(train_sales)
train_sales = scaler.transform(train_sales)
validation_sales = scaler.transform(validation_sales)
test_sales = scaler.transform(test_sales)


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Training a linear regression model and print out its mean squared error.
model = LinearRegression()
model.fit(train_sales, train_price)
price_predictions = model.predict(test_sales)
test_rmse_unregularized = mean_squared_error(test_price, price_predictions, squared = False)
test_rmse_unregularized # 215279.9416125085


# Train Ridge using the following choices of l2 penalty: [10^-5, 10^-4, ... , 10^4, 10^5]
from sklearn.linear_model import Ridge
data = []
l2_lambdas = np.logspace(-5, 5, 11, base = 10)
for i in l2_lambdas:
    ridge_model = Ridge(alpha=i)
    ridge_model.fit(train_sales, train_price)
    train_predictions_ridge = ridge_model.predict(train_sales)
    validation_predictions_ridge = ridge_model.predict(validation_sales)
    data.append({
        'l2_penalty': i,
        'model': ridge_model,
        'train_rmse': mean_squared_error(train_price, train_predictions_ridge, squared = False),
        'validation_rmse': mean_squared_error(validation_price, validation_predictions_ridge, squared = False)
    })
    
    
# Plot the validation RMSE as a blue line with dots
plt.plot(ridge_data['l2_penalty'], ridge_data['validation_rmse'], 
         'b-^', label='Validation')
# Plot the train RMSE as a red line dots
plt.plot(ridge_data['l2_penalty'], ridge_data['train_rmse'], 
         'r-o', label='Train')

# Make the x-axis log scale for readability
plt.xscale('log')

# Label the axes and make a legend
plt.xlabel('l2_penalty')
plt.ylabel('RMSE')
plt.legend()


# Take the best l2 penalty based on model evaluations, save in best_l2.
# Take the best model and evaluate its error on the test dataset. Save value in test_rmse_ridge
index = ridge_data['validation_rmse'].idxmin()
row_ridge = ridge_data.loc[index]
best_l2 = row_ridge['l2_penalty']
ridge_model_test = Ridge(alpha = best_l2)
ridge_model_test.fit(train_sales, train_price)
test_predictions_ridge = ridge_model_test.predict(test_sales)
test_rmse_ridge = mean_squared_error(test_price, test_predictions_ridge, squared = False)
test_rmse_ridge # 196459.94533935536


# Train LASSO model using the following l1 penalties: [10, 10^2, ... , 10^7]
from sklearn.linear_model import Lasso
data = []
l1_lambdas = np.logspace(1, 7, 7, base=10)
for i in l1_lambdas:
    lasso_model = Lasso(alpha=i)
    lasso_model.fit(train_sales, train_price)
    train_predictions_lasso = lasso_model.predict(train_sales)
    validation_predictions_lasso = lasso_model.predict(validation_sales)
    data.append({
        'l1_penalty': i,
        'model': lasso_model,
        'train_rmse': mean_squared_error(train_price, train_predictions_lasso, squared = False),
        'validation_rmse': mean_squared_error(validation_price, validation_predictions_lasso, squared = False)
    })
    

# Plot the validation RMSE as a blue line with dots

plt.plot(lasso_data['l1_penalty'], lasso_data['validation_rmse'],
         'b-^', label='Validation')

# Plot the train RMSE as a red line dots
plt.plot(lasso_data['l1_penalty'], lasso_data['train_rmse'],
         'r-o', label='Train')

# Make the x-axis log scale for readability
plt.xscale('log')

# Label the axes and make a legend
plt.xlabel('l1_penalty')
plt.ylabel('RMSE')
plt.legend()


# Take the best l1 penalty based on model evaluations, save in best_l1
# Take the best model and evaluate it on the test dataset and report its RMSE. save value in test_rmse_lasso
index = lasso_data['validation_rmse'].idxmin()
row_lasso = lasso_data.loc[index]
best_l1 = row_lasso['l1_penalty']
lasso_model_test = Lasso(alpha = best_l1)
lasso_model_test.fit(train_sales, train_price)
test_predictions_lasso = lasso_model_test.predict(test_sales)
test_rmse_lasso = mean_squared_error(test_price, test_predictions_lasso, squared = False)
test_rmse_lasso # 221445.06084699565
