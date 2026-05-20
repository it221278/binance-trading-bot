from bot.client import BinanceFuturesClient
from bot.logging_config import logger


class OrderManager:

    def __init__(self):

        self.client = BinanceFuturesClient()

    def create_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None
    ):

        try:

            response = self.client.place_order(
                symbol=symbol,
                side=side,
                order_type=order_type,
                quantity=quantity,
                price=price
            )

            print("\n===== ORDER SUCCESS =====")

            print(
                f"Order ID: {response.get('orderId')}"
            )

            print(
                f"Status: {response.get('status')}"
            )

            print(
                f"Executed Qty: {response.get('executedQty')}"
            )

            print(
                f"Avg Price: {response.get('avgPrice')}"
            )

            logger.info(
                "Order placed successfully"
            )

        except Exception as e:

            print("\nORDER FAILED")

            print(str(e))

            logger.error(
                f"Order failed: {e}"
            )