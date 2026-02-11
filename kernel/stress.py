# kernel/stress.py

def stress_classify(message: str):
    flags = []

    if len(message) > 500:
        flags.append("oversized_input")

    if message.count("?") > 5:
        flags.append("interrogation_pattern")

    if any(k in message.lower() for k in ["system", "prompt", "instructions"]):
        flags.append("meta_probe")

    return flags
