# core/negotiation.py

def negotiate(builder, critic_feedback):
    """
    Builder bargains for useful information.
    """
    if critic_feedback["issues"]:
        return {
            "request": "Provide top failure case",
            "offer": "Will refactor logic"
        }
    return {
        "request": "No changes needed",
        "offer": "Maintain current model"
    }
