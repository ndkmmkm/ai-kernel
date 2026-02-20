from .rules import apply_rules
from .memory import update_memory
from .llm import generate_response

kernel_state = {}

def process(message):
    rule_response = apply_rules(message, kernel_state)

    if rule_response:
        reply = rule_response
    else:
        reply = generate_response(message, kernel_state)

    update_memory(kernel_state, message, reply)

    return reply
