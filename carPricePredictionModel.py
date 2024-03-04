from sklearn.model_selection import train_test_split, GridSearchCV
import pandas as pd
import xgboost as xgb
from xgboost import XGBRegressor

df = pd.read_csv("final_car_data.csv")

df.drop("Unnamed: 0", axis=1, inplace=True)
df.drop("Model", axis=1, inplace=True)

X = df.drop(["Price"], axis=1)
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=144)

params = {"colsample_bytree": [0.4, 0.5, 0.6],
          "learning_rate": [0.01, 0.02, 0.09],
          "max_depth": [2, 3, 4, 5, 6],
          "n_estimators": [100, 200, 500, 2000]}

xgb1 = XGBRegressor(colsample_bytree=0.4,
                    learning_rate=0.02,
                    max_depth=5,
                    n_estimators=2000)

model_xgb = xgb1.fit(X_train, y_train)
