import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import joblib
import os

DATA_FILE = "data/aviator_data.csv"
MODEL_FILE = "model/aviator_model.h5"
SCALER_FILE = "model/scaler.pkl"
SEQ_LENGTH = 20  # use last 20 multipliers to predict next

def load_data():
    df = pd.read_csv(DATA_FILE)
    values = df['multiplier'].values.reshape(-1, 1)

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(values)

    X, y = [], []
    for i in range(len(scaled) - SEQ_LENGTH):
        X.append(scaled[i:i+SEQ_LENGTH])
        y.append(scaled[i+SEQ_LENGTH])

    X, y = np.array(X), np.array(y)
    return X, y, scaler

def train_model():
    if not os.path.exists(DATA_FILE):
        print("No data found. Run scraper first.")
        return

    X, y, scaler = load_data()

    model = Sequential([
        LSTM(64, return_sequences=True, input_shape=(SEQ_LENGTH, 1)),
        LSTM(32),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=20, batch_size=32)

    # Save model and scaler
    model.save(MODEL_FILE)
    joblib.dump(scaler, SCALER_FILE)
    print("Model trained and saved.")

if __name__ == "__main__":
    train_model()# Placeholder script content
