from sklearn.svm import SVC
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# data, label 불러오기
df = pd.read_csv("./iris.csv")
label = df["variety"]
data = df[["sepal.length", "sepal.width", "petal.length", "petal.width"]]
train_data, valid_data, train_label, valid_label = train_test_split(data, label)

# 학습시키기
model = SVC() # Support Vector Machine Classifier
model.fit(train_data, train_label)

# 정확도 확인하기
result = model.predict(valid_data)
score = accuracy_score(result, valid_label)
print(score)

# # 질문하기
# result = model.predict([
#     [4.5, 3.2, 4.2, 1.0],
#     [5.0, 1.3, 3.4, 5.7],
#     [7.1, 3.4, 3.1, 4.3]
# ])
#
# print(result)

import joblib

joblib.dump(model, "model.pkl")