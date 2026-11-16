from fake_model import FakeModel
from goldie_toolbox import GoldieToolbox
from hold_queue import HoldQueue
from my_assistant import HairAssistant
from my_tool import PriceList


class SilentModel:
    """A model that never has an answer. It stands in for Ollama being switched off."""

    def decide(self, instructions, history, tools):
        return None


def make_assistant(model):
    """Build a fresh assistant with its own tools and the model it is given."""
    price_list = PriceList({"shampoo": "$14.00", "hair oil": "$22.00"})
    tools = GoldieToolbox(price_list, HoldQueue(price_list))
    return HairAssistant("Goldie", "Be helpful.", tools, model)


def ask_for_tool(name, arguments):
    """Build the decision a model returns when it wants a tool."""
    return {"tool": name, "arguments": arguments}


def test_respond_records_both_messages():
    assistant = make_assistant(FakeModel([{"text": "Hi there!"}]))
    assistant.respond("hello")
    assert len(assistant.history) == 2
    assert assistant.history[1]["content"] == "Hi there!"


def test_model_can_ask_for_a_price():
    model = FakeModel(
        [
            ask_for_tool("check_price", {"product": "shampoo"}),
            {"text": "Shampoo is $14.00."},
        ]
    )
    assistant = make_assistant(model)
    assistant.respond("How much is the shampoo?")
    assert assistant.history[1]["content"] == "The shampoo costs $14.00."


def test_refund_goes_to_a_person_before_the_model():
    assistant = make_assistant(FakeModel([]))
    assert "store associate" in assistant.respond("I want a refund for my shampoo")


def test_made_up_name_is_refused():
    model = FakeModel(
        [
            ask_for_tool(
                "request_hold", {"product": "shampoo", "customer_name": "Jane Doe"}
            ),
            {"text": "What name should the hold be under?"},
        ]
    )
    assistant = make_assistant(model)
    assistant.respond("Please hold a shampoo for me")
    assert "has not given that name" in assistant.history[1]["content"]
    assert assistant.tools.hold_queue.waiting() == []


def test_hold_waits_for_a_store_associate():
    model = FakeModel(
        [
            ask_for_tool(
                "request_hold", {"product": "shampoo", "customer_name": "Dana Cruz"}
            ),
            {"text": "Sent to a store associate."},
        ]
    )
    assistant = make_assistant(model)
    assistant.respond("Please hold a shampoo for Dana Cruz")
    assert len(assistant.tools.hold_queue.waiting()) == 1
    assert assistant.tools.hold_queue.holds == []


def test_approve_holds_the_product_once():
    price_list = PriceList({"shampoo": "$14.00"})
    queue = HoldQueue(price_list)
    queue.request_hold("shampoo", "Dana Cruz")
    assert queue.approve(1) == "Request 1 approved."
    assert queue.approve(1) == "Request 1 is already approved."
    assert len(queue.holds) == 1


def test_unknown_tool_is_refused():
    model = FakeModel([ask_for_tool("give_discount", {}), {"text": "Sorry."}])
    assistant = make_assistant(model)
    assistant.respond("Can I get a discount?")
    assert assistant.history[1]["content"] == "There is no tool named give_discount."


def test_safe_reply_when_the_model_has_no_answer():
    assistant = make_assistant(SilentModel())
    assert "try again" in assistant.respond("Do you do haircuts?")


def test_loop_stops_after_three_tool_rounds():
    request = ask_for_tool("check_price", {"product": "shampoo"})
    assistant = make_assistant(FakeModel([request, request, request]))
    reply = assistant.respond("How much is the shampoo?")
    assert "store associate" in reply
    assert len(assistant.history) == 5
