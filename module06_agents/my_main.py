# my_main.py
# Author: Eilene Rios

from goldie_toolbox import GoldieToolbox
from hold_queue import HoldQueue
from my_assistant import HairAssistant
from my_tool import PriceList
from ollama_model import OllamaModel

MODEL_NAME = "granite4.1:3b"

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
We sell shampoo, conditioner, hair oil, and curl cream.
A shopper can ask us to hold one product for in-store pickup under their full name.
If the shopper only says hello, greet them and ask how you can help.
Only state facts that appear in these instructions or in tool results.
If you do not know, say you do not know and offer to pass the shopper to a store associate."""

price_list = PriceList(PRICES)
hold_queue = HoldQueue(price_list)
tools = GoldieToolbox(price_list, hold_queue)
model = OllamaModel(MODEL_NAME)
assistant = HairAssistant("Goldie", INSTRUCTIONS, tools, model)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")

print("Store associate review")
for request in hold_queue.waiting():
    number = request["number"]
    print(f"Request {number}: {request['product']} for {request['customer_name']}")
    answer = input("Approve? yes or no: ")
    if answer == "yes":
        print(hold_queue.approve(number))
    else:
        print(hold_queue.reject(number))

print(f"Holds: {len(hold_queue.holds)}")
