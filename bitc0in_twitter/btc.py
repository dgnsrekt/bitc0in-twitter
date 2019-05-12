# Provides fuctionality to interact with the bitcoin price.

from ccxt import bitmex

import logme

bitcoin_logger = logme.log(scope="module", name="bitcoin")


def get_percent_change(currency: str = "BTC/USD") -> float:
    """Gets the current BTC/USD percent change.

    :param currency: The ticker for the requested currency.
    :returns: The current 24 hour percent change.
    """

    bitcoin_logger.debug(f"Getting {currency} percentage change.")
    response = bitmex().fetch_ticker(currency)
    percent_change = response["percentage"]
    bitcoin_logger.info(f"{currency} percent change: {percent_change:0.2f} %.")
    return percent_change


if __name__ == "__main__":
    pc = get_percent_change()
    print(pc)
