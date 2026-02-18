  def apply_rules(message, state):
    msg = message.lower()

    # System diagnostics
    if "405" in msg:
        return "HTTP 405: incorrect request method."

    if "415" in msg:
        return "HTTP 415: Content-Type must be application/json."

    if msg.startswith("/mode"):
        mode = msg.split(" ")[1]
        state["mode"] = mode
        return f"Mode switched to {mode}"

    # Memory query
    if msg.startswith("/memory"):
        return str(state.get("memory", []))

    return None  # means no rule matched
