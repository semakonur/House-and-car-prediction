from sklearn.model_selection import train_test_split
import pandas as pd
import xgboost as xgb
from xgboost import XGBRegressor

df = pd.read_csv("final_house_data.csv")
df.drop("City", axis=1, inplace=True)
df.drop("Neighborhood", axis=1, inplace=True)
df.dropna(inplace=True)

df = df[['District', 'Price', 'Gross Square Meter', 'Net Square Meter', 'Number of Rooms', 'Building Age', 'Floor Location']]

X = df.drop(['Price'], axis=1)
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=144)

params = {"colsample_bytree": [0.4, 0.5, 0.6],
          "learning_rate": [0.01, 0.02, 0.09],
          "max_depth": [2, 3, 4, 5, 6],
          "n_estimators": [100, 200, 500, 2000]}

xgb1 = XGBRegressor(colsample_bytree=0.5,
                    learning_rate=0.02,
                    max_depth=5,
                    n_estimators=100)

model_xgb = xgb1.fit(X_train, y_train)
