def generate_response(message, state):
    response = f"LLM processed message: {message}"
    return f"{response}\n\n[KERNEL V1 ACTIVE]"
