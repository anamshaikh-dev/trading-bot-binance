# 🚀 Binance Futures Trading Bot (Testnet)

## 📌 Overview
This project is a **Python-based CLI trading bot** that interacts with the Binance Futures Testnet (USDT-M) to place MARKET and LIMIT orders.

The application is designed with a **modular architecture**, focusing on clean code structure, input validation, logging, and error handling — mimicking real-world backend systems used in trading platforms.

---

## 🎯 Objective
To build a simplified trading system that demonstrates:
- API integration with Binance Futures
- Command-line interaction
- Order execution logic
- Production-style logging and validation

---

## ✨ Features
- ✅ Place **MARKET** and **LIMIT** orders  
- ✅ Supports both **BUY** and **SELL**  
- ✅ CLI-based input using `argparse`  
- ✅ Input validation (type, quantity, price)  
- ✅ Structured logging (`bot.log`)  
- ✅ Exception handling (API errors, invalid inputs)  
- ✅ Clean modular design (separation of concerns)

---

## 🏗️ Project Structure


trading_bot/
│
├── bot/
│ ├── client.py # Binance API client setup
│ ├── orders.py # Order execution logic
│ ├── validators.py # Input validation
│ ├── logging_config.py # Logging configuration
│ └── init.py
│
├── cli.py # CLI entry point
├── requirements.txt
├── README.md
├── sample_logs.txt # Example logs (for evaluation)


---

## ⚙️ Setup Instructions

### 1. Clone Repository

git clone https://github.com/your-username/trading-bot-binance.git

cd trading-bot-binance


### 2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate


### 3. Install Dependencies

pip install -r requirements.txt


### 4. Configure Environment Variables
Create a `.env` file:


API_KEY=your_api_key
API_SECRET=your_api_secret


---

## ▶️ Usage

### 🔹 MARKET Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001


### 🔹 LIMIT Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 80000


---

## 📊 Output Example


📌 Order Request Summary
{'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.001}

✅ Order Successful
Order ID: 123456789
Status: NEW
Executed Qty: 0.0000
Avg Price: 0.00


---

## 📝 Logging

- All API requests, responses, and errors are logged in:

bot.log


- Sample logs are provided in:

sample_logs.txt


---

## ⚠️ Assumptions & Notes

- This project uses **Binance Futures Testnet**, not real trading.
- Orders may show:
  - `Executed Qty: 0.0000`
  - `Avg Price: 0.00`

  This is expected if:
  - The order is not filled yet
  - Market conditions do not match the limit price
  - Testnet delays execution

---

## 🧠 Design Decisions

- **Separation of Concerns**:
  - API logic, validation, CLI, and logging are separated
- **Scalability**:
  - Easy to extend with new order types (Stop-Limit, OCO, etc.)
- **Maintainability**:
  - Modular structure improves readability and reuse

---

## 🚀 Future Improvements
- Add Stop-Limit / OCO orders  
- Add interactive CLI (menus)  
- Add basic UI dashboard  
- Add unit tests  

---

## 👨‍💻 Author
Anam Shaikh

---

## ⭐ Conclusion
This project demonstrates the ability to build a **real-world backend system** involving API i
