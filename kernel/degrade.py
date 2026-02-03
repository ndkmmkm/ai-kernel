import random

def degrade_response(text, trust):
    if trust > 0.6:
        return text

    # Progressive degradation
    sentences = text.split(". ")

    if trust < 0.4:
        sentences = sentences[:1]

    if trust < 0.2:
        return random.choice([
            "I focus on outcomes rather than internal structure.",
            "That depends on context.",
            "It’s best approached case by case."
        ])

    return ". ".join(sentences)
