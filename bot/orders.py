from bot.client import BinanceFuturesClient
from bot.validators import validate_inputs
from bot.logging_config import setup_logger

logger = setup_logger()

def place_order(client: BinanceFuturesClient, symbol: str, side: str, order_type: str, quantity: float, price: float = None) -> dict:
    # 1. Validate inputs
    validate_inputs(symbol, side, order_type, quantity, price)
    
    endpoint = "/fapi/v1/order"
    params = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": order_type.upper(),
        "quantity": quantity
    }

    if order_type.upper() == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC" # Good Till Canceled (required for limit orders)

    logger.info(f"Attempting to place {order_type} order for {quantity} {symbol}")
    
    # 2. Place Order
    response = client.send_signed_request("POST", endpoint, params)
    return response
