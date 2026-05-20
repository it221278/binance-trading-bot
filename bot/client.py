import time
import hmac
import hashlib
import requests

from urllib.parse import urlencode
from dotenv import load_dotenv
import os

from bot.logging_config import logger

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
BASE_URL = os.getenv("BASE_URL")


class BinanceFuturesClient:

    def __init__(self):

        self.api_key = API_KEY
        self.api_secret = API_SECRET
        self.base_url = BASE_URL

    def generate_signature(self, params):

        query_string = urlencode(params)

        signature = hmac.new(
            self.api_secret.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()

        return signature

    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None
    ):

        endpoint = "/fapi/v1/order"

        url = self.base_url + endpoint

        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity,
            "timestamp": int(time.time() * 1000)
        }

        if order_type.upper() == "LIMIT":

            params["price"] = price
            params["timeInForce"] = "GTC"

        signature = self.generate_signature(params)

        params["signature"] = signature

        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        try:

            logger.info(f"REQUEST: {params}")

            response = requests.post(
                url,
                headers=headers,
                params=params,
                timeout=10
            )

            data = response.json()

            logger.info(f"RESPONSE: {data}")

            response.raise_for_status()

            return data

        except requests.exceptions.RequestException as e:

            logger.error(f"API Error: {e}")

            raise

        except Exception as e:

            logger.error(f"Unexpected Error: {e}")

            raise