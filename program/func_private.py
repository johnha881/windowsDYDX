from datetime import datetime, timedelta
import time
from pprint import pprint
from func_utils import format_number

# Place market order REDUCE ONLY SHOULD BE TRUE ONLY IF WE ARE CLOSING AN OPEN POSITION
def place_market_order(client, market,side, size, price, reduce_only):
    # Get Position ID
    account_response = client.private.get_account()
    position_id = account_response.data['account']['positionId']

    # Get expiration time
    server_time = client.public.get_time()
    expiration = datetime.fromisoformat(server_time.data['iso'].replace('Z','')) + timedelta(seconds=70)

    # Place an order
    place_order = client.private.create_order(
        position_id = position_id,
        market = market,
        side = side,
        order_type ='MARKET',
        post_only = False,
        size = size,
        price = price,
        limit_fee ='0.015',
        expiration_epoch_seconds = expiration.timestamp(),
        time_in_force ='FOK',
        reduce_only = reduce_only
        )
    
    #return result
    return place_order.data

# ABort all open positions
def abort_all_positions(client):
    
    # Cancel all orders
    client.private.cancel_all_orders()

    #Protect API
    time.sleep(0.5)

    # Get markest for reference of tick size
    markets = client.public.get_markets().data


    # Protect API
    time.sleep(0.5)

    #get all open positions
    positions = client.private.get_positions(status = "OPEN")
    all_positions = positions.data["positions"]


    # Handle open positions
    close_orders = []
    if len(all_positions) >0:

        #loop through each positions
        for position in all_positions:

            # Determain market
            market = position["market"]

            #Determine Side
            side = "BUY"
            if position["side"] == "LONG":
                side = "SELL"
            
            print(market, side)

            # Get Price
            price = float(position["entryPrice"])
            accept_price = price * 1.7 if side == "BUY" else price *0.3
            tick_size = markets["markets"][market]["tickSize"]
            accept_price = format_number(accept_price, tick_size)

            # Placeorder to close
            order = place_market_order(
                client,
                market,
                side,
                position["sumOpen"],
                accept_price,
                True

            )

            # Append the result
            close_orders.append(order)

            # Protect API
            time.sleep(0.2)

        # Return close orders
        return close_orders