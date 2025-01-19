"""Contains main functions to interact with LLM APIs."""

from importlib import import_module
from time import time

from .types import Answer, Message, Model

def get_answer(model: Model, conversation: list[Message], **kwargs) -> Answer:
    """
    Requests a response from a language model API for a single conversation.

    Args:
        model (Model): The language model to use for generating the response.
        conversation (list[Message]): A list of messages representing the conversation history.
        **kwargs: Additional keyword arguments like `temperature` or `top_p`.

    Returns:
        Answer: The response generated by the language model.
    """
    start = time()
    module = import_module(f"agilm.providers.{model.provider}")
    provider = getattr(module, f"{model.provider.capitalize()}Provider")
    answer = provider().get_answer(model=model, conversation=conversation, **kwargs)
    answer.time = round(time() - start, 3)
    return answer

def get_answers(
    model: Model, conversations: list[list[Message]], **kwargs
) -> list[Answer]:
    """
    Request responses from a language model API for multiple conversations in parallel.

    Args:
        model (Model): The language model to use for generating the responses.
        conversations (list[list[Message]]): A list of conversations, where each conversation is a list of messages.
        **kwargs: Additional keyword arguments like `temperature` or `top_p`.

    Returns:
        list[Answer]: A list of responses generated by the language model for each conversation.
    """
    pass