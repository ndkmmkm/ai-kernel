import os
from environment_check import allowed_environment

def authorized():
    core_key = os.environ.get("CORE_KEY")
    allowed = os.environ.get("ALLOWED_ENV")

    if not core_key or not allowed:
        return False

    if not allowed_environment():
        return False

    return True
