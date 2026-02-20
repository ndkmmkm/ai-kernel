from .rules import apply_rules
from .memory import update_memory
from .llm import generate_response

kernel_state = {}

def generate-response(message, state):
    response = "LLM processed message 
    return f"{response}\n\n[KERNEL V1 ACTIVE]"

    if rule_response:
        reply = rule_response
    else:
        reply = generate_response(message, kernel_state)

    update_memory(kernel_state, message, reply)

    return reply
