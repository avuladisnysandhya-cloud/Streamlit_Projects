# from sklearn.datasets import load_iris
# from sklearn.ensemble import RandomForestClassifier
# import joblib

# iris = load_iris()
# x, y = iris.data, iris.target
# model=RandomForestClassifier().fit(x,y)
# joblib.dump(model,"model.pkl")
# print("Model saved!")

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib
X,y=load_iris(return_X_y=True)
model=LogisticRegression(max_iter=200).fit(X,y)
joblib.dump(model,"model.pkl")
print("Logistic Regression model saved!")