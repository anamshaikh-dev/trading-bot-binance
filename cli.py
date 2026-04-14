import argparse
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logging

setup_logging()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

    print("\n📌 Order Request Summary")
    print(vars(args))

    order = place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    if order:
        print("\n✅ Order Successful")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))
        print("Avg Price:", order.get("avgPrice", "N/A"))
    else:
        print("\n❌ Order Failed")

except Exception as e:
    print(f"\n⚠️ Error: {e}")