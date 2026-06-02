import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from bot.logging_config import setup_logger

logger = setup_logger()

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        # Using the required testnet base URL
        self.base_url = "https://testnet.binancefuture.com" 
        self.api_key = api_key
        self.api_secret = api_secret
        self.session = requests.Session()
        self.session.headers.update({
            "X-MBX-APIKEY": self.api_key,
            "Content-Type": "application/json"
        })

    def _generate_signature(self, query_string: str) -> str:
        return hmac.new(
            self.api_secret.encode('utf-8'),
            query_string.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

    def send_signed_request(self, method: str, endpoint: str, params: dict = None) -> dict:
        if params is None:
            params = {}
        
        # Add required timestamp
        params['timestamp'] = int(time.time() * 1000)
        
        # Generate signature
        query_string = urlencode(params)
        signature = self._generate_signature(query_string)
        params['signature'] = signature

        url = f"{self.base_url}{endpoint}"
        logger.info(f"Sending {method} request to {endpoint}")
        logger.debug(f"Parameters: {params}")

        try:
            # Using data=params for POST requests as required by Binance REST API
            response = self.session.request(method, url, params=params)
            response.raise_for_status()
            logger.info("Request successful")
            return response.json()
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP Error: {response.text}")
            raise Exception(f"API Error: {response.json().get('msg', 'Unknown Error')}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Network Failure: {str(e)}")
            raise Exception("Network failure occurred while connecting to Binance API.")
