# Binance Futures Trading Bot (Testnet)

## Overview
This is a Python CLI-based trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

## Features
- Supports BUY and SELL orders
- MARKET and LIMIT order types
- CLI-based input using argparse
- Input validation
- Logging of API requests and responses
- Error handling for invalid inputs and API failures

## Project Structure
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── __init__.py
│
├── cli.py
├── requirements.txt
├── README.md

## Setup Instructions

1. Clone the repository
2. Create virtual environment:
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Create a `.env` file:
   API_KEY=your_api_key
   API_SECRET=your_api_secret

## Usage

### MARKET Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### LIMIT Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 80000

## Notes
- Orders are placed on Binance Futures Testnet
- Logs are stored in `bot.log`