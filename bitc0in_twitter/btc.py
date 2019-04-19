"""
bitc0in_twitter.btc
-------------------

This module provides fuctions to interact with the bitcoin price.
"""

import ccxt


def get_percent_change(currency="BTC/USD"):
    bitmex = ccxt.bitmex()
    response = bitmex.fetch_ticker(currency)
    return response["percentage"]


if __name__ == "__main__":
    pc = get_percent_change()
    print(pc)
