def update_memory(state, message, reply):
    if "memory" not in state:
        state["memory"] = []

    state["memory"].append({
        "message": message,
        "reply": reply
    })

    # optional cap
    state["memory"] = state["memory"][-20:]
