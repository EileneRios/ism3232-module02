# my_main.py
# Author: Eilene Rios

from my_assistant import HairAssistant
from my_tool import PriceList

PRICES = {
    "shampoo": "$14.00",
    "conditioner": "$15.50",
    "hair oil": "$22.00",
    "curl cream": "$18.00",
}

price_list = PriceList(PRICES)
assistant = HairAssistant(
    "Goldie",
    "You help shoppers at No Bald Spots check prices on hair products.",
    price_list,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
