# LAB 10
# QUESTION 02
import kagglehub
import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

path = kagglehub.dataset_download("uciml/sms-spam-collection-dataset")

print("Dataset Path:", path)
print("Files:", os.listdir(path))

df = pd.read_csv(os.path.join(path, "spam.csv"), encoding="latin-1")

df = df[["v1", "v2"]]
df.columns = ["label", "message"]

df["label"] = df["label"].map({"ham": 0, "spam": 1})

X = df["message"]
y = df["label"]

vectorizer = CountVectorizer(stop_words="english")
X_vectorized = vectorizer.fit_transform(X)

x_train, x_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)

pred = model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred))

new_message = ["Congratulations! You have won a free prize"]
new_vector = vectorizer.transform(new_message)

result = model.predict(new_vector)

print("Prediction:", result[0])
print("0 = Not Spam, 1 = Spam")
