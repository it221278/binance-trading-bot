import argparse

from bot.orders import OrderManager

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True
    )

    parser.add_argument(
        "--side",
        required=True
    )

    parser.add_argument(
        "--type",
        required=True
    )

    parser.add_argument(
        "--quantity",
        required=True
    )

    parser.add_argument(
        "--price",
        required=False
    )

    args = parser.parse_args()

    try:

        symbol = args.symbol.upper()

        side = validate_side(args.side)

        order_type = validate_order_type(
            args.type
        )

        quantity = validate_quantity(
            args.quantity
        )

        price = validate_price(args.price)

        if (
            order_type == "LIMIT"
            and price is None
        ):

            raise ValueError(
                "LIMIT order requires --price"
            )

        print("\n===== ORDER REQUEST =====")

        print(f"Symbol: {symbol}")

        print(f"Side: {side}")

        print(f"Type: {order_type}")

        print(f"Quantity: {quantity}")

        if price:
            print(f"Price: {price}")

        manager = OrderManager()

        manager.create_order(
            symbol,
            side,
            order_type,
            quantity,
            price
        )

    except Exception as e:

        print(f"\nError: {e}")


if __name__ == "__main__":
    main()