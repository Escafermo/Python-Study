import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder, StandardScaler
#from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# SETUP DATASET FROM .csv (TEXT ALREADY ENCODED)
dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:2].values # x IS A MATRIX
y = dataset.iloc[:, 2].values # y IS A VECTOR

# FIT RANDOM FOREST REGRESSION TO MODEL
random_forest_regressor = RandomForestRegressor(n_estimators = 1000, random_state = 0) # n_estimators = NUMBER OF TREES BUILT
random_forest_regressor.fit(x, y)

# PREDICT A NEW RESULT WITH RANDOM FOREST REGRESSION
y_pred = random_forest_regressor.predict(6.5)

# VISUALIZE RANDOM FOREST REGRESSION ONLY IN HIGH RES (NON-CONTINUOUS)
x_grid = np.arange(min(x), max(x), 0.01)      # TO INCREASE RESOLUTION ON GRAPH
x_grid = x_grid.reshape((len(x_grid)), 1)    # RESHAPE VECTOR INTO MATRIX
plt.scatter(x, y, color = 'red')
plt.plot(x_grid, random_forest_regressor.predict(x_grid), color = 'green')
plt.title('RANDOM FOREST REGRESSION')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()


'''
 ---- OPTIONAL----

# BUILD TRAINING (80%) AND TEST SETS (20%) - random_state to spit same results
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
 
# IMPUTE MISSING VALUES (NaN) AS MEAN
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

# ENCODE TEXT DEPENDENT VARIABLE
label_encoder_x = LabelEncoder()
x[:,0] = label_encoder_x.fit_transform(x[:,0])
one_hot_encoder = OneHotEncoder(categorical_features = [0])
x = one_hot_encoder.fit_transform(x).toarray()

# REMOVE ONE COLUMN OF ENCODED DUMMY DEPENDENT VARIABLE - AVOID TRAP
x = x[:, 1:]

# ENCODE TEXT INDEPENDENT VARIABLE
label_encoder_y = LabelEncoder()
y = label_encoder_y.fit_transform(y)

# SCALE NUMERIC VARIABLES
scaler_x = StandardScaler()
scaler_y = StandardScaler()
x = scaler_x.fit_transform(x) 
y = scaler_y.fit_transform(y) 
# OR
scaler_x = StandardScaler()
x_train = scaler_x.fit_transform(x_train) # FIT  = UNDERSTAND DATA (min, max, mean, stdev)
x_test = scaler_x.transform(x_test) # ONLY TRANSFORM, SINCE ALREADY UNDERSTOOD DATA FROM x_train FIT
 ---- END ----
'''