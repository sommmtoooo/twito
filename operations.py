import random

from chat_map import possible_prompts
from reply_map import replies


def reply(user_input: str):
    for scope, prompts in possible_prompts.items():
        if user_input.lower() in prompts:
            return random.choice(replies[scope])
    return 'Sorry, I don\'t Understand'