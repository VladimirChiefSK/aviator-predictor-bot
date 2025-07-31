# Aviator Predictor Bot

A Telegram bot that predicts Aviator game multipliers using an LSTM neural network trained on historical data.

## Setup (Local)
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run scraper to collect multipliers:
   ```bash
   python aviator_scraper.py
   ```
3. Train the model:
   ```bash
   python train_model.py
   ```
4. Add your Telegram bot token in `bot.py` and run:
   ```bash
   python bot.py
   ```

## Deployment (Heroku)
1. Login to Heroku:
   ```bash
   heroku login
   ```
2. Create Heroku app and push:
   ```bash
   git init
   heroku create
   git add .
   git commit -m "initial commit"
   git push heroku master
   ```
3. Scale worker:
   ```bash
   heroku ps:scale worker=1
   ```
