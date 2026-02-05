# core/rewards.py

def calculate_reward(feedback):
    reward = 0

    if feedback.get("score", 0) >= 8:
        reward += 5

    if not feedback.get("issues"):
        reward += 3
    else:
        reward -= len(feedback["issues"])

    if "edge case" in feedback.get("suggestion", "").lower():
        reward += 2

    return reward
