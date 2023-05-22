from func_connections import connect_dydx
from constants import ABORT_ALL_POSITIONS, FIND_COINTEGRATED
from func_private import abort_all_positions
from func_public import construct_market_prices

if __name__ == "__main__":
    
    #Connect to client

    try:
        print("connecting to Client...")
        client = connect_dydx()
    except Exception as e:
        print("Error connecting to client: ", e)
        exit(1)
    
    # Abort all open positions
    if ABORT_ALL_POSITIONS:
        try:
            print("close all positions")
            close_orders = abort_all_positions(client)
        except Exception as e:
            print("Error closing all positions: ", e)
            exit(1)

    # Find Cointegrated Pairs
    if FIND_COINTEGRATED:

        # Construct market prices
        try:
            print("Fetching market prices, please allow 3 minutes...")
            df_market_price = construct_market_prices(client)
        except Exception as e:
            print("Error Constructing market prices: ", e)
            exit(1)