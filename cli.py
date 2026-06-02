import argparse
import os
import sys
from bot.client import BinanceFuturesClient
from bot.orders import place_order
from bot.logging_config import setup_logger

def print_summary(args):
    print("\n" + "="*40)
    print("ORDER REQUEST SUMMARY")
    print("="*40)
    print(f"Symbol:   {args.symbol.upper()}")
    print(f"Side:     {args.side.upper()}")
    print(f"Type:     {args.type.upper()}")
    print(f"Quantity: {args.quantity}")
    if args.type.upper() == 'LIMIT':
        print(f"Price:    {args.price}")
    print("="*40 + "\n")

def print_response(response):
    print("ORDER RESPONSE DETAILS")
    print("-" * 40)
    print(f"Status:      {response.get('status', 'UNKNOWN')}")
    print(f"Order ID:    {response.get('orderId', 'N/A')}")
    print(f"ExecutedQty: {response.get('executedQty', '0')}")
    
    avg_price = response.get('avgPrice')
    if avg_price and float(avg_price) > 0:
        print(f"Avg Price:   {avg_price}")
    print("-" * 40 + "\n")

def main():
    logger = setup_logger()
    
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", required=True, help="Trading pair symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side: BUY or SELL")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type: MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Order price (required for LIMIT orders)")
    
    args = parser.parse_args()

    api_key = os.environ.get("BINANCE_TESTNET_API_KEY")
    api_secret = os.environ.get("BINANCE_TESTNET_API_SECRET")

    if not api_key or not api_secret:
        print("\n[ERROR] API credentials not found.")
        print("Please set BINANCE_TESTNET_API_KEY and BINANCE_TESTNET_API_SECRET as environment variables.\n")
        logger.error("Missing environment variables for API credentials.")
        sys.exit(1)

    print_summary(args)

    client = BinanceFuturesClient(api_key, api_secret)

    try:
        response = place_order(
            client=client,
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )
        print("[SUCCESS] Order placed successfully!\n")
        print_response(response)
        logger.info(f"Order Success: {response.get('orderId')}")

    except ValueError as ve:
        print(f"[INPUT ERROR] {str(ve)}")
        logger.error(f"Validation Error: {str(ve)}")
    except Exception as e:
        print(f"[FAILED] Could not place order.\nReason: {str(e)}")
        logger.error(f"Execution Error: {str(e)}")

if __name__ == "__main__":
    main()
