import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_model(df: pd.DataFrame, target: str):
    # Splitting the dataset into features (X) and target (y)
    X = df.drop(columns=[target])
    y = df[target]
    
    # Splitting data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Initialize and train the model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save the trained model
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)
    
    return {"message": "Model trained successfully"}
