import random

def degrade_response(reply, trust):
    if trust >= 0.8:
        return reply

    if trust >= 0.5:
        return reply  # normal, but monitored

    if trust >= 0.3:
        return (
            reply[:200]
            + "\n\n[Response condensed due to low trust.]"
        )

    if trust >= 0.1:
        return (
            "I can respond at a high level, "
            "but details are currently limited."
        )

    return (
        "I’m here, but I need more stable interaction "
        "before continuing."
    )


    return ". ".join(sentences)
