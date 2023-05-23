from func_connections import connect_dydx
from constants import ABORT_ALL_POSITIONS, FIND_COINTEGRATED
from func_private import abort_all_positions
from func_public import construct_market_prices
from func_cointegration import store_cointegration_results

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

        
        # STore Cointegrated Pairs
        try:
            print("Storing Cointegrated Pairs...")
            stores_result = store_cointegration_results(df_market_price)
            if stores_result != "saved":
                print("Error saving cointegrated pairs")
                exit(1)
        except Exception as e:
            print("Error saving cointegrated pairs: ", e)
            exit(1)