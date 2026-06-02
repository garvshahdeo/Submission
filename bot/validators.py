def validate_inputs(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    errors = []

    if not symbol.isalnum():
        errors.append("Symbol must be alphanumeric (e.g., BTCUSDT).")
    
    if side.upper() not in ["BUY", "SELL"]:
        errors.append("Side must be 'BUY' or 'SELL'.")
        
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        errors.append("Order type must be 'MARKET' or 'LIMIT'.")
        
    if quantity <= 0:
        errors.append("Quantity must be greater than 0.")
        
    if order_type.upper() == "LIMIT" and (price is None or price <= 0):
        errors.append("A valid price greater than 0 is required for LIMIT orders.")

    if errors:
        raise ValueError(" | ".join(errors))
