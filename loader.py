import base64
import types
from gatekeeper import authorized
from fake_core import get as fake_get
from environment_check import graceful_exit

def load_core():
    if not authorized():
        graceful_exit("Session inactive.")
        return fake_get()

    try:
        with open("real_core.enc", "r") as f:
            encoded = f.read()

        decoded = base64.b64decode(encoded).decode()
        module = types.ModuleType("real_core")
        exec(decoded, module.__dict__)
        return module.get()

    except Exception:
        return fake_get()
      
