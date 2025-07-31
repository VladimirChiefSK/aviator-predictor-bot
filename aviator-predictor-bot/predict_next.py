import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import joblib

DATA_FILE = "data/aviator_data.csv"
MODEL_FILE = "model/aviator_model.h5"
SCALER_FILE = "model/scaler.pkl"
SEQ_LENGTH = 20

def predict_next():
    df = pd.read_csv(DATA_FILE)
    scaler = joblib.load(SCALER_FILE)
    model = load_model(MODEL_FILE)

    if len(df) < SEQ_LENGTH:
        print("Not enough data to predict.")
        return

    last_seq = df['multiplier'].values[-SEQ_LENGTH:].reshape(-1, 1)
    scaled_seq = scaler.transform(last_seq)
    scaled_seq = np.expand_dims(scaled_seq, axis=0)

    pred_scaled = model.predict(scaled_seq)
    pred = scaler.inverse_transform(pred_scaled)[0][0]

    print(f"Predicted next multiplier: {pred:.2f}x")

if __name__ == "__main__":
    predict_next()# Placeholder script content
