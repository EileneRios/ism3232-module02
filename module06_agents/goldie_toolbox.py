# goldie_toolbox.py
# Author: Eilene Rios


class GoldieToolbox:
    """Every tool request from Goldie's model comes through here and is checked."""

    def __init__(self, price_list, hold_queue):
        """Hold the tools the model is allowed to ask for."""
        self.price_list = price_list
        self.hold_queue = hold_queue

    def tool_list(self):
        """Return the tools the model may ask for. They are not called here."""
        return [
            self.price_list.check_price,
            self.hold_queue.request_hold,
        ]

    def run(self, name, arguments, history):
        """Check one tool request. Run the tool only if every check passes."""
        if name == "check_price":
            product = self.clean(arguments, "product")
            if product == "":
                return "The product is missing. Ask the shopper which product."
            if not self.customer_said(history, product):
                return "The shopper has not named that product. Ask them which one."
            return self.price_list.check_price(product)
        if name == "request_hold":
            product = self.clean(arguments, "product")
            customer_name = self.clean(arguments, "customer_name")
            if product == "" or customer_name == "":
                return "The product and the shopper's full name are both needed."
            if not self.customer_said(history, product):
                return "The shopper has not named that product. Ask them which one."
            if not self.customer_said(history, customer_name):
                return "The shopper has not given that name. Ask them for it."
            return self.hold_queue.request_hold(product, customer_name)
        return f"There is no tool named {name}."

    def clean(self, arguments, key):
        """Return one argument as text without extra spaces, or "" if it is missing."""
        return str(arguments.get(key, "")).strip()

    def customer_said(self, history, text):
        """Return True if text appears in a message the shopper typed."""
        for message in history:
            if message["role"] == "user" and text.lower() in message["content"].lower():
                return True
        return False
