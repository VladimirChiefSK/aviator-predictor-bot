from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import joblib

# CONFIG
TOKEN = "8412877094:AAEYgE0r6uvt2OVJWAJkhOyNoEF9dy2bOQU"  # Replace with your token
DATA_FILE = "data/aviator_data.csv"
MODEL_FILE = "model/aviator_model.h5"
SCALER_FILE = "model/scaler.pkl"
SEQ_LENGTH = 20

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Aviator Predictor! Use /predict to get the next multiplier.")

async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Load model + scaler
        model = load_model(MODEL_FILE)
        scaler = joblib.load(SCALER_FILE)
        df = pd.read_csv(DATA_FILE)

        if len(df) < SEQ_LENGTH:
            await update.message.reply_text("Not enough data collected yet. Run scraper first.")
            return

        last_seq = df['multiplier'].values[-SEQ_LENGTH:].reshape(-1, 1)
        scaled_seq = scaler.transform(last_seq)
        scaled_seq = np.expand_dims(scaled_seq, axis=0)

        pred_scaled = model.predict(scaled_seq)
        pred = scaler.inverse_transform(pred_scaled)[0][0]

        await update.message.reply_text(f"Predicted next multiplier: {pred:.2f}x")

    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("predict", predict))

    app.run_polling()

if __name__ == "__main__":
    main()# Placeholder script content
