import sys
from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Global variable for model
model = None
label_encoders = {}
feature_columns = []

@app.route('/train', methods=['POST'])
def train():
  global model, label_encoders, feature_columns
  data = request.json
  df = pd.DataFrame(data)

  categorical_cols = df.select_dtypes(include=['object']).columns
  for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

  feature_columns = df.columns.tolist()
  feature_columns.remove('eta')  # Remove target column

  X = df.drop('eta', axis=1)
  y = df['eta']

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  model = GradientBoostingClassifier()
  model.fit(X_train, y_train)

  score = model.score(X_test, y_test)

  print("Feature Columns:", feature_columns)
  print("Label Encoders:", {k: v.classes_ for k, v in label_encoders.items()})

  return jsonify({'message': 'Training complete', 'accuracy': score})


@app.route('/predict', methods=['POST'])
def predict():
  global model, feature_columns, label_encoders
  if model is None:
    return jsonify({'error': 'Model not trained yet!'}), 400

  print("Feature Columns:", feature_columns)
  print("Label Encoders:", {k: v.classes_ for k, v in label_encoders.items()})

  input_data = request.json
  df = pd.DataFrame([input_data])

  categorical_cols = df.select_dtypes(include=['object']).columns
  for col in categorical_cols:
    if col in label_encoders:
      le = label_encoders[col]
      if any(val not in le.classes_ for val in df[col]):
        unknown_values = set(df[col]) - set(le.classes_)
        return jsonify({'error': f'Unknown categorical value(s): {", ".join(map(str, unknown_values))}'}), 400
      df[col] = le.transform(df[col])
    else:
      return jsonify({'error': f'Unknown categorical column: {col}'}), 400

  for col in feature_columns:
    if col not in df.columns:
      df[col] = 0

  df = df[feature_columns]

  prediction = model.predict(df)

  return jsonify({'prediction': int(prediction[0])})


if __name__ == '__main__':
  # Default to port 5001 if not specified
  port = int(sys.argv[1]) if len(sys.argv) > 1 else 5001
  app.run(host='0.0.0.0', port=port)
