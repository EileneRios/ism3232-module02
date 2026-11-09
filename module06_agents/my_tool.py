# my_tool.py
# Author: Eilene Rios


class PriceList:
    """A tool that knows the price of each product. It knows nothing about chatting."""

    def __init__(self, prices):
        """Store the product prices this tool can look up."""
        self.prices = prices

    def find_product(self, text):
        """Return the first known product mentioned in text, or None."""
        for product in self.prices:
            if product in text.lower():
                return product
        return None

    def price_for(self, product):
        """Return the price of one product, or None if the product is unknown."""
        if product in self.prices:
            return self.prices[product]
        return None
