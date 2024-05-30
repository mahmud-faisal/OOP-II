import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
file_path = 'data/allergen_del.csv'
df = pd.read_csv(file_path)

# Encode categorical variables
label_encoders = {}
for column in df.columns[:-1]:  # Exclude the 'Prediction' column
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Features and target
X = df.drop('Prediction', axis=1)
y = df['Prediction'].apply(lambda x: 1 if x == 'Contains' else 0)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the decision tree model
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Save the model and label encoders for later use
joblib.dump(clf, 'models/allergen_predictor.pkl')
joblib.dump(label_encoders, 'models/label_encoders.pkl')
