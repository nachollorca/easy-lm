from together import Together

from ..types import Answer, Message, Model


def _get_answer(model: Model, conversation: list[Message], **kwargs) -> Answer:
    client = Together()
    response = client.chat.completions.create(
        model=model.id,
        messages=[message.to_dict for message in conversation],
        **kwargs
    )
    return Answer(
        content=response.choices[0].message.content,
        tokens_in=response.usage.prompt_tokens,
        tokens_out=response.usage.completion_tokens
    )