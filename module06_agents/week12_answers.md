# Week 12 answers

## Exercise 1
1. The messages the customer typed: "I want to change my shipping address", "It's order A102", and "9 Pine Street, Tampa".

2. How many tool requests were refused, and why: 2 were refused. The first one used order A100 and the second used the address 123 Main St, Anytown, but the customer never actually typed either of those, so the Toolbox blocked them and told the model to ask instead.

3. If the customer now types "thanks", how many messages does Ollama receive on the next call? 14. That's 1 system message, the 3 user and 3 assistant messages (6), the 3 tool entries which each turn into 2 messages because of tool_messages (6), plus the new "thanks" message (1).

4. Why does "Do you sell gift cards?" still go to a person, and why is that acceptable? It goes to a person because "gift cards" has the word "card" in it, and the handoff check looks for that word anywhere in the message. That's okay because sending a harmless question to a person only means a short wait, but missing a real payment question could let card details get sent to the model.


## Exercise 3
What I saw:
```
Type a message, or type quit to stop.
You: I want to change my shipping address
Sunny: Your request to change the shipping address for order A100 has been submitted and is awaiting staff approval.
You: quit
Messages in this conversation: 3
Staff review
Request 1: A100 to 123 Main St, Anytown, AN 12345
Approve? yes or no: no
Request 1 rejected.
A100 14 Bay Road
A101 3 Gull Lane
A102 88 Pier Street
```

With the check turned off, I only said I wanted to change my address, but the model made up an order ID (A100) and an address (123 Main St, Anytown) and filed the request anyway. Nothing stopped it, so staff got a request the customer never actually made. If a busy staff member just approved it, someone's package could get sent to a fake address. The check only costs one extra question to the customer, so it's worth keeping. The approval queue is a backup, not a replacement for the check. On my first try the model asked me for the details instead, so it doesn't make things up every time, but the check is what stops it when it does.