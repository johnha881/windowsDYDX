from func_utils import get_ISO_times
from pprint import pprint
import pandas as pd
import numpy as np
import time
from constants import RESOLUTION


# Get relevant time peroids for ISO from and to
ISO_TIMES = get_ISO_times()

pprint(ISO_TIMES)

# Construct market prices
def construct_market_prices(client):
    pass