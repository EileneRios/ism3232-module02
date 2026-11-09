# my_main.py
# Author: Eilene Rios

from my_assistant import HairAssistant
from my_tool import PriceList
from ollama_model import OllamaModel

PRICES = {
    "shampoo": "$14.00",
    "conditioner": "$15.50",
    "hair oil": "$22.00",
    "curl cream": "$18.00",
}

INSTRUCTIONS = """You are Goldie, an assistant for No Bald Spots, a hair product shop.
Answer in one short sentence.
The store is open 9 am to 8 pm every day.
Orders over $35 get free shipping.
Only state facts that appear in these instructions.
If you do not know, say you do not know and offer to pass the shopper to a store associate."""

price_list = PriceList(PRICES)
model = OllamaModel("granite4.1:3b")
assistant = HairAssistant("Goldie", INSTRUCTIONS, price_list, model)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
