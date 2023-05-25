from dydx3.constants import API_HOST_GOERLI, API_HOST_MAINNET
#config lets you access our env variables
from decouple import config

# !!!! Select MODE!!!
MODE = "DEVELOPEMENT"

# Close all open positions and orders
ABORT_ALL_POSITIONS = True

# Find Coingreated pairs
FIND_COINTEGRATED = True

# MANGE EXITS-PLACE TRADES
MANAGE_EXITS = True
# Place Trades
PLACE_TRADES = True

# Resolution
RESOLUTION = "1HOUR"

# States window - days for info band
WINDOW = 21

# Threshold = opening a trade
MAX_HALF_LIFE = 24
ZSCORE_THRESH = 1.5
USD_PER_TRADE = 50
USD_MIN_COLLATERAL = 1800

# Threshold - Closing
CLOSE_AT_ZSCORE_CROSS = True

# Ethereum address
#check .env for reference to this
ETHEREUM_ADDRESS = config("ETHEREUM_ADDRESS")


# KEYS - DEVELOPMENT
# Must be on Testnet in DYDX
STARK_PRIVATE_KEY_TESTNET = config("STARK_PRIVATE_KEY_TESTNET")
DYDX_API_KEY_TESTNET = config("DYDX_API_KEY_TESTNET")
DYDX_API_SECRET_TESTNET =config("DYDX_API_SECRET_TESTNET")
DYDX_API_PASSPHRASE_TESTNET = config("DYDX_API_PASSPHRASE_TESTNET")



# Keys - Export
STARK_PRIVATE_KEY = STARK_PRIVATE_KEY_TESTNET
DYDX_API_KEY = DYDX_API_KEY_TESTNET
DYDX_API_SECRET = DYDX_API_SECRET_TESTNET
DYDX_API_PASSPHRASE = DYDX_API_PASSPHRASE_TESTNET


# HOST - Export
HOST = API_HOST_GOERLI

# HTTP providers
HTTP_PROVIDER_TESTNET = "https://eth-goerli.g.alchemy.com/v2/rduPja86U05uXu7fxufTV0OXU2nVzDx8"
HTTP_PROVIDER = HTTP_PROVIDER_TESTNET