# my_assistant.py
# Author: Eilene Rios

HANDOFF_WORDS = ["refund", "return", "allergic", "reaction"]


class HairAssistant:
    """A hair shop assistant. Rules handle prices and handoffs. A model handles the rest."""

    def __init__(self, name, instructions, price_list, model):
        """Set up one assistant with its own name, instructions, tool, model, and history."""
        self.name = name
        self.instructions = instructions
        self.price_list = price_list
        self.model = model
        self.history = []

    def respond(self, user_message):
        """Record the user's message, choose a reply, record it, and return it."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Use a rule when one applies. Otherwise ask the model."""
        text = user_message.lower()
        if self.needs_human(text):
            return "I can't handle that here. I'm passing you to a store associate."
        if "price" in text or "cost" in text or "how much" in text:
            return self.price_reply(user_message)
        return self.model_reply()

    def model_reply(self):
        """Ask the model for a reply. Give a safe answer if the model has none."""
        reply = self.model.reply(self.instructions, self.history)
        if reply is None:
            return "Sorry, I can't answer that right now. Please try again in a moment."
        return reply

    def needs_human(self, text):
        """Return True if the message is about something a person must handle."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def price_reply(self, user_message):
        """Use the price list to answer a question about a product."""
        product = self.price_list.find_product(user_message)
        if product is None:
            return "Which product? I can check shampoo, conditioner, hair oil, or curl cream."
        price = self.price_list.price_for(product)
        return f"The {product} costs {price}."
