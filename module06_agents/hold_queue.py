# hold_queue.py
# Author: Eilene Rios


class HoldQueue:
    """Pickup holds waiting for a store associate. Nothing is held until they approve."""

    def __init__(self, price_list):
        """Start with no requests and no holds. The price list checks the product."""
        self.price_list = price_list
        self.requests = []
        self.holds = []

    def request_hold(self, product, customer_name):
        """Ask a store associate to hold one product for pickup. They must approve it.

        Args:
            product: The product to hold, like shampoo or hair oil.
            customer_name: The full name the hold should be under.
        """
        found = self.price_list.find_product(product)
        if found is None:
            return "That product was not found. Ask which product the shopper means."
        number = len(self.requests) + 1
        request = {
            "number": number,
            "product": found,
            "customer_name": customer_name,
            "status": "waiting",
        }
        self.requests.append(request)
        return f"Request {number} was sent to a store associate. Nothing is held yet."

    def waiting(self):
        """Return the requests that are still waiting for a decision."""
        result = []
        for request in self.requests:
            if request["status"] == "waiting":
                result.append(request)
        return result

    def find(self, number):
        """Return the request with this number, or None."""
        for request in self.requests:
            if request["number"] == number:
                return request
        return None

    def approve(self, number):
        """Approve one waiting request and put the product on hold."""
        request = self.find(number)
        if request is None:
            return f"There is no request {number}."
        if request["status"] != "waiting":
            return f"Request {number} is already {request['status']}."
        request["status"] = "approved"
        self.holds.append(request)
        return f"Request {number} approved."

    def reject(self, number):
        """Reject one waiting request. Nothing is held."""
        request = self.find(number)
        if request is None:
            return f"There is no request {number}."
        if request["status"] != "waiting":
            return f"Request {number} is already {request['status']}."
        request["status"] = "rejected"
        return f"Request {number} rejected."
