import pickle
import pandas as pd

def predict(df: pd.DataFrame):
    # Load the pre-trained model
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    
    # Make predictions on the provided dataset
    predictions = model.predict(df)
    return predictions.tolist()  # Return predictions as a list
