
# Binance Futures Testnet Trading Bot

A simplified Python command-line application to place Market and Limit orders on the Binance Futures Testnet (USDT-M).

## Setup Steps
1. Clone this repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Set your API credentials as environment variables:
   - Windows (CMD): 
     `set BINANCE_TESTNET_API_KEY=your_api_key`
     `set BINANCE_TESTNET_API_SECRET=your_api_secret`
   - Mac/Linux: 
     `export BINANCE_TESTNET_API_KEY="your_api_key"`
     `export BINANCE_TESTNET_API_SECRET="your_api_secret"`

## How to Run Examples
**Market Order:**
`python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01`

**Limit Order:**
`python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 65000`

## Assumptions
- The application assumes the user has already funded their testnet account with test USDT.
- Environment variables are used for secure API key management to avoid hardcoding secrets.
