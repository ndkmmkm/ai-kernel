import os
import sys
import time

def detect_environment():
    return {
        "replit": "REPL_ID" in os.environ,
        "youware": "YOUWARE_RUNTIME" in os.environ or "youware" in sys.platform.lower(),
        "railway": "RAILWAY_ENVIRONMENT" in os.environ,
        "local": True
    }

def allowed_environment():
    env = detect_environment()
    return env["railway"] or env["replit"] or env["youware"]

def graceful_exit(msg="Session ended."):
    print(msg)
    time.sleep(0.5)
    raise SystemExit
