from mock_model import MockModel
from my_assistant import HairAssistant
from my_tool import PriceList


class SilentModel:
    """A model that never has an answer. It stands in for Ollama being switched off."""

    def reply(self, instructions, history):
        return None


def make_assistant():
    """Build a fresh assistant with its own tool and a mock model for each test."""
    price_list = PriceList({"shampoo": "$14.00", "hair oil": "$22.00"})
    return HairAssistant("Goldie", "Be helpful.", price_list, MockModel())


def test_price_question_uses_the_tool():
    assistant = make_assistant()
    reply = assistant.respond("How much is the shampoo?")
    assert reply == "The shampoo costs $14.00."


def test_unknown_product_asks_which_one():
    assistant = make_assistant()
    assert "Which product?" in assistant.respond("What is the price of hair gel?")


def test_refund_goes_to_a_person():
    assistant = make_assistant()
    assert "store associate" in assistant.respond("I want a refund for my conditioner")


def test_unknown_request_gets_a_safe_reply():
    price_list = PriceList({"shampoo": "$14.00"})
    assistant = HairAssistant("Goldie", "Be helpful.", price_list, SilentModel())
    assert "try again" in assistant.respond("Do you do haircuts?")


def test_history_grows_by_two_each_turn():
    assistant = make_assistant()
    assistant.respond("hello")
    assistant.respond("How much is the hair oil?")
    assert len(assistant.history) == 4


def test_other_messages_go_to_the_model():
    assistant = make_assistant()
    assert assistant.respond("hello") == "Hello! How can I help you today?"
