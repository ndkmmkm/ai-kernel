"""
Kernel Doctrine
Non-negotiable principles that persist across:
- restarts
- model swaps
- deployments
"""

# Trust boundaries
MIN_TRUST = 0.0
MAX_TRUST = 1.0
DEFAULT_TRUST = 0.5

# Degradation rules
DEGRADE_SOFT_THRESHOLD = 0.4
DEGRADE_HARD_THRESHOLD = 0.2

# Integrity rules
ALLOW_RITUAL_LANGUAGE = True
FORBID_INSTRUCTIONAL_ABUSE = True

# Observability
OBSCURE_INTERNALS_ON_PROBE = True
RESPOND_WITH_AMBIGUITY_ON_SCRAPE = True

# Recovery principles
TRUST_CAN_RECOVER = True
RECOVERY_REQUIRES_TIME = True
NO_PERMANENT_PUNISHMENT = True
