# Binance Futures Trading Bot

Python CLI bot for Binance Futures Testnet.

## Features

- MARKET Orders
- LIMIT Orders
- BUY/SELL
- Logging
- Validation
- Error Handling

## Install

pip install -r requirements.txt

## Run

### MARKET BUY

python run.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### LIMIT SELL

python run.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 90000