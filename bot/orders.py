from bot.client import get_client
import logging

client = get_client()

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )
        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
        else:
            raise ValueError("Invalid order type")

        logging.info(f"Order response: {order}")
        return order

    except Exception as e:
        logging.error(f"Error placing order: {e}")
        return None